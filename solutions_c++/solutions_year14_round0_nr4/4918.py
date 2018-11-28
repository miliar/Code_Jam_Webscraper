#include<iostream>
#include<stdio.h>
using namespace std;

int main()
{
int t,n;
int ans[51]={0},ans1[51]={0};
float min,a[1001],b[1001],as[1001],bs[1001];
cin>>t;
for(int k=0;k<t;k++)
{
cin>>n;


for(int i=0;i<n;i++)
scanf("%f",&a[i]);

for(int i=0;i<n;i++)
scanf("%f",&b[i]);
int s;
for(int i=0;i<n;i++)
{
    min=2.0;s=0;
    for(int j=0;j<n;j++)
    {
        if(min>a[j])
        {
            min=a[j];
            s=j;
        }
    }
    as[i]=a[s];
    a[s]=2.0;
}

for(int i=0;i<n;i++)
{
    min=2.0;s=0;
    for(int j=0;j<n;j++)
    {
        if(min>b[j])
        {
            min=b[j];
            s=j;
        }
    }
    bs[i]=b[s];
    b[s]=2.0;
}
/*for(int i=0;i<n;i++)
cout<<as[i]<<" ";
cout<<endl;
for(int i=0;i<n;i++)
cout<<bs[i]<<" ";
cout<<endl;*/
int p=0;
for(int i=0;i<n;i++)
{
    for(int j=p;j<n;j++)
    {
        if(as[i]>bs[j])
        {
         ans[k]++;
         p=j+1;
         break;
        }
    }

}
p=0;
for(int i=0;i<n;i++)
{
    for(int j=p;j<n;j++)
    {
        if(bs[i]>as[j])
        {
         ans1[k]++;
         p=j+1;
         break;
        }
    }

}
ans1[k]=n-ans1[k];

}
for(int k=0;k<t;k++)
{

    cout<<"Case #"<<k+1<<": ";
    printf("%d %d\n",ans[k],ans1[k]);
}
return 0;
}
