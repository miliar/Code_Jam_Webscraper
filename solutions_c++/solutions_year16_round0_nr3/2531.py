#include <bits/stdc++.h>

using namespace std;

vector<string> ans;

int pri[(1<<17)];

void go()
{
    int i,j;
    pri[0]=pri[1]=1;
    for(i=2;i<(1<<17);i++)
    {
        if(!pri[i])
        {
            for(j=i+i;j<(1<<17);j+=i)
                pri[j]=1;
        }
    }
}

string conv(long long x)
{
    string s="";
    while(x)
    {
        s+=((x%2)+'0');
        x/=2;
    }
    reverse(s.begin(),s.end());
    return s;
}

bool pr(long long x)
{
    long long i;
    if(!x||x==1) return 0;
    if(x>=(1<<17))
    {
        for(i=2;i*i<=x;i++)
        {
            if(x%i==0) return 0;
        }
        return 1;
    }
    return !pri[x];
}

bool ok(string s)
{
    long long i,j;
    for(i=2;i<=10;i++)
    {
        long long num=0;
        for(j=0;j<s.size();j++)
        {
            num*=i;
            num+=(s[j]-'0');
        }
        if(pr(num)) return 0;
    }
    return 1;
}

void get(string s)
{
    long long i,j;
    for(i=2;i<=10;i++)
    {
        long long num=0;
        for(j=0;j<s.size();j++)
        {
            num*=i;
            num+=(s[j]-'0');
        }
        //cout << s << " " << num << endl;
        for(j=2;j*j<=num;j++)
        {
            if(num%j==0)
            {
                cout << j << " ";
                break;
            }
        }
    }
    cout << endl;
}

int main()
{
    freopen("C.out","w",stdout);
    go();
    cout << "Case #1:" << endl;
    long long i;
    int t;
    cin >> t;
    int n,k;
    cin >> n >> k;
    for(i=1;i<=(1LL<<17);i++)
    {
        string x=conv(i);
        if(x.size()!=n||x[0]=='0'||x[x.size()-1]=='0') continue;
        //cout << x << endl;
        if(ok(x)){ans.push_back(x);}
        if(ans.size()>=k) break;
    }
    for(i=0;i<ans.size();i++)
    {
        cout << ans[i] << " ";
        get(ans[i]);
    }
}
