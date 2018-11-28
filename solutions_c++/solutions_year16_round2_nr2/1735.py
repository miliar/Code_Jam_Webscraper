#include<bits/stdc++.h>
using namespace std;
typedef pair<int,int> pii;
typedef pair<long long,long long> pll;
typedef vector<int> vi;
typedef vector<long long> vll;
typedef vector<pii> vpii;
typedef vector<pll> vpll;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define MOD 1000000007
#define ll long long
int GCD(int a, int b)
{
    return b? GCD(b,a%b) : a;
}
bool chk(string first, string second)
{
    string t1 = first + second;
    string t2 = second + first;
    return t1 < t2;
}
struct sort_pred
{
    bool operator()(const pair<int,int> &left, const pair<int,int> &right)
    {
        return left.second < right.second;
    }
};
long long POW(long long Base, long long Exp)
{
    long long y,ret=1;
    y=Base;
    while(Exp)
    {
        if(Exp&1)
            ret=(ret*y)%MOD;
        y = (y*y)%MOD;
        Exp/=2;
    }
    return ret%MOD;
}
vi A,B,Mark;
stack <char> Brkt;
vector<char> Aao;
void fun(int l, string str)
{
    string lwr="";
    for(int j=0; j<l; j++)
    {
        lwr = lwr + "0";
    }

    string upr="";

    for(int j=0; j<l-4; j++)
    {
        upr = upr + "1";
    }
    upr = upr + "3098";

    if(str>=lwr && str<=upr)
    {
        str = "1" + str;
    }
    cout<<str<<endl;
}

string str,str1,s1,s2;
vector<string> pehla,doosra;
int main()
{
    int t;
    cin>>t;
    for(int tc=1; tc<=t; tc++)
    {
        int i,j,k,len;
        cin>>s1>>s2;

        queue<string> q;
        q.push(s1);

        while(!q.empty())
        {
            str=q.front();
            len = str.length();
            q.pop();

            for(i=0; i<len; i++)
            {
                if(str[i]=='?')
                {
                    for(j=0; j<10; j++)
                    {
                        str[i]= j + '0';
                        q.push(str);
                    }
                    break;
                }
            }
            if(i==len)
                pehla.pb(str);
        }
        q.push(s2);

        while(!q.empty())
        {
            str=q.front();
            len = str.length();
            q.pop();

            for(i=0; i<len; i++)
            {
                if(str[i]=='?')
                {
                    for(j=0; j<10; j++)
                    {
                        str[i]= j + '0';
                        q.push(str);
                    }
                    break;
                }
            }
            if(i==len)
                doosra.pb(str);
        }

        int mini=MOD;
        string a1,a2;
        int a11,a21;
        for(i=0; i<pehla.size(); i++)
        {
            int val1=0,val2=0;
            for(k=pehla[i].size()-1; k>=0; k--)
            {
                val1+=(pehla[i][k]-'0')*pow(10,pehla[i].length()-1-k);
            }

            for(j=0; j<doosra.size(); j++)
            {
                val2=0;
                for(k=doosra[j].size()-1; k>=0; k--)
                {
                    val2+=(doosra[j][k]-'0')*pow(10,doosra[j].length()-1-k);
                }

                if(abs(val1-val2)<mini)
                {
                    mini=abs(val1-val2);
                    a11=val1;
                    a21=val2;
                    a1=pehla[i];
                    a2=doosra[j];
                }
                else if(abs(val1-val2)==mini)
                {

                    if(val1<a11)
                    {
                        a11=val1;
                        a21=val2;
                        a1=pehla[i];
                        a2=doosra[j];
                    }
                    else if(a11==val1)
                    {
                        if(val2<a21)
                        {
                            a11=val1;
                            a21=val2;
                            a1=pehla[i];
                            a2=doosra[j];
                        }

                    }

                }
            }
        }
        printf("Case #%d: ",tc);
        cout<<a1<<" "<<a2<<endl;
        a1.clear();
        a2.clear();
        pehla.clear();
        doosra.clear();
        str.clear();
    }
    return 0;
}
