#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;

int main()
{
ifstream cin("input3.txt");
ofstream cout("output3.txt");
int t;
cin>>t;
int d=1;
int n,i,j,c1,c2;
while(d<=t)
{
c1=0,c2=0;
double a[1000]={0},b[1000]={0};
cin>>n;
for(i=0;i<n;i++)
    cin>>a[i];
for(i=0;i<n;i++)
    cin>>b[i];
sort(a,a+n);
sort(b,b+n);
i=0;j=0;
while((i<n)&&(j<n))
{
    if(a[i]>=b[j])
    {
        j++;
    }
    else if(a[i]<b[j])
    {
        i++; j++;
    }
    c1=n-i;
}
i=0;j=0;
while((i<n)&&(j<n))
{
    if(b[i]>=a[j])
    {
        j++;
    }
    else if(b[i]<a[j])
    {
        i++; j++;
    }
    c2=i;
}

cout<<"Case #"<<d<<": "<<c2<<" "<<c1<<endl;
d++;
}
}
