#include<bits/stdc++.h>
using namespace std;
bool comp(pair<int,int> a,pair<int,int> b)
{
    return a.first > b.first;
}
int main()
{
    int n,x,t,count=0;
    cin>>t;
    for(int i=0;i<t;i++)
    {
        cout<<"Case #"<<i+1<<": ";
            cin>>n;
            vector<pair<int,int> > a;
            for(int i=0;i<n;i++)
            {
                cin>>x;
                a.push_back(make_pair(x,i));
                count+=x;
            }
            sort(a.begin(),a.end(),comp);
           
            while(count!= 0)
            {
                //cout<<count;
                a[0].first--;
                if(a[0].first >=0)
                {
                    cout<<char(a[0].second+'A');
                    count--;
                }
                if(count==2)
                {
                    cout<<" ";
                    sort(a.begin(),a.end(),comp);
                    continue;
                }
                a[1].first--;
                if(a[1].first >=0)
                {
                    cout<<char(a[1].second+'A');
                    count--;
                }
                cout<<" ";
               /* for(int i=0;i<n;i++)
            {
                cout<<a[i].first;
            }*/
                sort(a.begin(),a.end(),comp);
            }
            cout<<endl;
            }
}
