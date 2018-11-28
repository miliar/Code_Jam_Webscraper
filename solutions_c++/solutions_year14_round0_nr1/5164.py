#include<stdio.h>
#include<malloc.h>
#include<fstream>
using namespace std;
int arr1[4][16],arr2[4][16];
int main()
{
int test_no=1,i,j,row1,row2,test,num,ans;
scanf("%d",&test);
ofstream myfile;
myfile.open ("answer.txt");
while(test_no<=test)
{
num=0;
scanf("%d",&row1);
row1--;
for( i=0;i<4;i++)
{
for( j=0;j<4;j++)
{
scanf("%d",&arr1[i][j]);
}
}
scanf("%d",&row2);
row2--;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
scanf("%d",&arr2[i][j]);
}
}
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if(arr1[row1][i]==arr2[row2][j])
{
num++;
ans = arr1[row1][i];
}
}
}
if(num>1)
{
myfile << "Case #"<<test_no<<": Bad magician!\n";
}
else if(num==1)
{
myfile<<"Case #"<<test_no<<": "<<ans<<"\n";
}
else if(num==0)
{
myfile<<"Case #"<<test_no<<": Volunteer cheated!\n";
}
test_no++;
}
myfile.close();
}
