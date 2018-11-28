#include <vector>
#include <set>
#include <cmath>
#include <cstdio>

#include <iostream>
#include <iomanip>
#include <climits>
#include <algorithm>
#include <cstring>
#include <bitset>
#define rep(i,a,b) for(int (i) = (a); (i) < (b); (i)++)
#define s(x) scanf("%d",&x)
#define ss(x,y) scanf("%d%d",&x,&y)
#define ssll(x,y) scanf("%lld%lld",&x,&y)
#define ssl(x) scanf("%lld",&x)
#define p(x) printf("%d\n",x)
#define pl(x) printf("%lld\n",x)
#define lli long long int
using namespace std;



int main()
{

long long int t,n,ncopy;
scanf("%lld",&t);
int  mark[11];
int markcnt=0;
int test=0;
while(test!=t)
{
markcnt=0;
for(int i=0;i<=10;i++)
{
mark[i]=0;
}

scanf("%lld",&n);
if(n==0)
{
cout<<"Case #"<<test+1<<": "<<"INSOMNIA\n";
test++;
continue;
}

int g=1;
ncopy=n;
while(markcnt!=10)
{
long long int s=ncopy;
//cout<<n<<endl;
//cout<<s;
while(s!=0)
{
int digit=s%10;
if(mark[digit]==0)

{
mark[digit]=1;
markcnt++;

}

s=s/10;
}
g++;
ncopy=n*g;
}
g--;
cout<<"Case #"<<test+1<<": "<<n*g<<endl;
test++;
}


return 1;


}