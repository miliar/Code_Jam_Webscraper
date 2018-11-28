#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<cmath>
#include<cstdlib>
#include<cstdio>
#include<set>
#include<map>
#include<climits>
#include<cstring>
#include<list>
#include<fstream>
#include<queue>
#include<sstream>
#include<stack>
#include<iomanip>

using namespace std;
typedef long long LL;

LL mod=1e9+7;
string s;
map<vector <int>, bool> dp;
int pre[10][26];
string ret;

bool dfs(vector <int> ctr)
{
    int flag=0;
    for(int i=0; i<26; i++)
    {
        if(ctr[i]>0)
        {
            flag=1;
            break;
        }
    }

    if(flag==0)
        return true;

    if(dp.find(ctr)!=dp.end())
        return dp[ctr];

    vector <int> temp=ctr;

    for(int i=0; i<=9; i++)
    {
        int f=0;
        for(int j=0; j<26; j++)
        {
            if(temp[j]-pre[i][j]<0)
            {
                temp=ctr;
                f=1;
                break;
            }
            else
            {
                temp[j]-=pre[i][j];
            }
        }

        if(f==1)
            continue;

        bool t= dfs(temp);

        if(t==true)
        {
            ret+=(char)('0'+i);
            return true;
        }
        else
        {
            temp=ctr;
            continue;
        }

    }

    return false;

}

int main()
{

    ios_base::sync_with_stdio(false);
    cin.tie(0);

    ifstream cin("A-small-attempt0.in");
    ofstream cout("file.txt");

    pre[0]['Z'-'A']++;
    pre[0]['E'-'A']++;
    pre[0]['R'-'A']++;
    pre[0]['O'-'A']++;

    pre[1]['O'-'A']++;
    pre[1]['N'-'A']++;
    pre[1]['E'-'A']++;

    pre[2]['T'-'A']++;
    pre[2]['W'-'A']++;
    pre[2]['O'-'A']++;

    pre[3]['T'-'A']++;
    pre[3]['H'-'A']++;
    pre[3]['R'-'A']++;
    pre[3]['E'-'A']+=2;

    pre[4]['F'-'A']++;
    pre[4]['O'-'A']++;
    pre[4]['U'-'A']++;
    pre[4]['R'-'A']++;

    pre[5]['F'-'A']++;
    pre[5]['I'-'A']++;
    pre[5]['V'-'A']++;
    pre[5]['E'-'A']++;

    pre[6]['S'-'A']++;
    pre[6]['I'-'A']++;
    pre[6]['X'-'A']++;

    pre[7]['S'-'A']++;
    pre[7]['E'-'A']+=2;
    pre[7]['V'-'A']++;
    pre[7]['N'-'A']++;

    pre[8]['E'-'A']++;
    pre[8]['I'-'A']++;
    pre[8]['G'-'A']++;
    pre[8]['H'-'A']++;
    pre[8]['T'-'A']++;

    pre[9]['N'-'A']+=2;
    pre[9]['I'-'A']++;
    pre[9]['E'-'A']++;


    int T;
    cin>>T;

    for(int I=0; I<T; I++)
    {
        cin>>s;

        vector <int> ctr(26);

        for(int i=0; i<s.length(); i++)
            ctr[s[i]-'A']++;

        bool x=dfs(ctr);

        reverse(ret.begin(), ret.end());

        cout<<"Case #"<<I+1<<": "<<ret<<'\n';

        ret="";
        dp.clear();

    }

}
