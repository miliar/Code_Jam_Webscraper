/*
ID: kishwarshafin
PROG:
LANG: C++
*/
/*
Timus JI: 119454XP
*/
#include<iostream>
#include<vector>
#include<stack>
#include<string>
#include<queue>
#include<map>
#include<algorithm>
#include<sstream>
using namespace std;
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>
#define MAX 100
#define INF 1<<23

#define I1(a) scanf("%d",&a)
#define I2(a,b) scanf("%d %d",&a,&b)
#define I3(a,b,c) scanf("%d %d %d",&a,&b,&c)
#define rep(i,s,e) for(i=s;i<e;i++)
#define repr(i,s,e) for(i=s;i>e;i--)


#define in(a) freopen(a,"r",stdin)
#define out(a) freopen(a,"w",stdout)
#define ll long long
ll BigMod(ll B,ll P,ll M){  ll R=1; while(P>0)  {if(P%2==1){R=(R*B)%M;}P/=2;B=(B*B)%M;} return R%M;}
#define ull unsigned long long
int nums[10];
int R,N,M,K;
int mem[10][10];
int master[10];
vector<int>ans;

void factorize(int i,int num)
{
    if(num%2==0)
    {

        while(num%2==0)
        {
            num/=2;
            mem[i][2]++;
        }
    }
    if(num%3==0)
    {
        while(num%3==0)
        {
            num/=3;
            mem[i][3]++;
        }
    }
    if(num%5==0)
    {
        while(num%5==0)
        {
            num/=5;
            mem[i][5]++;
        }
    }
}

bool meets(vector<int>S)
{
    int freq[10];
    memset(freq,0,sizeof(freq));
    for(int i=0;i<S.size();i++)
    {
        if(S[i]==2)freq[2]++;
        if(S[i]==3)freq[3]++;
        if(S[i]==4)freq[2]+=2;
        if(S[i]==5)freq[5]++;
    }

    for(int i=0;i<K;i++)
    {
        if(freq[2]<mem[i][2])return false;
        if(freq[3]<mem[i][3])return false;
        if(freq[5]<mem[i][5])return false;
    }
    return true;
}

void recur(int pos,vector<int>S)
{
    if(S.size()==N)
    {
        if(meets(S))
        {
            ans=S;
        }
    }
    else if(pos<2)
    {
        return;
    }
    else
    {
        if(pos==3)
        {
            vector<int>Ns;
            Ns=S;
            for(int i=1;i<=master[3];i++)
            {
                Ns.push_back(3);
                recur(2,Ns);
            }
            recur(2,S);
        }
        if(pos==5)
        {
            vector<int>Ns;
            Ns=S;
            for(int i=1;i<=master[5];i++)
            {
                Ns.push_back(5);
                recur(3,Ns);
            }
            recur(3,S);
        }

        if(pos==2)
        {
            vector<int>Ns1;
            vector<int>Ns2;
            Ns1=S;
            Ns2=S;
            for(int i=1;i<=master[2];i++)
            {
                Ns1.push_back(2);
                recur(1,Ns1);
                if(i%2==0)
                {
                    Ns2.push_back(4);
                    recur(1,Ns2);
                }
            }
            recur(1,S);
        }
    }
}

void solve()
{
    memset(mem,0,sizeof(mem));
    memset(master,0,sizeof(master));
    ans.clear();
    for(int i=0;i<K;i++)
        factorize(i,nums[i]);


    for(int i=0;i<K;i++)
    {
        master[2]=max(master[2],mem[i][2]);
        master[3]=max(master[3],mem[i][3]);
        master[5]=max(master[5],mem[i][5]);
    }

    vector<int>solve;
    recur(5,solve);

    if(ans.size()==N)
    {
        for(int i=0;i<ans.size();i++)
        {
            cout<<ans[i];
        }
        cout<<endl;
    }
    else
    {
        for(int i=0;i<N;i++)
            cout<<"2";
        cout<<endl;
    }
}

int main()
{
    #ifndef ONLINE_JUDGE
	in("in.txt");
	out("out.txt");
    #endif

    int t,caseno=1;
    cin>>t;
    while(t--)
    {
        printf("Case #%d:\n",caseno++);

        cin>>R>>N>>M>>K;
        for(int i=0;i<R;i++)
        {
            for(int i=0;i<K;i++)
            {
                scanf("%d",&nums[i]);
            }
            solve();
        }

    }
	return 0;
}
