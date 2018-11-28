#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("OP1B.txt","w",stdout);
    int T,M=0;
    string str;
    cin>>T;
    while(T--)
    {
        long long C=0,S=0;
        int N;
        cin>>N>>str;
        vector<pair<int,int> >V;
        for(int i=0;i<(int)str.size();i++)
            V.push_back(make_pair(i,str[i]-'0'));
        C+=V[0].second;
        for(int i=1;i<(int)V.size();i++)
        {
            if(C<V[i].first)
            {
                S+=(V[i].first-C);
                C+=(V[i].first-C);
            }
            C+=V[i].second;
        }
        cout<<"Case #"<<++M<<": "<<S<<endl;
    }
}
