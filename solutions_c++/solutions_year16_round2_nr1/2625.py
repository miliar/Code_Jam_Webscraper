#include<bits/stdc++.h>                         //Author: Sharad Chandran
#define lld long long int                       //Handle: sharad07
#define llu unsigned long long int
#define pb(x) push_back(x)
#define pii pair<int,int>
#define pll pair<lld,lld>
#define pq priority_queue<int> 
#define mp(x,y) make_pair(x,y)
#define sz size()
#define inp1(x) scanf("%d",&x)
#define inp2(x,y) scanf("%d%d",&x,&y)
#define inp3(x,y,z) scanf("%d%d%d",&x,&y,&z)
#define print(x) printf("%d",x)
#define println(x) printf("%d\n",x)
#define _for(i,x,y) for(int i=x;i<y;i++)
using namespace std;
const int maxx=1e5+3;
lld mod=1e9+7;

string solve()
{
    string inp="",zero="",one="",two="",three="",four="",five="",six="",seven="",eight="",nine="";
    cin>>inp;
    int alpha[26];
    memset(alpha,0,sizeof(alpha));
    _for(i,0,inp.length()) alpha[inp[i]-'A']++;
    int cnt;
    cnt=alpha['Z'-'A']; //0
    if(cnt>0)
    {
        _for(j,0,cnt) zero+='0';
        alpha['Z'-'A']-=cnt;
        alpha['E'-'A']-=cnt;
        alpha['R'-'A']-=cnt;
        alpha['O'-'A']-=cnt;
    }
    
    cnt=alpha['G'-'A']; //8
    if(cnt>0)
    {
        _for(j,0,cnt) eight+='8';
        alpha['E'-'A']-=cnt;
        alpha['I'-'A']-=cnt;
        alpha['G'-'A']-=cnt;
        alpha['H'-'A']-=cnt;
        alpha['T'-'A']-=cnt;
    }
    
    cnt=alpha['X'-'A']; //6
    if(cnt>0)
    {
        _for(j,0,cnt) six+='6';
        alpha['S'-'A']-=cnt;
        alpha['I'-'A']-=cnt;
        alpha['X'-'A']-=cnt;
    }
    
    cnt=alpha['W'-'A']; //2
    if(cnt>0)
    {
        _for(j,0,cnt) two+='2';
        alpha['T'-'A']-=cnt;
        alpha['W'-'A']-=cnt;
        alpha['O'-'A']-=cnt;
    }
    
    cnt=alpha['U'-'A']; //4
    if(cnt>0)
    {
        _for(j,0,cnt) four+='4';
        alpha['F'-'A']-=cnt;
        alpha['O'-'A']-=cnt;
        alpha['U'-'A']-=cnt;
        alpha['R'-'A']-=cnt;
    }
    
    cnt=alpha['O'-'A']; //1
    if(cnt>0)
    {
        _for(j,0,cnt) one+='1';
        alpha['O'-'A']-=cnt;
        alpha['N'-'A']-=cnt;
        alpha['E'-'A']-=cnt;
    }
    
    cnt=alpha['H'-'A']; //3
    if(cnt>0)
    {
        _for(j,0,cnt) three+='3';
        alpha['T'-'A']-=cnt;
        alpha['H'-'A']-=cnt;
        alpha['R'-'A']-=cnt;
        alpha['E'-'A']-=cnt;
        alpha['E'-'A']-=cnt;
    }
    
    cnt=alpha['F'-'A']; //5
    if(cnt>0)
    {
        _for(j,0,cnt) five+='5';
        alpha['F'-'A']-=cnt;
        alpha['I'-'A']-=cnt;
        alpha['V'-'A']-=cnt;
        alpha['E'-'A']-=cnt;
    }
    
    cnt=alpha['S'-'A']; //7
    if(cnt>0)
    {
        _for(j,0,cnt) seven+='7';
        alpha['S'-'A']-=cnt;
        alpha['E'-'A']-=cnt;
        alpha['V'-'A']-=cnt;
        alpha['E'-'A']-=cnt;
        alpha['N'-'A']-=cnt;
    }
    
    cnt=alpha['N'-'A']; //9
    if(cnt>0)
    {
        _for(j,0,cnt/2) nine+='9';
        alpha['N'-'A']-=cnt;
        alpha['I'-'A']-=cnt;
        alpha['N'-'A']-=cnt;
        alpha['E'-'A']-=cnt;
    }
    
    return zero+one+two+three+four+five+six+seven+eight+nine; 
}

int main()
{
    int t,N;
    freopen("A.in","r",stdin);
    freopen("out.in","w",stdout);
    cin>>t;
    _for(tc,1,t+1)
    {
        cout<<"Case #"<<tc<<": "<<solve()<<endl;
    }
    return 0;
}