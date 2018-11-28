#include<bits/stdc++.h>
using namespace std;
#define ll long long
ll t,z,i,slen,j;
string s;
ll res[20];
char x;
map<char,ll> cnt;
int main()
{
    freopen("input.in","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>t;
	z=0LL;
	while(t--)
    {
        for(i=0;i<=9;i++)
        {
            res[i]=0LL;
        }
        cnt.clear();
        s.clear();
        z++;
        cin>>s;
        slen=s.length();
        for(i=0;i<slen;i++)
        {
            x=s[i];
            cnt[x]++;
        }
        res[0]=cnt['Z'];
        cnt['Z']-=res[0];
        cnt['E']-=res[0];
        cnt['R']-=res[0];
        cnt['O']-=res[0];
        res[8]=cnt['G'];
        cnt['E']-=res[8];
        cnt['I']-=res[8];
        cnt['G']-=res[8];
        cnt['H']-=res[8];
        cnt['T']-=res[8];
        res[6]=cnt['X'];
        cnt['S']-=res[6];
        cnt['I']-=res[6];
        cnt['X']-=res[6];
        res[2]=cnt['W'];
        cnt['T']-=res[2];
        cnt['W']-=res[2];
        cnt['O']-=res[2];
        res[4]=cnt['U'];
        cnt['F']-=res[4];
        cnt['O']-=res[4];
        cnt['U']-=res[4];
        cnt['R']-=res[4];
        res[3]=cnt['H'];
        cnt['T']-=res[3];
        cnt['H']-=res[3];
        cnt['R']-=res[3];
        cnt['E']-=res[3];
        cnt['E']-=res[3];
        res[1]=cnt['O'];
        cnt['O']-=res[1];
        cnt['N']-=res[1];
        cnt['E']-=res[1];
        res[5]=cnt['F'];
        cnt['F']-=res[5];
        cnt['I']-=res[5];
        cnt['V']-=res[5];
        cnt['E']-=res[5];
        res[7]=cnt['S'];
        cnt['S']-=res[7];
        cnt['E']-=res[7];
        cnt['V']-=res[7];
        cnt['E']-=res[7];
        cnt['N']-=res[7];
        res[9]=cnt['I'];
        string ans="";
        for(i=0;i<=9;i++)
        {
            for(j=1;j<=res[i];j++)
            {
                ans+=(i+'0');
            }
        }
        cout<<"Case "<<"#"<<z<<": "<<ans<<"\n";
    }
    return 0;
}