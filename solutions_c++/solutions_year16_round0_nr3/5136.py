#include <iostream>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <cstdio>

#define pairr pair<int, int>
#define s second
#define f first
#define pb push_back

using namespace std;

int n,m,t,i,j,r,k;
long long a;
char s[40];
vector<int> v;

int main()
{
    //freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t>>n>>m;
    cout<<"Case #1:\n";
    for (i=0;i<n;i++) s[i]='0';
    s[0]='1';
    s[n-1]='1';
    while (r<m)
    {
        a=strtoll(s,NULL,2);
        k=0;
        for (i=2;i<=sqrt(a);i++)
        {
            if (a%i==0)
            {
                k=1;
                v.pb(i);
                break;
            }
        }
        if (k==1)
        {
            k=0;
            a=strtoll(s,NULL,3);
            for (i=2;i<=sqrt(a);i++)
            {
                if (a%i==0)
                {
                    k=1;
                    v.pb(i);
                    break;
                }
            }
        }
        if (k==1)
        {
            k=0;
            a=strtoll(s,NULL,4);
            for (i=2;i<=sqrt(a);i++)
            {
                if (a%i==0)
                {
                    k=1;
                    v.pb(i);
                    break;
                }
            }
        }
        if (k==1)
        {
            k=0;
            a=strtoll(s,NULL,5);
            for (i=2;i<=sqrt(a);i++)
            {
                if (a%i==0)
                {
                    k=1;
                    v.pb(i);
                    break;
                }
            }
        }
        if (k==1)
        {
            k=0;
            a=strtoll(s,NULL,6);
            for (i=2;i<=sqrt(a);i++)
            {
                if (a%i==0)
                {
                    k=1;
                    v.pb(i);
                    break;
                }
            }
        }
        if (k==1)
        {
            k=0;
            a=strtoll(s,NULL,7);
            for (i=2;i<=sqrt(a);i++)
            {
                if (a%i==0)
                {
                    k=1;
                    v.pb(i);
                    break;
                }
            }
        }
        if (k==1)
        {
            k=0;
            a=strtoll(s,NULL,8);
            for (i=2;i<=sqrt(a);i++)
            {
                if (a%i==0)
                {
                    k=1;
                    v.pb(i);
                    break;
                }
            }
        }
        if (k==1)
        {
            k=0;
            a=strtoll(s,NULL,9);
            for (i=2;i<=sqrt(a);i++)
            {
                if (a%i==0)
                {
                    k=1;
                    v.pb(i);
                    break;
                }
            }
        }
        if (k==1)
        {
            k=0;
            a=strtoll(s,NULL,10);
            for (i=2;i<=sqrt(a);i++)
            {
                if (a%i==0)
                {
                    k=1;
                    v.pb(i);
                    break;
                }
            }
        }
        if (k==1)
        {
            r++;
            for (i=0;i<n;i++) cout<<s[i];
            for (i=0;i<v.size();i++) cout<<" "<<v[i];
            cout<<endl;
        }
        v.clear();

        for (i=n-1;i>=0;i--)
        {
            if (s[i]=='0')
            {
                s[i]='1';
                i++;
                for (;i<n-1;i++)
                {
                    s[i]='0';
                }
                break;
            }
        }
    }
    return 0;
}
