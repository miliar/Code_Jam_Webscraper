#include<stdio.h>
#include<string.h>
#include<vector>
#include<algorithm>
#define tr(c,it) for( vector<int>::iterator it=c.begin();it!=c.begin()+siz;it++)
using namespace std;
char s[2002];
int c[30];
vector<int> a;
int siz;
void rm(char b[])
{
 //   printf("%s\n",b);
    int i,j,k,l=strlen(b);
    for(i=0;i<l;i++)
    {
        for(j=0;j<siz;j++)
        {
            if(a[j]==(b[i]-'A'))
            {
                for(k=j;k<siz-1;k++)
                {
                    a[k]=a[k+1];
                }
                siz--;
                break;
            }
        }
    }
}
int main()
{
 //   freopen("input2.in","r",stdin);
   // freopen("output2.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int l=0;
    while(l<t)
    {   l++;
        scanf("%s",s);
        int i,j;
        for(i=0;i<30;i++) c[i]=0;
        int n=strlen(s);
        siz=n;

        for(i=0;i<n;i++)
        {
            a.push_back(s[i]-'A');
   //         printf("%d",a[i]);
        }
        while(siz!=0){
        while(find(a.begin(),a.end(),'Z'-'A')-a.begin()<siz)
        {
            c[0]++;
            rm("ZERO");
        }
        while(find(a.begin(),a.end(),'W'-'A')-a.begin()<siz)
        {
            c[2]++;
            rm("TWO");
        }
        while(find(a.begin(),a.end(),'U'-'A')-a.begin()<siz)
        {
            c[4]++;
            rm("FOUR");
        }
        while(find(a.begin(),a.end(),'X'-'A')-a.begin()<siz)
        {
            c[6]++;
            rm("SIX");
        }
            while(find(a.begin(),a.end(),'R'-'A')-a.begin()<siz)
        {   c[3]++;
            rm("THREE");
        }
        while(find(a.begin(),a.end(),'S'-'A')-a.begin()<siz)
        {
            c[7]++;
            rm("SEVEN");
        }
        while(find(a.begin(),a.end(),'V'-'A')-a.begin()<siz)
        {
            c[5]++;
            rm("FIVE");
        }
        while(find(a.begin(),a.end(),'T'-'A')-a.begin()<siz)
        {
            c[8]++;
            rm("EIGHT");
        }
        while(find(a.begin(),a.end(),'I'-'A')-a.begin()<siz)
        {
            c[9]++;
            rm("NINE");
        }
        while(find(a.begin(),a.end(),'O'-'A')-a.begin()<siz)
        {
            c[1]++;
            rm("ONE");
        }}
   //       tr(a,it)
     //   printf("%d ",*it);
     printf("Case #%d: ",l);
        for(i=0;i<30;i++)
        {
            while(c[i]--) printf("%d",i);
        }
        printf("\n");
        a.clear();
    }
    return 0;
}
