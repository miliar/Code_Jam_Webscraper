#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<string>
#include<vector>
#include<map>
using namespace std;
int main()
{
freopen("in1.txt","r",stdin);
freopen("out1.txt","w",stdout);

int t,test,a,b,k,i,j,m,ans;

cin>>t;
for(test=1;test<=t;test++)
{
    ans=0;
cin>>a>>b>>k;

for(i=0;i<a;i++)
{
    for(j=0;j<b;j++)
    {
        m=i&j;
        if(m<k)
         ans++;
    }
}

cout<<"Case #"<<test<<": "<<ans<<endl;


}
return 0;
}

