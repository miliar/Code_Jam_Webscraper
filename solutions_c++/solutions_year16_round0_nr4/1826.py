#include<bits/stdc++.h>
using namespace std;
vector<int> v;
int main()
{
    int k,c,s,t;
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    cin>>t;
    for(int i=1;i<=t;i++)
    {
        cin>>k>>c>>s;
        int cnt=0,i1=1;
        while(cnt<k)
        {
            //cout<<cnt<<" "<<
            v.push_back(i1);
            cnt++;
            i1+=k;
            if(c==1)
                break;
        }
        if(c==1)
        {
            for(int i=2;i<=k;i++)
                v.push_back(i);
        }
        printf("Case #%d: ",i);
        for(int k1=0;k1<v.size();k1++)
        {
            cout<<v[k1]<<" ";
        }
        cout<<endl;
        v.clear();
    }
    return 0;
}
