//program A

#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<vector>
#include<cmath>
#include<set>
using namespace std;

void print(int i){cout << i << " ";}
template<class T>void print(vector<T> v){for(int i=0;i<v.size();++i)print(v[i]);cout << endl;}

typedef unsigned long long int num;

num gcd(num a,num b)
{
    while(a)
    {
        int c=a;
        a=b%a;
        b=c;
    }
    return b;
}

int main()
{
    freopen("A.in","r",stdin);
    //freopen("A.out","w",stdout);
    int totaltest;
    cin >> totaltest;
    for(int test=1;test<=totaltest;test++)
    {
        printf("Case #%d: ",test);
        
        num p,q;
        scanf("%lld/%lld",&p,&q);
        num d=gcd(p,q);
        p/=d;q/=d;
        if(q&(q-1))
            cout << "impossible" << endl;
        else
        {
            num pot=1;while(pot<=p)pot*=2;pot/=2;
            int res=0;
            while(pot<q)
            {
                pot*=2;
                res++;
            }
            cout << res << endl;
        }
    }
    return 0;
}
