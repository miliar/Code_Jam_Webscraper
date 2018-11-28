#include<iostream>
#include<fstream>
#include<string>
#include<algorithm>
#include<cmath>
#include<string.h>
#include<ctime>
#include<set>
#include<vector>
#include<stack>
#include<queue>
#include <cstdio>
//#define F first
//#define S second
//#define mp make_pair
#define inf 1000*1000*1000
#define mod 1000000007
double delta=0.0000001;
using namespace std;
double t, x, p;
int a[1009], b[1009], ind, u[1009], n;
set<double> s, s2;
int main()
{
    ifstream cin("D-large.in");
    ofstream cout("D-large.out");
    cin>>t;
    while(t--)
    {
        ind++;
        cin>>n;
        for(int i = 1;i <= n; i++)
        {
            cin>>x;
            a[i] = x * 100000;
            s.insert(x);
        }
        for(int i = 1;i <= n; i++)
        {
            cin>>x;
            b[i] = x * 100000;
            s2.insert(x);
        }
        cout<<"Case #"<<ind<<": ";
        p = 0;
        for(int i=1;i<=n;i++)
        {
            set<double> :: iterator it = s.begin();
            double q = *it;
            set<double> :: iterator it2 = s2.begin();
            double w = *it2;
            //cout<<q<<" "<<w<<endl;
            if(q < w)
            {
                set<double> :: iterator it3 = s2.end();
                it3--;
                double xx = *it3;
                s2.erase(xx);
                s.erase(q);
            }
            else
            {
                p ++;
                s.erase(q);
                s2.erase(w);
            }
        }
        cout<<p<<" ";
        p = 0;
        sort(a+1, a+n+1);
        sort(b+1, b+n+1);
        for(int i=1;i<=n;i++)
        {
            int xx = a[i];
            int p2 = 0;
            for(int j=1;j<=n;j++)
            {
                if(!u[j] && b[j] > xx)
                {
                    u[j] = 1;
                    p2 = 1;
                    break;
                }
            }
            if(!p2)
            {
                p++;
                for(int j=1;j<=n;j++)
                {
                    if(!u[j])
                    {
                        u[j] = 1;
                        break;
                    }
                }
            }
        }
        for(int j=1;j<=n;j++)
            u[j] = 0;
        cout<<p<<endl;
    }
}
