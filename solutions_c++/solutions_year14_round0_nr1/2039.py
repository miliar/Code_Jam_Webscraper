#include <stdio.h>
#include <algorithm>
#include <iostream>

using namespace std;

FILE *in, *out;


int main(){

	int t=0;
	int i=0, j=0;

	in=fopen("A-small-attempt0.in","r");
	out=fopen("A-small-attempt0.out","w");

	fscanf(in,"%d",&t);


	for(int a=0; a<t; a++){
		int row1=0, row2=0;
		int arr1[5][5]={0,};
		int arr2[5][5]={0,};
		int cnt=0, ans=0;

		fscanf(in,"%d",&row1);
		for(i=1; i<5; i++)
			for(j=1; j<5; j++)
				fscanf(in,"%d",&arr1[i][j]);
		fscanf(in,"%d",&row2);
		for(i=1; i<5; i++)
			for(j=1; j<5; j++)
				fscanf(in,"%d",&arr2[i][j]);


		for(i=1; i<5; i++){
			for(j=1; j<5; j++){
				if(arr2[row2][j]==arr1[row1][i]){
					cnt++;
					ans=arr2[row2][j];
				}
			}
		}
		if(cnt==1) fprintf(out,"Case #%d: %d\r\n",a+1,ans);
		else if(cnt>1) fprintf(out,"Case #%d: Bad magician!\r\n",a+1);
		else fprintf(out,"Case #%d: Volunteer cheated!\r\n",a+1);

	}

	fclose(in);
	fclose(out);

	return 0;


}