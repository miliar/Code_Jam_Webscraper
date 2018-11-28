#include<iostream>
#include<fstream>
#include<stdlib.h>
#include<limits.h>
#include<math.h>
#include<cstdio>
#include<vector>
#include<string>
#include<cstring>
#include<queue>
#include<map>
#include<set>
#include<algorithm>
#include<iomanip>
#include<bitset>
#define max3(a,b,c) a>=b?(a>=c?a:c):(b>=c?b:c)
using namespace std;
int t,sm,x,ans,pre,i;
string str;
int main() {
freopen("ttt.txt","r", stdin);
scanf("%d",&t);
x=1;
while(t--)
{
cin>>sm>>str;
ans=0;
pre=(str[0]-'0');
for(i=1;i<=sm;i++)
{
if(pre<i && (str[i]-'0'>0))
{
ans+=(i-pre);
pre+=(ans);
}
pre+=(str[i]-'0');
}
cout<<"Case #"<<x<<": "<<ans<<"\n";
x++;
}
 return 0;
}

