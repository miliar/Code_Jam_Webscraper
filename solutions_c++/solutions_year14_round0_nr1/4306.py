#include <iostream>
using namespace std;

int main() {
int t,arr1[5][5],i,j,num,count,k=0,ans;
cin>>t;
while(t--)
{
k++;
int count=0;
int arr2[17]={0};
cin>>num;
for(i=1;i<=4;i++)
{
for(j=1;j<=4;j++)
{

cin>>arr1[i][j];

}
}
for(j=1;j<=4;j++)
{
arr2[arr1[num][j]]++;
}
cin>>num;
for(i=1;i<=4;i++)
{
for(j=1;j<=4;j++)
{

cin>>arr1[i][j];

}
}
for(j=1;j<=4;j++)
{
if(arr2[arr1[num][j]]==1)
{count++;ans=arr1[num][j];
}}
if(count==0)
printf("Case #%d: Volunteer cheated!\n",k);
else if(count==1)
printf("Case #%d: %d\n",k,ans);
else
printf("Case #%d: Bad magician!\n",k);
}
	return 0;
}