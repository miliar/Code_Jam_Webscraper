#include<bits/stdc++.h>
#define ll long long int
#define sd(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define slf(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define INF 99999999
#define pii pair<int,int>
#define MAX 1005
int Set(int n,int pos) {return n | (1<<pos);}
int Reset(int n,int pos){return n & ~(1<<pos);}
int Check(int n,int pos){return n & (1<<pos);}
using namespace std;
int ch[30],ans[10];
map<int,string>mp;
int solve(int n)
{
    int cnt=ch[n];
    string temp=mp[n];
    for(int i=0;i<temp.size();i++)
    {
        ch[temp[i]-'A']-=cnt;
    }
    return cnt;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t,T=0,i,j;
    mp['Z'-'A']="ZERO";
    mp['W'-'A']="TWO";
    mp['U'-'A']="FOUR";
    mp['G'-'A']="EIGHT";
    mp['X'-'A']="SIX";
    mp['O'-'A']="ONE";
    mp['H'-'A']="THREE";
    mp['F'-'A']="FIVE";
    mp['S'-'A']="SEVEN";
    mp['I'-'A']="NINE";
    string s;
    cin>>t;
    while(t--)
    {
        memset(ch,0,sizeof(ch));
        cin>>s;
        for(i=0;i<s.size();i++)
        {
            ch[s[i]-'A']++;
        }
        ans[0]=solve('Z'-'A');
        ans[2]=solve('W'-'A');
        ans[4]=solve('U'-'A');
        ans[6]=solve('X'-'A');
        ans[8]=solve('G'-'A');
        ans[1]=solve('O'-'A');
        ans[3]=solve('H'-'A');
        ans[5]=solve('F'-'A');
        ans[7]=solve('S'-'A');
        ans[9]=solve('I'-'A');
        cout<<"Case #"<<++T<<": ";
        for(i=0;i<10;i++)
        {
            while(ans[i]--)
            {
                cout<<i;
            }
        }
        cout<<endl;
    }
    return 0;
}
