#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<algorithm>

using namespace std;

long long int a[1007],b[1007];

int main(){
	
	FILE *p1,*p2;
	p1=fopen("A-large.txt","r");
	p2=fopen("Output.txt","w");
	long long int t,i,j,n;
	
	fscanf(p1,"%lld\n",&t);
	for(i=0;i<t;i++){	
		fscanf(p1,"%lld\n",&n);
		for(j=0;j<n-1;j++)fscanf(p1,"%lld",&a[j]);
		fscanf(p1,"%lld\n",&a[j]);
		
		long long int ans1=0,maxi=0;
		for(j=1;j<n;j++){
			if(a[j]<a[j-1]){
				maxi=max((a[j-1]-a[j]),maxi);
				ans1+=(a[j-1]-a[j]);
			}
			
		}
		long long ans2=0;
		for(j=0;j<n-1;j++){
			if(a[j]<=maxi)ans2+=a[j];
			else ans2+=maxi;
		}
		
		fprintf(p2,"Case #%lld: %lld %lld\n",i+1,ans1,ans2);
	}
	
	//system("PAUSE");
	return 0;	

}
