#include"stdio.h"
#include"string.h"
#include"algorithm"
using namespace std;
char out[1000][1000];
void solve1(int r,int c,int m)
{
	int blank=r*c-m;
	for(int i=0;i<r;i++)
 	{
	 	 for(int j=0;j<c;j++)
		 {
		 	if(blank>0){
		 		if(i==0&&j==0)
		 		printf("c");
		 		else
			 	printf(".");
		 		blank--;
		 	}
		 	else{
		 		printf("*");
		 	}
		 }
		 puts("");
	 } 
}
void solve2(int r,int c,int m){
	int blank=r*c-m;
	if(blank%2!=0&&blank!=1||blank==2){
		puts("Impossible");
		return;
	}
	if(r>c){
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				if(blank>0){
		 		if(i==0&&j==0)
		 		out[i][j]='c';
		 		else
			 	out[i][j]='.';
		 		blank--;
			 	}
			 	else{
			 	out[i][j]='*';
			 	}
			}
		}	
		
	}
	else{
		for(int j=0;j<c;j++){
			for(int i=0;i<r;i++){
			if(blank>0){
		 		if(i==0&&j==0)
		 		out[i][j]='c';
		 		else
			 	out[i][j]='.';
		 		blank--;
			 	}
			 	else{
			 	out[i][j]='*';
			 	}
			}
		}
	}
		for(int i=0;i<r;i++,puts("")){
			for(int j=0;j<c;j++){
				printf("%c",out[i][j]);
			}
		}
}
void solve3(int r,int c,int m,int delta){
	int blank=r*c-m;
	if(blank==2||blank==3||blank==5||blank==7){
		puts("Impossible");
		return;
	}	
	for(int i=0;i<r;i++)
	for(int j=0;j<c;j++)
	out[i][j]='*';
	if(blank==1){
		
		 	out[0][0]='c';
	}else 
	if(blank%3==1)
	{
		blank-=4;
		int tmp=blank;
		for(int i=0;i<r;i++)
		 	for(int j=0;j<c;j++)
		 	{
 				if(blank>0){
			 	out[i][j]='.';
		 		blank--;
			 	}
			 	else{
			 		out[i][j]='.';
					out[i][j+1]='.';
					out[i+1][j]='.';
					out[i+1][j+1]='.'; 	
	 				goto st;
			 	}
			}
		st:;
 	
		out[0][0]='c';
		
	}
	
	else {
		for(int i=0;i<r;i++)
		 	for(int j=0;j<c;j++)
		 	{
 				if(blank>0){
			 	out[i][j]='.';
		 		blank--;
			 	}
			 	else{
			 	out[i][j]='*';
			 	}
			}
		out[0][0]='c';	
	}
	if(delta==0){
		for(int i=0;i<r;i++,puts("")){
			for(int j=0;j<c;j++){
				printf("%c",out[i][j]);
			}
		}
	}
	else{
		for(int j=0;j<c;j++,puts("")){
			for(int i=0;i<r;i++){
				printf("%c",out[i][j]);
			}
		}
	}
}
void solve4(int r,int c,int m){
	int tr=r;
	int tc=c;
	for(int i=0;i<r;i++)
	for(int j=0;j<c;j++)
	out[i][j]='.';
	if(m==0){
		out[0][0]='c';
			for(int i=0;i<tr;i++,puts("")){
			for(int j=0;j<tc;j++){
				printf("%c",out[i][j]);
			}
		}
		return;
	}
	if(r%2&&c%2)
	{
		if(m>r+c-1)
		{
			m-=r+c-1;
			for(int j=0;j<c;j++)
			out[r-1][j]='*';
			for(int j=0;j<r;j++)
			out[j][c-1]='*';
		
		}
		else{
			int cnt=0;
			int left=0;
			if(m%2==0)
			{
				left=1;
				m-=1;
			}
			for(int j=0;j<c&&cnt<m;j++,cnt++)
			out[r-1][j]='*';
			for(int j=r-2;j>=0&&cnt<m;j--,cnt++)
			out[j][c-1]='*';			
			m=left;
		}		
		r-=1;
		c-=1; 
	}
	else if(r%2){
		if(m>r)
		{
			m-=c;
			for(int j=0;j<c;j++)
			out[r-1][j]='*';
		}
		else{
			int cnt=0;
			int left=0;
			if(m%2!=0)
			{
				left=1;
				m-=1;
			}
			for(int j=0;j<c&&cnt<m;j++,cnt++)
			out[r-1][j]='*';	
			m=left;
		}
		r-=1;
	}
	else if(c%2){
		if(m>c)
		{
			m-=r;
			for(int j=0;j<r;j++)
			out[j][c-1]='*';
		
		}
		else{
			int cnt=0;
			int left=0;
			if(m%2!=0)
			{
				left=1;
				m-=1;
			}
			for(int j=r-1;j>=0&&cnt<m;j--,cnt++)
			out[j][c-1]='*';			
			m=left;
		}	
		c-=1;	
	}
	int blank=r*c-m;
	if(blank==2||blank==3||blank==5||blank==7){
		puts("Impossible");
		return;
	}

	if(m==1){
		for(int i=0;i<r;i++)
		for(int j=0;j<c;j++)
		out[i][j]='.';
		out[0][0]='*';
		out[2][2]='c';
	}else if(blank<12){
		for(int i=0;i<r;i++)
	 	for(int j=0;j<c;j++)
	 	{
	 		out[i][j]='*';
	 	}
		if(blank==1)
		{
			out[0][0]='c';	
		}
		else if(blank==4){
			out[0][0]='c';
			out[0][1]='.';
			out[1][0]='.';
			out[1][1]='.';
		}
		else if(blank==6){		
			out[0][0]='c';
			out[0][1]='.';
			out[1][0]='.';
			out[1][1]='.';
			out[0][2]='.';
			out[1][2]='.';
		}
		else if(blank==8)
		{
			out[0][0]='c';
			out[0][1]='.';
			out[1][0]='.';
			out[1][1]='.';
			out[0][2]='.';
			out[1][2]='.';
			out[0][3]='.';
			out[1][3]='.';
		}
		else if(blank==9){
			out[0][0]='c';
			out[0][1]='.';
			out[1][0]='.';
			out[1][1]='.';
			out[0][2]='.';
			out[1][2]='.';
			out[2][0]=out[2][1]=out[2][2]='.';
		}else if(blank==10){
			out[0][0]='c';
			out[0][1]='.';
			out[1][0]='.';
			out[1][1]='.';
			out[0][2]='.';
			out[1][2]='.';
			out[0][3]='.';
			out[1][3]='.';
			out[2][0]='.';
			out[2][1]='.';
		}else if(blank==11){
			out[0][0]='c';
			out[0][1]='.';
			out[1][0]='.';
			out[1][1]='.';
			out[0][2]='.';
			out[1][2]='.';
			out[0][3]='.';
			out[1][3]='.';
			out[2][0]='.';
			out[2][1]='.';
			out[2][2]='.';
		}
		
				
	}else{
		int tmp=blank/4;
		int left=blank%4;
			for(int i=0;i<r;i++)
	 	for(int j=0;j<c;j++)
	 	{
	 		out[i][j]='*';
	 	}
		for(int i=0;i<r;i+=2)
		 for(int j=0;j<c;j+=2)
		 	{
		 		if(tmp>0)
		 		{
				 	if(tmp==1&&(j+2==c||i==0)&&left)
				 	{
		 				j=c;
		 				continue;
	 				}
		 			out[i][j]=out[i+1][j]=out[i][j+1]=out[i+1][j+1]='.';
		 			tmp--;
		 		
		 			 
			 	}
			 	else if(tmp==0&&left!=0)
			 	{
	 				for(int q=j;q<j+2;q++)
	 					for(int p=i;p<i+2;p++)
	 					 if(left>0)
	 					 {
 					 	    out[p][q]='.';
							left--;	
 					 	 }
 					 	 else{
 	 					 	out[p][q]='*';
 	 					 }
	 			}
	 			else{
			 		out[i][j]=out[i+1][j]=out[i][j+1]=out[i+1][j+1]='*';
			 	}
		 		
	 		}
	 	out[0][0]='c';	
	}
		for(int i=0;i<tr;i++,puts("")){
			for(int j=0;j<tc;j++){
				printf("%c",out[i][j]);
			}
		}
}
int main()
{
	int t,cas=1;
	freopen("1.out","w",stdout);
	scanf("%d",&t);
	while(t--){
		int r,c,m;
		scanf("%d%d%d",&r,&c,&m);
		printf("Case #%d:\n",cas++);
		if(min(r,c)==1)
		{
			solve1(r,c,m);
		}
		else if(min(r,c)==2)
		{
			solve2(r,c,m);
		}
		else if(min(r,c)==3)
		{
			if(r>c)
			solve3(r,c,m,0);
			else 
			solve3(c,r,m,1);
		}
		else{
			solve4(r,c,m);
		}
	}
} 