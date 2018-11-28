#include<vector>
#include<iostream>
#include<stdio.h>
#include<bitset>
#include<algorithm>
#include<functional>
#include<numeric>
#include<utility>
#include<sstream>
#include<iostream>
#include<iomanip>
#include<cstdio>
#include<cmath>
#include<math.h>
#include<cstdlib>
#include<ctime>
#include<cstring>
#include<climits>
#include<sstream>
#include<string.h>
#include<set>
#include<map>
#include<utility>
#include<stack>
#include<queue>
#include<deque>
#include<list>
#include<bitset>

#define llu unsigned long long int
#define lli long long
#define mp make_pair
#define pb push_back
#define F first
#define S second

const double eps = 1e-5;
const double PI = 3.14159265359;
int INF = 2147483645;

template <class T>T Max2(T a,T b){return a<b?b:a;}
template <class T>T Min2(T a,T b){return a<b?a:b;}
template <class T>T Max3(T a,T b,T c){return Max2(Max2(a,b),c);}
template <class T>T Min3(T a,T b,T c){return Min2(Min2(a,b),c);}
template <class T>T Max4(T a,T b,T c,T d){return Max2(Max2(a,b),Max2(c,d));}
template <class T>T Min4(T a,T b,T c,T d){return Min2(Min2(a,b),Max2(c,d));}

using namespace std;

int a[10];
int main()
{
    std::ios::sync_with_stdio(false);
    cin.tie(0);

    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);

    int t;
    cin>>t;

    for(int k=1;k<=t;k++)
    {
        for(int i=0;i<10;i++)
            a[i] = 0;
        lli n,last;
        cin>>n;

        bool yes = false;
        for(int i=1;i<=100000;i++)
        {
            bool done = true;
            lli temp = i*n;

            while(temp)
            {
                a[temp%10] = 1;
                temp/=10;
            }

            for(int j=0;j<10;j++)
            {
                if(a[j] == 0)
                    done = false;
            }

            if(done)
            {
                yes = true;
                last = i*n;
                break;
            }
        }

        if(yes)
        {
            cout<<"Case #"<<k<<": "<<last<<endl;
        }
        else
        {
            cout<<"Case #"<<k<<": INSOMNIA"<<endl;
        }
    }
    return 0;
}
