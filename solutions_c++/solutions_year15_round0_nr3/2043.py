#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
using namespace std;
int casenum;
char s[10005];
int x[10005];
int xx[10005];
int y[80005];
int yy[80005];
int chang,ci;

void clean(void)
{
    for(int i=1;i<=chang+1;i++) xx[i]=x[i];
}

int m[5][5];

void init(void)
{
    memset(m,0,sizeof(m));
    m[1][1]=1;
    m[1][2]=2;
    m[1][3]=3;
    m[1][4]=4;
    m[2][1]=2;
    m[2][2]=-1;
    m[2][3]=4;
    m[2][4]=-3;
    m[3][1]=3;
    m[3][2]=-4;
    m[3][3]=-1;
    m[3][4]=2;
    m[4][1]=4;
    m[4][2]=3;
    m[4][3]=-2;
    m[4][4]=-1;
}

int mult(int aa,int bb)
{
    if(aa*bb<0) return -1*m[abs(aa)][abs(bb)];
    else return m[abs(aa)][abs(bb)];
}


int func(void)
{
    clean();
    for(int i=1;i<=chang;i++)
    {
        xx[i]=mult(xx[i-1],x[i]);
    }
    return xx[chang];
}




int main(void)
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("C-small-attempt1.out","w",stdout);
    init();
    scanf("%d",&casenum);
    for(int k=1;k<=casenum;k++)
    {
       scanf("%d %d",&chang,&ci);
       scanf("%s",s+1);
       for(int i=1;i<=chang;i++)
       {
           if(s[i]=='i') x[i]=2;
           else if(s[i]=='j') x[i]=3;
           else x[i]=4;
       }
       x[0]=x[chang+1]=1;


       //int zuida=min(8,ci);
       int pos=1;
       for(int i=1;i<=ci;i++)
       {
           for(int j=1;j<=chang;j++)
           {
               y[pos]=x[j];pos++;
           }
       }

       int first=-1,third=-1;

       y[0]=y[ci*chang+1]=1;


       for(int i=0;i<=chang*ci+1;i++)
       {
           yy[i]=y[i];

       }
       //printf("\nsasadasdasdasdasda\n");

       for(int i=1;i<=chang*ci;i++)
       {
          // printf("%d %d\n",yy[i-1],y[i]);
           yy[i]=mult(yy[i-1],y[i]);
           if(yy[i]==2) {first=i;break;}
       }

       for(int i=chang*ci;i>=1;i--)
       {
           yy[i]=mult(y[i],yy[i+1]);
           if(yy[i]==4) {third=i;break;}
       }

       //printf("%d %d\n",first,third);

       if(first==-1||third==-1||first>=third||first+1==third) printf("Case #%d: NO\n",k);

       else{
           yy[first]=1;
           for(int i=first+1;i<third;i++)
              yy[i]=mult(yy[i-1],y[i]);
           if(yy[third-1]==3)  printf("Case #%d: YES\n",k);
           else printf("Case #%d: NO\n",k);

       }


    }
    return 0;
}
