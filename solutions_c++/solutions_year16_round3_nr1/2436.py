#include <bits/stdc++.h>
using namespace std;
int main(int argc, char const *argv[]) {
    int test,ti;
    int n,i,j,k;
    char ch='A';
    std::vector<pair<int,char> > v;
    cin>>test;
    ti=0;
    while(test--)
    {
        ti+=1;
        ch='A';
        cin>>n;
        for(i=0;i<n;i++)
        {
            cin>>j;
            v.push_back(make_pair(j,ch));
            ch++;
        }
        cout<<"Case #"<<ti<<": ";
        while(1)
        {
            // cout<<"sasa";
            sort(v.begin(),v.end(),greater<pair<int,char> >());
            // for(i=0;i<n;i++)
            //     cout<<v[i].first<<" "<<v[i].second<<endl;
            if(v[0].first<=0)
                break;
            // cout<<v[0].first<<" "<<v[1].first;
            if(v[0].first!=v[1].first)
            {
                if(v[1].first==v[2].first)
                {
                    cout<<v[0].second<<v[0].second<<" ";
                    v[0].first-=2;
                }
                else
                {
                    cout<<v[0].second<<" ";
                    v[0].first--;
                }
            }
            if(v[0].first==v[1].first && v[0].first!=1)
            {
                if(v[1].first==v[2].first)
                {
                    cout<<v[0].second<<" ";
                    v[0].first--;
                }
                else
                {
                    cout<<v[0].second<<v[1].second<<" ";
                    v[0].first-=1;
                    v[1].first-=1;
                }
            }
            if(v[0].first==v[1].first && v[0].first==1)
            {
                if(v[2].first==1)
                {
                    cout<<v[0].second<<" ";
                    v[0].first--;
                }
                else
                {
                    cout<<v[0].second<<v[1].second<<" ";
                    v[0].first-=1;
                    v[1].first-=1;
                }
            }
            // break;
        }
        cout<<endl;

    }
    return 0;
}
