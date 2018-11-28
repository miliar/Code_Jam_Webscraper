#include <iostream>
#include <cstring>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <algorithm>
#define ll long long
#define eps 1e-9
using namespace std;

vector<double>N;
vector<double>K;
bool bi[1005];

int main()
{
    freopen("0.in","r",stdin);
    freopen("0.out","w",stdout);

    int a,b,c,d,e,t,n,z;
    double x,y,C,F,Z,X;

    cin>>t;

    for(int i=1;i<=t;i++)
    {
        cin>>n;
        N.clear();
        K.clear();
        for(a=0;a<n;a++)
        {
            cin>>x;
            x=x+eps;
            N.push_back(x);
        }
        for(a=0;a<n;a++)
        {
            cin>>x;
            x=x+eps;
            K.push_back(x);
            bi[a]=0;
        }
        sort(N.begin(),N.end());
        sort(K.begin(),K.end());
        e=0;
        //for(a=0;a<n;a++) cout<<N[a]<<" "; cout<<endl;
        //for(a=0;a<n;a++) cout<<K[a]<<" "; cout<<endl;
        z=0;
        for(a=0;a<n;a++)
        {
            for(b=0;b<n;b++)
            {
                if(!bi[b])
                {
                    if(N[a]>K[b])
                    {
                        e++;
                        bi[b]=1;
                        //cout<<"took "<<K[b]<<" by "<<N[a]<<endl;
                    }
                    else
                    {
                        for(c=n-1;c>=0;c--)
                        {
                            if(!bi[c])
                            {
                                bi[c]=1;
                                //cout<<"blocked "<<K[c]<<" by "<<N[a]<<endl;
                                break;
                            }
                        }
                    }
                    break;
                }
            }
        }
        for(a=0;a<n;a++) bi[a]=0;

        d=0;
        //cout<<endl;
        for(a=0;a<n;a++)
        {
            for(b=0;b<n;b++)
            {
                if(bi[b]) continue;
                if(K[b]>N[a])
                {
                    //cout<<N[a]<<" taken by "<<K[b]<<endl;
                    bi[b]=1;
                    break;
                }
            }
            if(b==n)
            {
                for(b=0;b<n;b++)
                {
                    if(bi[b]) continue;
                    bi[b]=1;
                    //cout<<N[a]<<" takes "<<K[b]<<endl;
                    d++;
                    break;
                }
            }
        }

        cout<<"Case #"<<i<<": "<<e<<" "<<d<<endl;
    }

    return 0;
}
