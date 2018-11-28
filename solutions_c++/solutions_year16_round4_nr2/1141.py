#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<cmath>
#include<sstream>
#include<algorithm>
#include<set>
#include<ctime>
using namespace std;
int n;
int main(){
	
	
	int tc;
	cin>>tc;
	for(int caso=1;caso<=tc;caso++){
		cout<<"Case #"<<caso<<": ";
		int n,k;
		cin>>n>>k;
		double p[n];
		
		int id[1<<k];
		int tid=0;
		for(int j=0;j<(1<<k);j++){
			if(__builtin_popcount(j)==k/2)
				id[tid++]=j;
		}
		
		for(int i=0;i<n;i++)cin>>p[i];
		
		
		double dev=0;
		for(int i=0;i<(1<<n);i++){
			if(__builtin_popcount(i)==k){
				double c[k];
				int cont=0;
				for(int j=0;j<n;j++)
					if( (i&(1<<j))!=0 )
						c[cont++]=p[j];
				
				double sum=0;
				/*
				for(int j=0;j<tid;j++){
					double prod=1;
					for(int m=0;m<k;m++){
						if( (id[j]&(1<<m))==1 )
							prod*=c[m];
						else
							prod*=(1-c[m]);
					}
					sum+=prod;
				}
				*/
				
				for(int j=0;j<(1<<k);j++){
					if(__builtin_popcount(j)!=k/2)continue;
			
					double prod=1;
					for(int m=0;m<k;m++){
						if( (j&(1<<m))!=0 ){
							prod*=c[m];
							
						}
						else{
							prod*=(1-c[m]);
						}
					}
					sum+=prod;
				}
				dev=max(dev,sum);
			}
		}
				printf("%.10lf\n",dev);
		
		
	}
	
    return 0;
}

