#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cmath>
#include<algorithm>

using namespace std;



int main(){
	
	FILE *p1,*p2;
	p1=fopen("B-small-attempt0.in","r");
	p2=fopen("Output.txt","w");
	
	if(p1!=NULL){
		int T,i,n,j;
		fscanf(p1,"%d\n",&T);
		for(i=0;i<T;i++){
			fscanf(p1,"%d\n",&n);
			int count=0;
			int s[n];
			for(j=0;j<n-1;j++)
			fscanf(p1,"%d",&s[j]);
			
			fscanf(p1,"%d\n",&s[j]);
			
			int max=s[0];
			for(j=1;j<n;j++){
				if(s[1]>max)max=s[1];
			}
			
			
			//CALCULATIONS
			
			sort(s,s+n);
			//for(j=0;j<n;j++)
			//cout<<s[j]<<' ';
			//cout<<endl;
			int k;
			for()
			
			for(j=0;j<n;j++){
				if(s[j]==0)continue;
				else{
					count+=s[j];
					k=j+1;
					while(k<n){
						s[k]-=s[j];
					}
					
				}
			}
			
			fprintf(p2,"Case #%d: %d\n",i+1,count);
			
			
	
	}
	
	
	fclose(p1);
	fclose(p2);
}
	system("PAUSE");
	return 0;
}
