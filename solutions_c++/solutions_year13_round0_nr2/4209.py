#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string>
#include<string.h>
#include<vector>
#include<iostream>
#include<map>

using namespace std;

int lawn[101][101];

int main(){

	int tt;
	scanf("%d",&tt);
	for(int kk = 1;kk<=tt;kk++){
		printf("Case #%d: ",kk);
		int n,m,maximo=0;
		scanf("%d %d",&n,&m);
		
		if(n==1 || m==1){
			//printf("YES\n");
			//continue;
		}
		
		for(int i = 0;i<n;i++){
			for(int j = 0;j<m;j++){
				scanf("%d",&lawn[i][j]);
				maximo = max(maximo,lawn[i][j]);
			}
		}		
		
		int lol=0;
		while(1){
			if(!n || !m) break;
			
			int minc=0,minr=0,min=25000;
			for(int i = 0;i<n;i++){
				for(int j = 0;j<m;j++){
					 if(min>lawn[i][j]){
					 	minr = i;
					 	minc = j;
					 	min = lawn[i][j];
					 }
				}
			}
			
			for(int i = 0;i<n;i++){
				for(int j = 0;j<m;j++){
					//cout<<lawn[i][j]<<" ";
				}
				//cout<<endl;
			}
			
			//cout<<minr<<" - "<<minc<<" - "<<min<<endl; 
			
			int numc = 0, numr = 0;
        	bool rb = true, cb = true;
        	// check the whole row		        	
        	for(int j = 0; j < m; j++)
        		if (lawn[minr][j] == min)
        			numr++;
        	if (numr != m)
        		rb = false;
        	
        	// check the whole column
        	for(int j = 0; j < n; j++)
        		if (lawn[j][minc] == min)
        			numc++;
        	if (numc != n)
        		cb = false;
        	//cout<<n<<"/"<<m<<endl;
			//cout<<numr<<"/"<<numc<<endl;        		
			//cout<<rb<<"/"<<cb<<endl;
        	if(!rb && !cb){
        		printf("NO\n");
        		break;
        	}

        	if(cb){
        		for(int i = 0;i<n;i++){
        			lawn[i][minc] = lawn[i][m-1];
        		}
        		m--;
        	}
        	else if(rb){
        		for(int i = 0;i<m;i++){
        			lawn[minr][i] = lawn[n-1][i];
        		}
        		n--;
        	}
		}
		if(!n || !m) printf("YES\n");
		
	}

	return 0;
}
