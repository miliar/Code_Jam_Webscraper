#include <stdio.h>
#include <cassert>
#include <iostream>

using namespace std;

#define JUDGE 1
#define MAXSIZE 105

int main(){
	
	if(JUDGE){
		freopen("input","r",stdin);
		freopen("output","w",stdout);
	}
	
	int t;
	int rec[MAXSIZE][MAXSIZE];
	scanf("%d",&t);
	for(int tt=1;tt<=t;tt++){
		
		int n,m;
		scanf("%d%d",&n,&m);
		for(int i=0;i<n;i++)
			for(int j=0;j<m;j++)
				scanf("%d",&rec[i][j]);
		
		bool flag=true;
		bool flag1=true;
		
		for(int i=0;i<n;i++){
			
			bool temp=true;
			for(int j=0;j<m;j++){
				
				if(rec[i][j] != rec[0][j]){
					temp=false;
				}
			}
			if(temp)
			{
				flag1=true;
				break;
			}
			
		}
		
		
		if(!flag1){
			
			for(int j=0;j<m;j++){
			
				bool temp=true;
				for(int i=0;i<n;i++){
					
					if(rec[i][j] != rec[i][0]){
						temp=false;
					}
				}
				if(temp)
				{
					flag1=true;
					break;
				}
				
			}
		}
			
		for(int i=0;i<n;i++){
			for(int j=0;j<m;j++){
				bool b1=true,b2=true,check=true;
				for(int p=0;p<n;p++){
					if(rec[p][j]>rec[i][j]){
						b1=false;
						break;
					}
				}
				
				for(int p=0;p<m;p++){
					if(rec[i][p]>rec[i][j]){
						b2=false;
						break;
					}
				}
				
				check=b1||b2;
				if( !check){
					flag=false;
					break;
				}
			}
			if(!flag)
				break;
		}
		
		flag = flag && flag1;
		if(flag)
			printf("Case #%d: YES\n",tt);
		else
			printf("Case #%d: NO\n",tt);
				
	}
	return 0;	

}