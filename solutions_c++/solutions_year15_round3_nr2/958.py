/*Krypto...........................jagsxi..........!!! */
/*Google Code Jam Round1C */
#include<bits/stdc++.h>
using namespace std;
template<class T> T pwr(T b, T p){T r=1,x=b;while(p){if(p&1)r*=x;x*=x;p=(p>>1);}return r;}
#define     inf             (0x7f7f7f7f)
int K,TL,SL;
string keys;
string tword;

pair<int,int> sol(int idx,string s)
{
    if(idx==SL)
    {
        int ans = 0;
for(int i=0;i<=SL-TL;++i)
        {
            if(!s.compare(i,TL,tword))ans++;
        }
        return make_pair(ans,ans);
    }
    pair<int,int> ans = make_pair(0,-inf);
for(int i=0;i<=K-1;++i)
    {
        pair<int,int> tmp = sol(idx+1,s+keys[i]);
        ans.second = max(ans.second,tmp.second);
        ans.first += tmp.first;
    }
    return ans;
}

int main()
{

 freopen("2.txt", "r", stdin);
  freopen("2o.txt", "w", stdout);
    int T,t=1;
    cin>>T;
    while(T--)
    {
        cin>>K>>TL>>SL;
        cin>>keys;
        cin>>tword;
        pair<int,int> ans = sol(0,"");
        double ok = (double)ans.second-double(ans.first)/double(pwr(K,SL));
        cout<<"Case #"<<t++<<": "<<setprecision(8)<<ok<<endl;
    }
    return 0;
}
