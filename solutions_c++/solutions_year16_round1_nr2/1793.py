#include<bits/stdc++.h>
using namespace std;
vector<int> v;
int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int t,n,a;
    cin>>t;
    for(int i1=1;i1<=t;i1++)
    {
        cin>>n;
        int freq[3000];
        memset(freq,0,sizeof(freq));
        for(int i=1;i<=2*n-1;i++)
        {
            for(int j=1;j<=n;j++)
            {
                cin>>a;
                freq[a]+=1;
            }
        }
        for(int i=1;i<=2500;i++)
        {
            if(freq[i]&&freq[i]%2)
            {
                v.push_back(i);
            }
        }
        cout<<"Case #"<<i1<<":"<<" ";
        for(int i=0;i<v.size();i++)
            cout<<v[i]<<" ";
        cout<<endl;
        v.clear();
    }
}
