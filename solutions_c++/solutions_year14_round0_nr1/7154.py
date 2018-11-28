#include<iostream>
#include<iomanip>
#include<cstdio>
using namespace std;
main(){
int t;
cin>>t;
for(int i=0;i<t;i++){
	int r1,r2;
	cin>>r1;
	int mat1[4][4],mat2[4][4];
	for(int j=0;j<4;j++)
	cin>>mat1[j][0]>>mat1[j][1]>>mat1[j][2]>>mat1[j][3];
	cin>>r2;
	for(int j=0;j<4;j++)
	cin>>mat2[j][0]>>mat2[j][1]>>mat2[j][2]>>mat2[j][3];
	r1--;r2--;
	int count =0,ans;
	for(int j=0;j<4;j++)
	for(int k=0;k<4;k++)
	if(mat1[r1][j]==mat2[r2][k])
	{count++;ans=mat1[r1][j];}
	if(count==1)
	printf("Case #%d: %d\n",i+1,ans);
	else if(count==0)
	printf("Case #%d: Volunteer cheated!\n",i+1);
	else
	printf("Case #%d: Bad magician!\n",i+1);
}
}