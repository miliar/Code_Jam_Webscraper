#include <bits/stdc++.h>
using namespace std;
#define L long long
int a[65600];
vector<int> p;
void init()
{
    int n=65536;
    for(int i=0;i<n;i++)
        a[i]=i+2;
    for(int i=0;i<n;i++)
    {
        if(a[i]!=-1)
        {
            p.push_back(a[i]);
            for(int j=2*a[i]-2;j<n;j+=a[i])
                a[j]=-1;
        }
    }
}
int main()
{
    init();
    L t;
    cin>>t;
    for(int I=1;I<=t;I++)
    {
        L n,k;
        cin>>n>>k;
        cout<<"Case #"<<I<<":\n";
        L N=1;
        for(int i=1;i<=n;i++)
            N=N*2;
        for(L i=N/2+1;i<=N && k;i+=2)
        {
            vector<int> s;
            for(int b=2;b<=10;b++)
            {
                L x=0,m=1;
                for(int j=0;j<n;j++)
                {
                    if(i&(1<<j))
                    {
                        x=x+m;
                    }
                    m*=b;
                }
                if(x<65536 && x>1 && a[x-2]!=-1)
                {
                    break;
                }
                else
                {
                    for(int j=0;j<p.size() && p[j]*p[j]<=x;j++)
                    {
                        if(x%p[j]==0)
                        {
                            s.push_back(p[j]);
                            break;
                        }
                    }
                }
            }
            if(s.size()==9)
            {
                k--;
                vector<int> s1;
                for(int j=0;j<n;j++)
                {
                    if(i&(1<<j))
                        s1.push_back(1);
                    else
                        s1.push_back(0);
                }
                for(int j=n-1;j>=0;j--)
                    cout<<s1[j];
                cout<<" ";
                for(int j=0;j<9;j++)
                    cout<<s[j]<<" ";
                cout<<endl;
            }
        }
    }
    return 0;
}
