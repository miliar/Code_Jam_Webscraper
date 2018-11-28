#include<iostream>
#include<fstream>
using namespace std;

int main()
{
ifstream cin("input1.txt");
ofstream cout("output1.txt");
int t;
int b[4][4];
int g1,g2,ans,num,i,j;
cin>>t;
int d=1;
while(d<=t)
{
int a[16]={0};
cin>>g1;
for(i=0;i<4;i++)
{
    for(j=0;j<4;j++)
    {
        cin>>b[i][j];
        if(i==g1-1)
            a[b[i][j]-1]++;
    }
}
cin>>g2;
for(i=0;i<4;i++)
{
    for(j=0;j<4;j++)
    {
        cin>>b[i][j];
        if(i==g2-1)
            a[b[i][j]-1]++;
    }
}
ans=0;
for(i=0;i<16;i++)
{
    if(a[i]==2)
    {
        ans++;
        num=i+1;
    }
}

if(ans==1)
cout<<"Case #"<<d<<": "<<num<<endl;
else if(ans>1)
cout<<"Case #"<<d<<": "<<"Bad magician!"<<endl;
else
cout<<"Case #"<<d<<": "<<"Volunteer cheated!"<<endl;

d++;
}
}
