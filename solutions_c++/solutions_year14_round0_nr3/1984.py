#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include <string>
#include <map>

using namespace std;

/*
int test2(int field[][], int R, int C){
	int x,y;
	for (y=0;y<R;y++){
		for (x=0;x<C;x++){
			if (test2(field,R,C))
				return 1;
		}
	}
}
*/

#define RMAX 10
#define CMAX 10

void print_field_(int field[CMAX][RMAX],int R, int C){
	int x,y;
	for (y=0;y<R;y++){
		for (x=0;x<C;x++){
			if (field[x][y]==-1)printf("*");
			else if (field[x][y]==0)printf(".");
			else printf("%d",field[x][y]);
		}
	}
	printf("\n");
	char tmp_s[CMAX*RMAX+1];
	int i=0;
	for (y=0;y<R;y++){
		for (x=0;x<C;x++){
			if (field[x][y]==-1)tmp_s[i]='*';
			else if (field[x][y]==0)tmp_s[i]='.';
			else assert(0);
			i++;
		}
	}
	tmp_s[i]='\0';
	printf("%s\n",tmp_s);
}

void print_field(int field[CMAX][RMAX],int R, int C){
	print_field_(field,R,C);
	int x,y;
	for (y=0;y<R;y++){
		for (x=0;x<C;x++){
			if (field[x][y]==-1)printf("*");
			else if (field[x][y]==0)printf(".");
			else printf("%d",field[x][y]);
		}
		printf("\n");
	}
	printf("\n");
}

map<string,int> field_memo;

void field_memo_clear(void){
	field_memo.clear();
}

void field_memo_add(int field[CMAX][RMAX], int R, int C)
{
	char tmp_s[CMAX*RMAX+1];
	int i=0;
	int x,y;
	for (y=0;y<R;y++){
		for (x=0;x<C;x++){
			if (field[x][y]==-1)tmp_s[i]='*';
			else if (field[x][y]==0)tmp_s[i]='.';
			else assert(0);
			i++;
		}
	}
	tmp_s[i]='\0';
	field_memo[string(tmp_s)]=0;
	//fprintf(stderr,"add %s\n",tmp_s);
}

// return 0 if when it is already checked as 0
int field_memo_lookup(int field[CMAX][RMAX], int R, int C)
{
	char tmp_s[CMAX*RMAX+1];
	int i=0;
	int x,y;
	for (y=0;y<R;y++){
		for (x=0;x<C;x++){
			if (field[x][y]==-1)tmp_s[i]='*';
			else if (field[x][y]==0)tmp_s[i]='.';
			else assert(0);
			i++;
		}
	}
	tmp_s[i]='\0';
	int ret=field_memo.find(string(tmp_s))==field_memo.end();
	//if (ret)
	//	fprintf(stderr,"%s is new\n",tmp_s);
	//else fprintf(stderr,"%s is not new\n",tmp_s);
	return ret;
}

void mark_field(int field[CMAX][RMAX], int R, int C){
	int x,y;
	for (y=0;y<R;y++){
		for (x=0;x<C;x++){
			if (field[x][y]==-1){
				// mine, mark neighbors
				int xx,yy;
				for (yy=y-1;yy<=y+1;yy++){
					if (yy<0 || yy>=R)continue;
					for (xx=x-1;xx<=x+1;xx++){
						if (xx<0 || xx>=C)continue;
						if (field[xx][yy]!=-1)
							field[xx][yy]++;
					}
				}
			}
		}
	}
}

int check_(int mfield[CMAX][RMAX], int opened[CMAX][RMAX], int ox, int oy, int R, int C){
	if (opened[ox][oy])return 0;
	assert(mfield[ox][oy]!=-1);
	opened[ox][oy]=1;
	if (mfield[ox][oy]!=0)return 1;
	int ret=1;
	int xx,yy;
	for (yy=oy-1;yy<=oy+1;yy++){
		if (yy<0 || yy>=R)continue;
		for (xx=ox-1;xx<=ox+1;xx++){
			if (xx<0 || xx>=C)continue;
			ret+=check_(mfield,opened,xx,yy,R,C);
		}
	}
	return ret;
}

int check(int field[CMAX][RMAX], int R, int C, int M, int *ox, int *oy){
	int opened[CMAX][RMAX];
	int x,y;
	int mfield[CMAX][RMAX];
	memcpy(mfield,field,sizeof(int)*RMAX*CMAX);
	mark_field(mfield,R,C);
	//print_field(mfield,R,C);
	for (y=0;y<R;y++){
		for (x=0;x<C;x++){
			memset(opened,0,sizeof(opened));
			if (mfield[x][y]!=-1){
				int ret=check_(mfield,opened,x,y,R,C);
				//fprintf(stderr,"open (%d,%d) %d\n",x,y,ret);
				if (ret+M==R*C){
					*ox=x;*oy=y;
					return 1;
				}
			}
		}
	}
	return 0;
}

int put_mine(int field[CMAX][RMAX], int Mrest, int Midx, int R, int C, int M,int afield[CMAX][RMAX], int *ox, int *oy){
	int ret;
	int ox_,oy_;
	// If all mines are already put, finish
	if (Mrest==0){
		// Check the field
		//print_field(field,R,C);
		ret=check(field,R,C,M-Mrest,&ox_,&oy_);
		if (!ret){
			field_memo_add(field,R,C);
			return 0;
		}
		//print_field(field,R,C);
		memcpy(afield,field,sizeof(int)*RMAX*CMAX);
		*ox=ox_;*oy=oy_;
		return 1;
	}
	// try to put a mine in the new place
	if (Midx>=R*C)return 0;
	int x,y;
	y=Midx/C;
	x=Midx%C;
	assert(y*C+x==Midx);
	for (;y<R;y++){
		for (;x<C;x++){
			if (Midx>=R*C)goto myexit;
			//fprintf(stderr,"%d %d\n",x,y);
			assert(field[x][y]!=-1);
			field[x][y]=-1;
			//assert(field_memo_lookup(field,R,C)==1);
			/*if (field_memo_lookup(field,R,C))*/{
				// recursion
				if (put_mine(field,Mrest-1,Midx+1,R,C,M,afield,ox,oy)==1)return 1;
			}
			// restore
			field[x][y]=0;
			Midx++;
		}
	}
myexit:;
	field_memo_add(field,R,C);
	return 0;
}

int main(int argc,char **argv)
{
	int t,T;
#if 1
	scanf("%d\n",&T);
	for (t=1;t<=T;t++){
		int R,C,M;
		int field[CMAX][RMAX],afield[CMAX][RMAX];
		int ox,oy;
		memset(field,0,sizeof(field));
		field_memo_clear();
		scanf("%d %d %d\n",&R,&C,&M);
		printf("Case #%d:\n",t);
		if (put_mine(field,M,0,R,C,M,afield,&ox,&oy)){
			int x,y;
			for (y=0;y<R;y++){
				for (x=0;x<C;x++){
					if (x==ox && y==oy)printf("c");
					else if (afield[x][y]==-1)printf("*");
					else printf(".");
				}
				printf("\n");
			}
		}
		else{
			 printf("Impossible\n");
		}
	}
#else
	int f[5][5]={
			{0,0,0,-1,-1},
			{0,0,0,-1,-1},
			{-1,-1,-1,-1,-1},
			{-1,-1,-1,-1,-1},
			{-1,-1,-1,-1,-1}
	};
	int a=-1,b=-1;
	int ret=check(f,5,5,19,&a,&b);
	printf("%d (%d,%d)\n",ret,a,b);
#endif
	return 0;
}
