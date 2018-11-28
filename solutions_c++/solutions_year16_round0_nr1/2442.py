#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<cmath>
#include<queue>
#include<vector>
#define eps 1e-9
#define mod 1000000007
using namespace std;
int t;
long long n;
set<int>s;
void gao()
{

    long long tmp=n,m;
    for(int tm=1;;tm++){
        n=(long long)tm*tmp;
        while(n)
        {
            m=n%10;
            n=n/10;
            s.insert(m);
        }
        if((int)s.size()==10ll)
        {
            cout<<tm*tmp<<endl;return;
        }
    }

}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("a.out","w",stdout);
    cin>>t;
    for(int __=1;__<=t;++__)
    {
        cin>>n;

         cout<<"Case #"<<__<<": ";
         if(n==0){
            cout<<"INSOMNIA\n";continue;
            }
         s.clear();
         gao();

    }

    return 0;
}

// 001011 -4
// 010101 -6
