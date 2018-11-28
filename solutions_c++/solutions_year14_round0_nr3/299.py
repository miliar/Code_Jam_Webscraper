#include <stdio.h>
#include <memory.h>
int max(int x, int y){return x<y ? y : x;}
int min(int x, int y){return x>y ? y : x;}

bool stdSet(int l, int m, char *res){
	memset(res+l-m, '*', m);
	memset(res+1,'.',l-m-1);
	res[0]='c';
	return true;
}

bool solve(int r, int c, int m, char *res){
	int mn = min(r,c);
	if(mn == 1 || m==r*c-1)return stdSet(r*c,m,res);
	else if(mn == 2){
		if(m & 1 || m == r*c-2)return false;
		if(c == 2)return stdSet(r*c, m, res);
		memset(res, '*', m/2);
		memset(res+c, '*', m/2);
		memset(res+m/2, '.', c-m/2);
		memset(res+c+m/2,'.', c-m/2-1);
		res[c*2-1]='c';
		return true;
	}
	int d = r*c-m;
	switch(d){
		case 2: 
		case 3:
		case 5:
		case 7:
			return false;
	}
	res[0] = 'c';
	if(d<=c*2+1){
		stdSet(r*c, (r-2)*c, res);
		if(d&1){                                
			res[c*2]=res[c*2+1]=res[c*2+2]='.'; 
			d-=3; //now 2c > d >= 6;
		}
		d/=2;
		memset(res+d, '*', c-d);
		memset(res+c+d, '*', c-d);
		return true;
	}
	stdSet(r*c, m, res);
	if(d%c == 1){// d >= 3c+1;
		res[d] = '.';
		res[d-2] = '*';
	}
	return true;
}

int main(){
	FILE *fin = fopen("input.txt","r"), *fout;
	if(!fin){printf("no input\n"); return 0;}
	fout = fopen("output.txt","w");
	int i, j, T=0, r, c, m;
	if(fscanf(fin,"%d",&T)!=1)return 0;
	char *str=0;
	for(i=1; i<=T; i++){
		if(i==35){
			i=i;
		}
		fscanf(fin, "%d%d%d", &r, &c, &m);
		str = new char[r*c+c+2];
		str[r*c+c+1]=0;str[r*c+c]='\n';
		fprintf(fout, "case #%d:\n", i);
		if(solve(r,c,m,str)){
			for(j=0; j<r; j++){
				memcpy(str+r*c, str+j*c, c);
				fputs(str+r*c, fout);
			}
		}else fprintf(fout, "Impossible\n");
//		for(j=0; j<m*n; j++)fscanf(fin, "%d", str+j);
		delete[]str;
	}
	fclose(fin); fclose(fout);
	return 0;
}