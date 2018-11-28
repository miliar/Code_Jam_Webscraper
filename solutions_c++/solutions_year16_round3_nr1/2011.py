#include <bits/stdc++.h>

using namespace std;


typedef long long ll;

vector<pair<int,int> >v;

int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);

    int t,n;
    cin>>t;
    int i=1,x,sum;
    char c;
    while(i<=t)    {
        scanf("%d",&n);
        sum=0;
        for(int j=0;j<n;j++)    {
            scanf("%d",&x);
            v.push_back(make_pair(x,j));
            sum+=x;
        }
        printf("Case #%d: ",i);
        while(1)    {
            sort(v.begin(),v.end());
            reverse(v.begin(),v.end());
            if(v[0].first>=2+v[1].first)    {
                v[0].first-=2;
                sum-=2;
                c=v[0].second+'A';
                cout<<c<<c<<" ";
                if(!sum)    {
                    cout<<endl;
                    break;
                }
            }
            else if(v[0].first==1+v[1].first)    {

                v[0].first-=1;
                sum-=1;
                c=v[0].second+'A';
                cout<<c<<" ";
                if(!sum)    {
                    cout<<endl;
                    break;
                }
            }
            else    {
                if(2*v[1].first<=sum-1)    {

                    v[0].first-=1;
                    sum-=1;
                    c=v[0].second+'A';
                    cout<<c<<" ";
                    if(!sum)    {
                        cout<<endl;
                        break;
                    }
                }
                else    {

                    v[0].first-=1;
                    v[1].first-=1;
                    sum-=2;
                    c=v[0].second+'A';
                    cout<<c;
                    c=v[1].second+'A';
                    cout<<c<<" ";
                    if(!sum)    {
                        cout<<endl;
                        break;
                    }
                }
            }
        }
        v.clear();
        i++;
    }


    return 0;
}
