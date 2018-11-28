#include<bits/stdtr1c++.h>
using namespace std;

typedef pair<char,int> pr;
vector<pr> v;
vector<int> ch[105];

void zabbat(string &s)
{
    v.clear();
    v.push_back(pr(s[0],1));
    int st=0;
    for(int i=1;i<s.size();i++)
    {
        if(s[i]==v[st].first)
        {
            v[st].second++;
        }
        else
        {
            st=v.size();
            v.push_back(pr(s[i],1));
        }
    }
    
    for(int i=0;i<v.size();i++)
    {
        ch[i].push_back(v[i].second);
    }
}

int check(string &s)
{
    vector<pr> vv;
    
    vv.push_back(pr(s[0],1));
    int st=0;
    
    for(int i=1;i<s.size();i++)
    {
        if(s[i]==vv[st].first)
        {
            vv[st].second++;
        }
        else
        {
            st=vv.size();
            vv.push_back(pr(s[i],1));
        }
    }
    if(vv.size()!=v.size())
        return 1;
    
    for(int i=0;i<v.size();i++)
        if(vv[i].first!=v[i].first)
            return 1;
    
    for(int i=0;i<vv.size();i++)
    {
        ch[i].push_back(vv[i].second);
    }
    
    return 0;
}

int cnt()
{
    int ret=0;
    for(int i=0;i<v.size();i++)
    {
        int mini=1<<30;
        for(int j=0;j<=104;j++)
        {
            int c=0;
            for(int k=0;k<ch[i].size();k++)
            {
                c+=abs(ch[i][k]-j);
            }
            //cout<<j<<" "<<c<<endl;
            mini=min(mini,c);
        }
        ret+=mini;
    }
    return ret;
}

int main()
{
    #ifndef ONLINE_JUDGE
        freopen("2.in","r",stdin);
        freopen("3.out","w",stdout);
        
    #endif // ONLINE_JUDGE
    
    ios::sync_with_stdio(false);
    cin.tie(NULL);
    cout.tie(NULL);
    
    int t;
    cin>>t;
    for(int ic=1;ic<=t;ic++)
    {
         for(int i=0;i<105;i++)
            ch[i].clear();
        int n;
        string s;
        cin>>n;
        int f=0,feg=0;
        for(int i=0;i<n;i++)
        {
            cin>>s;
            if(!f)
                {
                    f=1;
                    zabbat(s);
                }
            else
            {
                feg|=check(s);
            }
        }
        cout<<"Case #"<<ic<<": ";
        if(feg)
        {
            cout<<"Fegla Won"<<endl;
        }
        else
        {
            cout<<cnt()<<endl;
        }
    }
    return 0;
    
}
