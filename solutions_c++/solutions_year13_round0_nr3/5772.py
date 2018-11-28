#include <fstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
ifstream cin("/Users/yangsiyu/Documents/HelloWorld/HelloWorld/in.txt");
ofstream cout("/Users/yangsiyu/Documents/HelloWorld/HelloWorld/out.txt");

bool check(long long a)
{
    long long b,tmp;
    b=0; tmp=a;
    while (tmp>0)
    {
        b=b*10+(tmp%10);
        tmp/=10;
    }
    if (a==b) return true;
    return false;
}

int main()
{
    long long t,a,b,i,x,y,ans,count=0;
    cin>>t;
    while (t--)
    {
        count++;
        ans=0;
        cin>>a>>b;
        x=(int)sqrt(double(a));
        y=(int)sqrt(double(b))+1;
        for (i=x;i<=y;i++)
            if (check(i))
                if (i*i>=a&&i*i<=b&&check(i*i))
                {
                    ans++;
                }
        cout<<"Case #"<<count<<": "<<ans<<endl;
    }
    return 0;
}