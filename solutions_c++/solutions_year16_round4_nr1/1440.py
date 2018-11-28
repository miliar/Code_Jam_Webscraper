#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
#include <cstdlib>
#include <cmath>
#include <queue>
#include <vector>
#include <map>
#define pb push_back
#define mp make_pair
#define eps 1e-9
#define zero(x) (fabs(x)<eps)
#define pi acos(-1.0)
#define f1 first
#define f2 second
#define ms(x,y) memset(x,y,sizeof(x))
#define fr(i,x,y) for(int i=x;i<=y;i++)
using namespace std;
typedef long long ll;
typedef pair <int, int> PII;
template<typename X> inline bool minimize(X&p,X q){if(p<=q)return 0;p=q;return 1;}
template<typename X> inline bool maximize(X&p,X q){if(p>=q)return 0;p=q;return 1;}
#define N 10000
struct node{
    int left,right;
    int now;
}a[N<<1];
int n,m,o;
char ans[N],temp1[N],temp2[N];
void output(int s,int dep)
{
    if (dep==m) {
        if (a[s].now==0)    //printf("%c",'R');
            ans[o++]='R';
        if (a[s].now==1)    //printf("%c",'P');
            ans[o++]='P';
        if (a[s].now==2)    //printf("%c",'S');
            ans[o++]='S';
        return;
    }
    output(a[s].left,dep+1);
    output(a[s].right,dep+1);
}
void doit()
{
    int a1,a2,a3,aa1,aa2,aa3,nn,mm;
    char cc;
    o=0;
    scanf("%d%d%d%d",&n,&a1,&a2,&a3);m=n;
    nn=a1+a2+a3;mm=nn;
    int x=a1,y=a2,z=a3;
    fr(i,nn,nn+nn-1)
    {
        if (y>0) {y--;a[i].now=1;continue;}
        if (z>0) {z--;a[i].now=2;continue;}
        if (x>0) {x--;a[i].now=0;continue;}
    }
    int q1,q2,q3;
    q2=nn;
    q3=nn+a2;
    q1=nn+a2+a3;
    while (n>=1)
    {   if ((a1+a3-a2)%2!=0) {puts("IMPOSSIBLE"); return;}
        x=(a1+a3-a2)/2;
        if (x<0){puts("IMPOSSIBLE"); return;}
        aa1=x;
        aa2=a2-a3+x;
        aa3=a3-x;
        if (aa1>a1||aa1<0){puts("IMPOSSIBLE"); return;}
        if (aa2>a2||aa2<0){puts("IMPOSSIBLE"); return;}
        if (aa3>a3||aa3<0){puts("IMPOSSIBLE"); return;}

//        b[n][0]=aa1;
//        b[n][1]=aa2;
//        b[n][2]=aa3;
        nn/=2;
        x=aa1;y=aa2;z=aa3;
        //printf("@@%d %d %d  %d %d %d\n",q1,q2,q3,aa1,aa2,aa3);
        fr(i,nn,nn+nn-1)
        {


            if (y>0) {y--;a[i].now=1;a[i].left=q2++;a[i].right=q1++;continue;}
            if (z>0) {z--;a[i].now=2;a[i].left=q2++;a[i].right=q3++;continue;}
            if (x>0) {x--;a[i].now=0;a[i].left=q1++;a[i].right=q3++;continue;}

        }
       // fr(i,nn,nn+nn-1)
    //printf("~~~~~~~~~`%d %d %d\n",i,a[i].left,a[i].right);
        q2=nn;
        q3=nn+aa2;
        q1=nn+aa2+aa3;
        //printf("(%d %d %d)->(%d %d %d)\n",a1,a2,a3,aa1,aa2,aa3);
        a1=aa1;
        a2=aa2;
        a3=aa3;
        n--;
    }
    output(1,0);

//fr(i,0,mm-1)printf("%c",ans[i]);puts("~~~~~"); return;
    string s1,s2;
    int cha=1;
    fr(t,1,m)
    {

        //printf("%d %d %c%c%c%c\n",t,cha,ans[0],ans[1],ans[2],ans[3]);
        for(int j=0;j<mm;j+=cha*2)
            {
                strncpy(temp1,ans+j,cha);
                strncpy(temp2,ans+j+cha,cha);
                temp1[cha]='\0';
                temp2[cha]='\0';
                s1=temp1;
                s2=temp2;
                //cout<<s1<<" "<<s2<<" #"<<endl;
                if (s1>s2)
                {


                    //puts("oooooo");
                    for (int k=0;k<cha;k++)
                        {
                            cc=ans[j+k];
                            ans[j+k]=ans[j+cha+k];
                            ans[j+cha+k]=cc;
                        }
                }

            }
        cha<<=1;
    }
    fr(i,0,mm-1)printf("%c",ans[i]);
    puts("");
}

int main()
{
    freopen("aa.in","r",stdin);
    freopen("aa.txt","w",stdout);
    int cas,i=0;
    scanf("%d",&cas);
    while (cas--)
    {   printf("Case #%d: ",++i);

        doit();
    }
}
/*

5
111111
112112
123231
131313
133311
*/
