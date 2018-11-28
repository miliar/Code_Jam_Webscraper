#include <stdio.h>
#include <iostream>
#include <algorithm>
#include <string.h>
#include <math.h>


using namespace std;

void func(int t);

FILE *f1,*f2;
	

int main(){

	int t=0;

	f1=fopen("A-small-attempt0.in","r");
	f2=fopen("A-small-attempt0.out","w");


	fscanf(f1,"%d",&t);

	for(int a=0; a<t; a++)
		func(a+1);

	return 0;

}

void func(int t){
	
	int n=0, x=0,y, z, w;
	char str[100][2][102];
	int cnt[100][100]={0,};
	int max[100]={0,};
	int sum=0;

	fscanf(f1,"%d",&n);


	for(z=0; z<n; z++){
		x=0;
	
		fscanf(f1,"%s",str[z][0]);

	for(y=0; str[z][0][y]!=0; y++){
		if(str[z][0][y]==str[z][0][y+1]) cnt[z][x]++;
		else {
			str[z][1][x++]=str[z][0][y];
			
		}
	}
	str[z][1][x]=0;
	}


//	cout<<"*"<<str[0][1]<<endl<<"*"<<str[1][1]<<endl;

	for(z=0; z<n-1; z++){
		for(w=z+1; w<n; w++){
			if(strcmp(str[z][1], str[w][1])==0){
				for(x=0; str[z][1][x]!=0; x++){
					if(max[x]<abs(cnt[z][x]-cnt[w][x]))  max[x]=abs(cnt[z][x]-cnt[w][x]);

				}
			}
			else{
				fprintf(f2,"Case #%d: Fegla Won\n",t);
				return;
			}
		}
	}


	for(y=0; y<x; y++){
//		cout<<"max[y]="<<max[y]<<endl;
		sum+=max[y];
	}

	fprintf(f2,"Case #%d: %d\n",t,sum);
	return;





}