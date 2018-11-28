#include<iostream>
#include<fstream>
#include<cstring>
#include<stdio.h>
#include<assert.h>
#include<algorithm>
#include<cmath>
#include<vector>
#include<queue>
#include<stack>
#include<map>
#include<set>
#define mp make_pair
#define pb push_back
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define F first
#define S second
#define ll long long
#define pp pair<int,int>
#define SS system("pause")
#define INF 1000000000
#define dd double
#define vec vector<int>::iterator
using namespace std;
const int N=100006;
int T,t,i,j,n,x,l,I='i',J='j',K='k';
int rk[N],li[N],now;
string a,s,ans;

int go(int x,int y){
    int key=1;
    if(x<0)key*=-1;
    if(y<0)key*=-1;

    x=abs(x);
    y=abs(y);

    if(x==1)return key*y;
    if(y==1)return key*x;
    if(x==y)return -1*key;

    if(x==I && y==J)return key*K;
    if(x==I && y==K)return -1*key*J;
    if(x==J && y==I)return -1*key*K;
    if(x==J && y==K)return key*I;
    if(x==K && y==I)return key*J;
    if(x==K && y==J)return -1*key*I;
    assert(0);
}

int main()
{freopen("C-small-attempt3.in","r",stdin);
 freopen("Cout.txt","w",stdout);
 scanf("%d",&T);
 for(t=1;t<=T;t++){
    scanf("%d%d",&l,&x);
    cin>>a;
    s="a";
    l=l*x+1;
    for(i=0;i<x;i++)s+=a;

    now=1;
    for(i=1;i<l;i++){
        now=go(now,s[i]);
        if(now==I || li[i-1])li[i]=1;
    }
    now=1;
    for(i=l-1;i>0;i--){
        now=go(s[i],now);
        if(now==K || rk[i+1])rk[i]=1;
    }

    int goal=go(go(I,J),K);


    ans="NO";
    if(now==goal)
    for(j=2;j+1<l;j++)
        if(li[j-1] && rk[j+1])ans="YES";
    cout<<"Case #"<<t<<": "<<ans<<endl;
    for(i=0;i<l;i++)li[i]=rk[i]=0;
 }
 return 0;
}

