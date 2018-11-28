#include<cstdio>
#include<iostream>
#include<cstdlib>
#include<cstring>
using namespace std;
int main(){
freopen("sr.in","r",stdin);
freopen("sr.out","w",stdout);
int t,k,c,s,i=1,j;

cin>>t;
while(i<=t)
{

    cin>>k>>c>>s;
    cout<<"Case #"<<i<<": ";
    for(j=1;j<=k;j++)
    cout<<j<<" ";
    cout<<endl;
i++;
}
return 0;
}
