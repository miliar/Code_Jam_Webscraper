#include <iostream>
#include <cmath>
#include <string>
#include <cstring>
#include <vector>
#include <stack>
#include <cstdio>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <queue>
#include <set>

using namespace std;

typedef long long ll;

#define SL(s) strlen(s)
#define BUF 1024
#define pb(i) push_back(i)
#define it(x) vector<x>::iterator x
#define inf 2147483647

char ibuf[BUF];
int ipt = BUF;
int SI()
{
    while(ipt<BUF && ibuf[ipt]<'0')
        ipt++;
    if(ipt==BUF)
    {
        fread(ibuf,1,BUF,stdin);
        ipt=0;
        while(ipt<BUF && ibuf[ipt]<'0')
            ipt++;
    }
    int n=0;
    while(ipt<BUF && ibuf[ipt]>='0')
        n=(n*10)+(ibuf[ipt++]-'0');
    if (ipt==BUF)
    {
        fread(ibuf,1,BUF,stdin);
        ipt=0;
        while(ipt<BUF && ibuf[ipt]>='0')
            n=(n*10)+(ibuf[ipt++]-'0');
    }
    return n;
}

//ll mod=1000000007;

/* code starts here */
int isv(char ch)
{
    if(ch=='a'||ch=='i'||ch=='o'||ch=='u'||ch=='e')
        return 1;
        return 0;
}
void f();

int main()
{
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    
    int testcases,i;
    scanf("%d",&testcases);
    for(i=1;i<=testcases;i++)
      {
          printf("Case #%d: ",i);
          f();
      }
    return 0;
}
void f()
{
   char s[100002];
   int n,i,l,j,k;
  scanf("%s%d",s,&l);
  n=strlen(s);
  int count=0;
  for(i=0;i<n;i++)
    for(j=i;j<n;j++)
    {
        int p=i-1,c;
        for(k=i;k<=j;k++)
        {
            if(isv(s[k])){ c=k; //printf("i=%d c=%d j=%d\n",i,c,j);
            if(c-p-1>=l) { count++;  break;}
            p=c;
            }
            
            if(k==j&&!isv(s[j])) if(j-p>=l) count++;
        }
        
    }

    printf("%d\n",count);

return ;

}
