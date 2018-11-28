#include<bits/stdc++.h>
using namespace std;
const int maxn=1e2+7;
int out[maxn];
int MaxS,T;
int main()
{
    ios_base::sync_with_stdio(false);
    cin>>T;
    for(int i=1;i<=T;i++)
    {
        cin >> MaxS;
        string tmp;
        cin >>tmp;
        int counter=0;
        for(int j=0;j<tmp.size();j++)
        {
            int osoby=tmp[j]-'0';
            if(counter<j)
            {
                out[i]+=j-counter;
                counter=j;
            }
            counter+=osoby;
        }
        cout<<"Case #"<<i<<": "<<out[i]<<"\n";
    }
    
    return 0;
}
