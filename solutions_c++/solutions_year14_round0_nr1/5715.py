#include <iostream>
#include <fstream>
#include <cstdio>

using namespace std;
int arr2[5];
int main(){
	FILE *ifp, *ofp;
	ifp=fopen("A-small-attempt0.in","r");
	ofp=fopen("outputfile.txt","w");
	int t,rno,i,j,count,ans;
	int arr[5][5];
	fscanf(ifp,"%d",&t);
	int caseno=1;
	while(caseno<=t){
	count=0;
	fscanf(ifp,"%d",&rno);
	for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
			fscanf(ifp,"%d",&arr[i][j]);
	
	for(i=1;i<5;i++)
		arr2[i]=arr[rno][i];		
		
	fscanf(ifp,"%d",&rno);
	
	for(i=1;i<5;i++)
		for(j=1;j<5;j++)
			fscanf(ifp,"%d",&arr[i][j]);
			
	for(i=1;i<=4;i++)
		for(j=1;j<=4;j++)
			if(arr[rno][i]==arr2[j])
				{count++;ans=arr2[j];}
	
	switch(count){
		case 0:fprintf(ofp,"Case #%d: Volunteer cheated!\n",caseno);
			break;
		case 1:fprintf(ofp,"Case #%d: %d\n",caseno,ans);
			break;
		case 2:
		case 3:
		case 4:fprintf(ofp,"Case #%d: Bad Magician!\n",caseno);
			break;	
		}
	caseno++;	
	}
	fclose(ifp);
	fclose(ofp);
return 0;
}
