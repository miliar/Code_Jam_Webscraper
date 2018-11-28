#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
freopen("A-small-attempt1.in","r",stdin);
freopen("outfile.txt","w",stdout);
int t,a[4][4],b[4][4];
cin>>t;
for(int c=1;c<=t;c++)
{
 int ans1,ans2,temp[4];
 cin>>ans1;
 int k=0;
 for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        {cin>>a[i][j];
        if(i==ans1-1)
        temp[k++]=a[i][j];

        }
 cin>>ans2;
for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        cin>>b[i][j];
        int a,flag=0;
for(int i=0;i<4;i++)
    for(int j=0;j<4;j++)
{
    if(temp[i]==b[ans2-1][j])
        {flag++;
        a=temp[i];
        }
}
if(flag==1)
    cout<<"Case #"<<c<<": "<<a<<endl;
    else if(flag==0)
    cout<<"Case #"<<c<<": Volunteer cheated!"<<endl;
    else
        cout<<"Case #"<<c<<": Bad magician!"<<endl;
}
return 0;
}
