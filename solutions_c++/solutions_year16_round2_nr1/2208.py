#include <bits/stdc++.h>

using namespace std;
#define ll long long

string st[10]={"ZERO","ONE","TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

int X[26];
string ans="";

void reduce(char c,int z)
{
        int cnt=X[c-'A'];
        string r =st[z];
        for(int i=0;i<r.length();i++)
        {
            X[r[i]-'A']-=cnt;
        }
        //cout<<c<<" "<<z<<" "<<ans<<endl;
//        }
    //i[c-'A'];
    if(z==9)cnt/=2;
    while(cnt--)
    {
        ans+=(z+'0');
    }
}

int main()
{
    freopen("inputl.in","r",stdin);
    freopen("output3.txt","w",stdout);
    int T;
    cin>>T;
    for(int iter=1;iter<=T;iter++)
    {
        string s;
        cin>>s;
        ans="";
        int slen = s.length();
        for(int i=0;i<26;i++)
        {
            X[i]=0;
        }
        for(int i=0;i<slen;i++)
        {
            X[s[i]-'A']++;
        }
        //cout<<"safe\n";

        reduce('G',8);
        reduce('X',6);
        reduce('U',4);
        reduce('H',3);
        reduce('Z',0);
        reduce('W',2);
        reduce('O',1);
        reduce('F',5);
        reduce('S',7);
        reduce('N',9);
        //cout<<ans<<endl;
        sort(ans.begin(),ans.end());
        cout<<"Case #"<<iter<<": "<<ans<<endl;
    }
}

