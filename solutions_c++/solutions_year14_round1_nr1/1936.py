#include<bits/stdc++.h>
#define gc getchar
#define ll long long int
using namespace std;


int n,mini,l;
long long int out[100];
inline long long int inp();
int check(ll[]);
int fliprec(int ,ll [],int );
int minimum(int,int);

int main()
{
    int t,j,counte,i;
    ll avail[100];

	scanf("%d",&t);

    for(j=1;j<=t;j++)
    {
        counte=1;
        printf("Case #%d: ",j);
        mini=25000;
        scanf("%d%d\n",&n,&l);
        for(i=0;i<n;i++) avail[i]=inp();
        for(i=0;i<n;i++) out[i]=inp();
        sort(out,out+n);

        if(check(avail)) {printf("0\n"); continue;}


        //for(i=0;i<n;i++) printf("avail%lld\n",avail[i]);

        for(i=0;i<l;i++)
        {
        fliprec(i,avail,counte);
		//for(j=0;j<n;j++) printf("avail%lld ",avail[j]);
		//printf("\n");
		}

        if(mini>=500) printf("NOT POSSIBLE\n");
        else printf("%d\n",mini);
    }
}

int fliprec(int pass,ll avail[100],int counte)
{
	long long int availe[100];
	if(pass==l) return 0;
    int i,j;
    ll y=1<<pass;
    for(i=0;i<n;i++)
    {
    	availe[i]=avail[i];
        if((availe[i]&y)==0) availe[i]=availe[i]|y;
        else availe[i]=availe[i]&(~y);
        //printf("check%lld\n",availe[i]);
    }
    if(check(availe)) mini=minimum(counte,mini);

    for(j=pass+1;j<l;j++) fliprec(j,availe,counte+1);
}

inline long long int inp()
{
  char c = gc();
  long long int ret = 0;
  while((c<'0' || c>'9') && c!='-') c = gc();
  while(c>='0' && c<='9')
  {
    ret =ret*2+c-'0';
    c = gc();
  }
  return ret;
}

int check(long long int avail[100])
{
    int i=0;
    sort(avail,avail+n);
    for(i=0;i<n;)
    {
        if(avail[i]==out[i]) i++;
        else break;
    }
    if(i==n) return 1;
    else return 0;
}

int minimum(int a,int b)
{
    if(a>b) return b;
    else return a;
}
