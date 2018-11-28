#include<iostream>
#include<stdio.h>
using namespace std;
void magician(int a[][4],int b[][4],int r1,int r2,int t)
{
int count =0;
int result;
for (int i=0;i<4;i++)
for (int j=0;j<4;j++)
{
 if (a[r1-1][i] == b[r2-1][j])
 {
 count++;
 result = a[r1-1][i];
 }
}
 if (count == 1)
 cout<<"Case #"<<t<<": "<<result<<endl;
 else if(count >1)
 cout <<"Case #"<<t<<": "<<"Bad magician!"<<endl;
 else if (count == 0)
 cout <<"Case #"<<t<<": "<<"Volunteer cheated!"<<endl;
}
int main()
{
int t,r1,r2;
scanf("%d",&t);
int m[4][4],n[4][4];
for (int x=0;x<t;x++)
{
    scanf("%d",&r1);
    for (int i=0;i<4;i++)
        for (int j=0;j<4;j++)
        scanf("%d",&m[i][j]);
    scanf("%d",&r2);
   for (int i=0;i<4;i++)
        for (int j=0;j<4;j++)
        scanf("%d",&n[i][j]);
    magician(m,n,r1,r2,x+1);
}
return 0;
}
