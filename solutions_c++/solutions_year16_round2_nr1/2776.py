#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<string>
#include<stack>
#include<queue>
#include<vector>
#include<algorithm>
#include<cstdlib>
#include<set>
using namespace std;
#define LL long long
#define maxn 100010
const double pi=acos(-1);

int n,t;
char s[2010];
int vis[300];
int num[11];
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    cin>>t;
    int o=1;
    while(t--)
    {
        memset(vis,0,sizeof(vis));
        cin>>s;
        int len=strlen(s);
        for(int i=0;i<len;i++)
        {
            vis[s[i]]++;
        }
        num[0]=vis['Z'];
        vis['Z']=0;
        //cout<<"0 "<<num[0]<<endl;
        vis['E']-=num[0];
        vis['R']-=num[0];
        vis['O']-=num[0];
        num[2]=vis['W'];
        vis['W']=0;
       // cout<<"2 "<<num[2]<<endl;
        vis['T']-=num[2];
        vis['O']-=num[2];
        num[4]=vis['U'];
        vis['U']=0;
       // cout<<"4 "<<num[4]<<endl;
        vis['F']-=num[4];
        vis['O']-=num[4];
        vis['R']-=num[4];
        num[6]=vis['X'];
        vis['X']=0;
       // cout<<"6 "<<num[6]<<endl;
        vis['S']-=num[6];
        vis['I']-=num[6];
        num[8]=vis['G'];
        vis['G']=0;
       // cout<<"8 "<<num[8]<<endl;
        vis['E']-=num[8];
        vis['I']-=num[8];
        vis['H']-=num[8];
        vis['T']-=num[8];
        num[3]=vis['T'];
        vis['T']=0;
       // cout<<"3 "<<num[3]<<endl;
        vis['H']-=num[3];
        vis['R']-=num[3];
        vis['E']-=num[3];
        vis['E']-=num[3];
        num[7]=vis['S'];
        vis['S']=0;
       // cout<<"7 "<<num[7]<<endl;
        vis['E']-=num[7];
        vis['V']-=num[7];
        vis['E']-=num[7];
        vis['N']-=num[7];
        num[5]=vis['F'];
        vis['F']=0;
        //cout<<"5 "<<num[5]<<endl;
        vis['I']-=num[5];
        vis['V']-=num[5];
        vis['E']-=num[5];
        num[1]=vis['O'];
        vis['O']=0;
        //cout<<"1 "<<num[1]<<endl;
        vis['N']-=num[1];
        vis['E']-=num[1];
        num[9]=vis['I'];
        vis['I']=0;
        //cout<<"9 "<<num[9]<<endl;
        char ans[20000];
        int j=0;
        for(int i=0;i<=9;i++)
        {
            while(num[i]--)
            {
                ans[j++]=(char)(i+48);
            }
        }
        sort(ans,ans+j);
        printf("Case #%d: ",o++);
        for(int i=0;i<j;i++)
            cout<<ans[i];
        cout<<endl;
    }
}





