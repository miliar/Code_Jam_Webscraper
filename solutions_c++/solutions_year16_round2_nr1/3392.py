#include<iostream>
#include<string>
#include<string.h>
using namespace std;
string a[10]= {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
int x[10][26];
int ans[10];
int cnt[26];
int main()
{
    int i,j,k;
    string s;
    int t,ca=1;
    memset(x,0,sizeof(x));
    for(i=0; i<10; i++)
    {
        for(j=0; j<a[i].size(); j++)
        {
            x[i][a[i][j]-'A']++;
        }
    }
    cin>>t;
    while(t--)
    {
        cin>>s;
        cout<<"Case #"<<ca<<": ";
        ca++;
        memset(ans,0,sizeof(ans));
        memset(cnt,0,sizeof(cnt));
        for(i=0; i<s.size(); i++)
        {
            cnt[s[i]-'A']++;
        }
        int tmp,y;
        tmp='Z'-'A';
        if(cnt[tmp]!=0)
        {
            y=0;
            ans[y]+=cnt[tmp];
            for(i=0; i<26; i++)
            {
                cnt[i]-=x[y][i]*ans[y];
            }
        }
        tmp='X'-'A';
        if(cnt[tmp]!=0)
        {
            y=6;
            ans[y]+=cnt[tmp];
            for(i=0; i<26; i++)
            {
                cnt[i]-=x[y][i]*ans[y];
            }
        }
        tmp='U'-'A';
        if(cnt[tmp]!=0)
        {
            y=4;
            ans[y]+=cnt[tmp];
            for(i=0; i<26; i++)
            {
                cnt[i]-=x[y][i]*ans[y];
            }
        }
        tmp='W'-'A';
        if(cnt[tmp]!=0)
        {
            y=2;
            ans[y]+=cnt[tmp];
            for(i=0; i<26; i++)
            {
                cnt[i]-=x[y][i]*ans[y];
            }
        }
        tmp='G'-'A';
        if(cnt[tmp]!=0)
        {
            y=8;
            ans[y]+=cnt[tmp];
            for(i=0; i<26; i++)
            {
                cnt[i]-=x[y][i]*ans[y];
            }
        }
        tmp='S'-'A';
        if(cnt[tmp]!=0)
        {
            y=7;
            ans[y]+=cnt[tmp];
            for(i=0; i<26; i++)
            {
                cnt[i]-=x[y][i]*ans[y];
            }
        }
        tmp='R'-'A';
        if(cnt[tmp]!=0)
        {
            y=3;
            ans[y]+=cnt[tmp];
            for(i=0; i<26; i++)
            {
                cnt[i]-=x[y][i]*ans[y];
            }
        }
        tmp='F'-'A';
        if(cnt[tmp]!=0)
        {
            y=5;
            ans[y]+=cnt[tmp];
            for(i=0; i<26; i++)
            {
                cnt[i]-=x[y][i]*ans[y];
            }
        }
        tmp='O'-'A';
        if(cnt[tmp]!=0)
        {
            y=1;
            ans[y]+=cnt[tmp];
            for(i=0; i<26; i++)
            {
                cnt[i]-=x[y][i]*ans[y];
            }
        }
        tmp='E'-'A';
        if(cnt[tmp]!=0)
        {
            y=9;
            ans[y]+=cnt[tmp];
            for(i=0; i<26; i++)
            {
                cnt[i]-=x[y][i]*ans[y];
            }
        }
        for(i=0;i<10;i++)
        {
            for(j=0;j<ans[i];j++)
            {
                cout<<((char)('0'+i));
            }
        }
        cout<<endl;
    }
}
