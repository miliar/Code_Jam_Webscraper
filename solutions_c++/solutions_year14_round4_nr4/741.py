#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>
#include<ctime>
#include<assert.h>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
#include<limits.h>

using namespace std;

#define MAX(a,b) ((a)>(b) ? (a) : (b))
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define EPS 1e-9
#define asdf exit(0);







string in[20];
int len[20];
int n;//mach
int m;//string
int mx;
int cnt;
int mem[10][10];
int mark[20];




void gone()
{
    int now=0;
    vector<int> v[5];

    int i,j;


    for(i=0;i<m;i++)
    {
        v[mark[i]].push_back(i);
    }



    for(i=0;i<n;i++)
    {
        for(j=0;j<v[i].size();j++)
        {
            now+=(len[ v[i][j] ]+1);
            if(j) now-=(1+mem[ v[i][j] ][ v[i][j-1] ]);
        }
        //if(v[i].size()==0) now++;
    }




    //cout<<now<<endl;

    if(now==mx)
    {
        cnt++;
    }
    else if(now>mx)
    {
        mx=now;
        cnt=1;
    }

}



void bttk(int pos)
{
    if(pos==m)
    {
        gone();
        return;
    }

    int i;
    for(i=0;i<n;i++)
    {
        mark[pos]=i;
        bttk(pos+1);
    }
}


void ini()
{
    int i,j,k,n1,n2;


    for(i=0;i<m;i++) len[i]=in[i].length();


    for(i=0;i<m;i++)
    for(j=0;j<m;j++)
    {
        n1=len[i];
        n2=len[j];
        mem[i][j]=0;

        for(k=0;k<min(n1,n2);k++)
        {
            if(in[i][k]!=in[j][k]) break;
            mem[i][j]++;
        }


    }
}
int main()
{
    //freopen("in.txt","r",stdin);



    freopen("D-small-attempt2.in","r",stdin);
	freopen("D-small-attempt2.out","w",stdout);
    int T,cs,i,j,k,x;

    scanf("%d",&T);

    for(cs=1;cs<=T;cs++)
    {
        printf("Case #%d: ",cs);
        mx=0;
        cnt=0;

        scanf("%d %d",&m,&n);
        for(i=0;i<m;i++)
        {
            cin>>in[i];
        }
        sort(in,in+m);


        ini();

        bttk(0);

        //gone();
        printf("%d %d\n",mx,cnt);
    }



    return 0;
}
