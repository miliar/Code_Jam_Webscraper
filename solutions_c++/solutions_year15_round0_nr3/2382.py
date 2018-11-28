#include <iostream>
#include <string>
#include <vector>

using namespace std;

#define _i 2
#define _j 3
#define _k 4

bool _isi(char c)
{
    return abs(c)==_i;
}

bool _isj(char c)
{
    return abs(c)==_j;
}

bool _isk(char c)
{
    return abs(c)==_k;
}

char _val(char c)
{
    if (c=='i') return _i;
    if (c=='j') return _j;
    if (c=='k') return _k;
}

char mult(char a, char b)
{
    char sign = ( (a>=0) ^ (b>=0) ) ? -1:1;
    a = abs(a);
    b = abs(b);
    char ans=1;
    if (a==1 || b==1)
    {
        return a*b*sign;
    }

    if (a==_i)
    {
        if (b==_i) ans=-1;
        else if (b==_j) ans=_k;
        else if (b==_k) ans=-_j;
    }
    else if (a==_j)
    {
        if (b==_i) ans=-_k;
        else if (b==_j) ans=-1;
        else if (b==_k) ans=_i;
    }
    else if (a==_k)
    {
        if (b==_i) ans=_j;
        else if (b==_j) ans=-_i;
        else if (b==_k) ans=-1;
    }

    return ans*sign;
}

void print(vector<string> d)
{
    for (int i=0; i<d.size(); i++)
    {
        for (int j=0; j<d.size(); j++)
        {
            string s;
            if (d[i][j]<0) s.push_back('-');
            d[i][j]=abs(d[i][j]);
            if (_isi(d[i][j])) s.push_back('i');
            if (_isj(d[i][j])) s.push_back('j');
            if (_isk(d[i][j])) s.push_back('k');
            if (d[i][j]==1) s.push_back('1');
            if (d[i][j]==0) s.push_back('0');
            printf("%3s ",s.c_str());
        }
        cout<<endl;
    }
}

char dp[10010][10010];

bool check(int s1, int s2, int n)
{
    if (s1<1) return false;
    if (s2>=n) return false;

    if (dp[0][s1-1]!=_i) return false;
    if (dp[s1][s2-1]!=_j) return false;
    if (dp[s2][n-1]!=_k) return false;

    return true;
}

int main()
{
    freopen("C-small-attempt2.in", "r", stdin);
    freopen("c.out", "w", stdout);

    int T;
    cin>>T;
    for (int cas=1; cas<=T; cas++)
    {
        int l,x;
        cin>>l>>x;
        string s,t;
        cin>>t;
        for (int i=0; i<x; i++) s.append(t);
        int n = s.size();
        //cout<<dp[0].size()<<endl;
        for (int i=0; i<s.size(); i++)
        {
            dp[i][i] = _val(s[i]);
        }

        for (int len=2; len<=n; len++)
        {
            for (int i=0, j=i+len-1; j<n; i++, j++)
            {
                dp[i][j] = mult(dp[i][j-1], dp[j][j]);
            }
        }
        //print(dp);

        bool found = false;
        for (int i=1; i<=n; i++)
        {
            for (int j=i+1; j<=n; j++)
            {
                if (check(i, j, n))
                {
                    found = true;
                    break;
                }
            }
            if (found)
            {
                break;
            }
        }

        if (found)
        {
            cout<<"Case #"<<cas<<": YES"<<endl;
        }
        else
        {
            cout<<"Case #"<<cas<<": NO"<<endl;
        }
    }
    return 0;
}
