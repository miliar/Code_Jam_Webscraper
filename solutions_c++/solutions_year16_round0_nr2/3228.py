#include<bits/stdc++.h>
using namespace std;
#define gc getchar
#define ll long long
#define v vector
#define pr pair<int,int>
#define sd second
#define ft first
#define pb push_back
#define mp make_pair
int main()
{
//    freopen("B-large.in","r",stdin);
//    freopen("output.txt","w",stdout);
    ios::sync_with_stdio(false);
    int i,j,k,t,n,flag,x,ans;
    cin>>t;
    for(k=1;k<=t;k++)
    {
        string pan;
        cin>>pan;
        n=pan.length();
        v<int> fin;
        if(pan[0]=='-')
            fin.pb(-1);
        else
            fin.pb(1);
        for(i=1;i<n;i++)
        {
            if(pan[i]=='-')
            {
                if(pan[i]==pan[i-1])
                    fin[fin.size()-1]--;
                else
                    fin.pb(-1);
            }
            else
            {
                if(pan[i]==pan[i-1])
                    fin[fin.size()-1]++;
                else
                    fin.pb(1);
            }
        }
        ans=fin.size();
        if(fin[fin.size()-1]>0)
            ans--;
        cout<<"Case #"<<k<<": "<<ans<<endl;
        fin.clear();
    }
    return 0;
}
