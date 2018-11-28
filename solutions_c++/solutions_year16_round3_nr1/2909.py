#include<bits/stdc++.h>
using namespace std;
#define mp make_pair
#define pb push_back
#define F first
#define S second
#define ll long long
using namespace std;
ll n,x;
vector<pair<int,char> >v;
int main(){
    ios_base::sync_with_stdio(0),cin.tie(0),cout.tie(0);
    freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	cin>>n;
	int t,k=1;

	while(n--)
    {
        char c='A';
        cin>>t;
        for(int i=0 ; i<t ; i++)
        {
            cin>>x;
            v.pb(mp(x,c));
            c++;
        }
        cout<<"Case #"<<k++<<": ";
        while(1)
        {
            //cout<<"ddddddd"<<endl;
            sort(v.rbegin(),v.rend());
            if(v[0].F==0)   break;
            if(v[0].F==v[1].F)
            {
                if(v[1].F==1)
                {
                    if(v.size()>2)
                    {
                        if(v[2].F==1)
                        {
                           cout<<v[0].S<<" "<<v[1].S<<v[2].S;
                           v[0].F--;
                           v[1].F--;
                           v[2].F--;
                        }
                        else
                        {
                            cout<<v[0].S<<v[1].S;
                            v[0].F--;
                            v[1].F--;
                        }
                    }
                    else
                    {
                        cout<<v[0].S<<v[1].S<<" ";
                        v[0].F--;
                        v[1].F--;
                    }
                }
                else
                {
                    cout<<v[0].S<<v[1].S<<" ";
                    v[0].F--;
                    v[1].F--;
                }
            }
            else if(v[0].F>v[1].F)
            {
                cout<<v[0].S<<" ";
                v[0].F--;
            }

        }
        v.clear();
        cout<<endl;
    }
}
