#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <regex>
#include <algorithm>
#include <iomanip>

#define large
#ifdef none
#define T 100
#define N 10
#endif

#ifdef small
#define T 100
#define N 10
#endif

#ifdef large
#define N 100
#define T 1000
#endif



		 

void main(){
FILE *O,*I;
#ifdef none
freopen_s(&I,"bt.in","r+",stdin);
freopen_s(&O,"bt.out","w+",stdout);
#endif
#ifdef small
freopen_s(&I,"b-small-attempt3.in","r+",stdin);
freopen_s(&O,"b-small-attempt3.out","w+",stdout);
#endif

#ifdef large
freopen_s(&I,"b-large.in","r+",stdin);
freopen_s(&O,"b-large.out","w+",stdout);
#endif

	int t,n,m;
	int mat[N][N];

	std::cin>>t;
	
	for(int i=1;i<=t;i++){
		int flag1=0,flag2=0;
		std::cin>>n>>m;
		
		//std::cin.getline(buff,2*N+1,'\n');
		for(int j=0;j<n;j++){
		//std::cin.getline(buff,2*N+1,'\n');		
		//std::istringstream ss(buff);
		
			for(int k=0;k<m;k++){
				std::cin>>mat[j][k];
			}
		}
		if(m==1||n==1){
			std::cout<<"Case #"<<i<<": YES"<<std::endl;
			
			continue;
		}
		
		for(int p=0;p<n&&(!flag1||!flag2);p++){
			for(int q=0;q<m&&(!flag1||!flag2);q++){
				int ele =mat[p][q];flag1=0;flag2=0;
				for(int k=0;k<n;k++){
					if(mat[k][q]>ele){
						flag1=1;
						break;
					}
				}
				for (int k=0;k<m;k++){
					if(mat[p][k]>ele){
						flag2=1;
						break;
					}
				}
			}
		}

		if(flag1&&flag2){
		
		std::cout<<"Case #"<<i<<": NO"<<std::endl;
		}
		else {
			std::cout<<"Case #"<<i<<": YES"<<std::endl;
		}
	}

					
				
			
}



