#include <stdio.h> 
#include <stdlib.h> 
#include <math.h> 
#include <algorithm> 
#include <vector> 
#include <stack> 
#include <queue> 
  
using namespace std; 

int main(){ 
	int t;
	FILE *input,*output;

	input=fopen("A-large.in","r");
	output=fopen("output.txt","w");

	fscanf(input,"%d",&t);

	for(int i=1;i<=t;i++){
		int ma;
		int ans=0;

		fscanf(input,"%d",&ma);

		int numofstanding=0;
		char tra;

		fscanf(input,"%c",&tra);
		fscanf(input,"%c",&tra);

		numofstanding+=(int)(tra-48);

		for(int j=1;j<=ma;j++){
			fscanf(input,"%c",&tra);

			if(numofstanding<j && (int)(tra-48)!=0){
				ans+=j-numofstanding;
				numofstanding+=j-numofstanding;
			}

			numofstanding+=(int)(tra-48);
		}
		fscanf(input,"%c",&tra);

		fprintf(output,"Case #%d: %d\n",i,ans);
	}

	fclose(input);
	fclose(output);

	return 0;
}