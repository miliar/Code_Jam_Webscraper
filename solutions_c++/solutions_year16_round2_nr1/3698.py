#include<iostream>
#include<cstdio>
#include<string>
#include<vector>
#include<cstring>
using namespace std;
int t,br[32],p;
string s;
bool l;
vector<int> ans;
bool prov()
{
    /**for(int i=0;i<26;++i)
    {
        if(br[i])
        {
            char c=i+'A';
            cout<<c<<" - "<<br[i]<<"\n";
        }
    }
    cout<<"\n";**/
    for(int i=0;i<26;++i)
        if(br[i])return 0;
    return 1;
}
void solve()
{
    if(prov())
    {
        cout<<"Case #"<<p<<": ";
        int sz=ans.size();
        for(int i=0;i<sz;++i)cout<<ans[i];
        cout<<"\n";
        l=1;
    }
    for(int i=0;i<10;++i)
    {
        if(i==0&&br['Z'-'A']&&br['E'-'A']&&br['R'-'A']&&br['O'-'A'])
        {
            --br['Z'-'A'];
            --br['E'-'A'];
            --br['R'-'A'];
            --br['O'-'A'];
            ans.push_back(0);
            solve();
            if(l==1)return;
            ++br['Z'-'A'];
            ++br['E'-'A'];
            ++br['R'-'A'];
            ++br['O'-'A'];
            ans.pop_back();
        }
        else if(i==1&&br['O'-'A']&&br['N'-'A']&&br['E'-'A'])
        {
            --br['O'-'A'];
            --br['N'-'A'];
            --br['E'-'A'];
            ans.push_back(1);
            solve();
            if(l==1)return;
            ++br['O'-'A'];
            ++br['N'-'A'];
            ++br['E'-'A'];
            ans.pop_back();
        }
        else if(i==2&&br['T'-'A']&&br['W'-'A']&&br['O'-'A'])
        {
            --br['T'-'A'];
            --br['W'-'A'];
            --br['O'-'A'];
            ans.push_back(2);
            solve();
            if(l==1)return;
            ++br['T'-'A'];
            ++br['W'-'A'];
            ++br['O'-'A'];
            ans.pop_back();
        }
        else if(i==3&&br['T'-'A']&&br['H'-'A']&&br['R'-'A']&&br['E'-'A']>=2)
        {
            --br['T'-'A'];
            --br['H'-'A'];
            --br['R'-'A'];
            br['E'-'A']-=2;
            ans.push_back(3);
            solve();
            if(l==1)return;
            ++br['T'-'A'];
            ++br['H'-'A'];
            ++br['R'-'A'];
            br['E'-'A']+=2;
            ans.pop_back();
        }
        else if(i==4&&br['F'-'A']&&br['O'-'A']&&br['U'-'A']&&br['R'-'A'])
        {
            --br['F'-'A'];
            --br['O'-'A'];
            --br['U'-'A'];
            --br['R'-'A'];
            ans.push_back(4);
            solve();
            if(l==1)return;
            ++br['F'-'A'];
            ++br['O'-'A'];
            ++br['U'-'A'];
            ++br['R'-'A'];
            ans.pop_back();
        }
        else if(i==5&&br['F'-'A']&&br['I'-'A']&&br['V'-'A']&&br['E'-'A'])
        {
            --br['F'-'A'];
            --br['I'-'A'];
            --br['V'-'A'];
            --br['E'-'A'];
            ans.push_back(5);
            solve();
            if(l==1)return;
            ++br['F'-'A'];
            ++br['I'-'A'];
            ++br['V'-'A'];
            ++br['E'-'A'];
            ans.pop_back();
        }
        else if(i==6&&br['S'-'A']&&br['I'-'A']&&br['X'-'A'])
        {
            --br['S'-'A'];
            --br['I'-'A'];
            --br['X'-'A'];
            ans.push_back(6);
            solve();
            if(l==1)return;
            ++br['S'-'A'];
            ++br['I'-'A'];
            ++br['X'-'A'];
            ans.pop_back();
        }
        else if(i==7&&br['S'-'A']&&br['E'-'A']>=2&&br['V'-'A']&&br['N'-'A'])
        {
            --br['S'-'A'];
            br['E'-'A']-=2;
            --br['V'-'A'];
            --br['N'-'A'];
            ans.push_back(7);
            solve();
            if(l==1)return;
            ++br['S'-'A'];
            br['E'-'A']+=2;
            ++br['V'-'A'];
            ++br['N'-'A'];
            ans.pop_back();
        }
        else if(i==8&&br['E'-'A']&&br['I'-'A']&&br['G'-'A']&&br['H'-'A']&&br['T'-'A'])
        {
            --br['E'-'A'];
            --br['I'-'A'];
            --br['G'-'A'];
            --br['H'-'A'];
            --br['T'-'A'];
            ans.push_back(8);
            solve();
            if(l==1)return;
            ++br['E'-'A'];
            ++br['I'-'A'];
            ++br['G'-'A'];
            ++br['H'-'A'];
            ++br['T'-'A'];
            ans.pop_back();
        }
        else if(i==9&&br['N'-'A']>=2&&br['I'-'A']&&br['E'-'A'])
        {
            br['N'-'A']-=2;
            --br['I'-'A'];
            --br['E'-'A'];
            ans.push_back(9);
            solve();
            if(l==1)return;
            br['N'-'A']+=2;
            ++br['I'-'A'];
            ++br['E'-'A'];
            ans.pop_back();
        }
    }
}
int main()
{
    freopen("getting.out","w",stdout);
    cin>>t;
    for(p=1;p<=t;++p)
    {
        cin>>s;
        int sz=s.size();
        for(int i=0;i<sz;++i)++br[s[i]-'A'];
        solve();
        ans.clear();
        memset(br,0,sizeof(br));
        l=0;
    }
    return 0;
}
