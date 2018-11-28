#include<fstream>
#include<cstdlib>
using namespace std;
void ordonare(float x[1001],int n)
{
    int i,j;
    float aux;
    for(i=1; i<=n; i++)
        for(j=i+1; j<=n; j++)
        if(x[i]>x[j])
        {
            aux=x[i];
            x[i]=x[j];
            x[j]=aux;
        }
}
int main()
{
    fstream f,g;
    f.open("war.in",ios::in);
    g.open("war.out",ios::out);
    int T,n,k,i,aok[1001]={0},bok[1001]={0},dw,w,ok,j;
    float a[1001],b[1001];
    f>>T;
    for(k=1; k<=T; k++)
    {
        g<<"Case #"<<k<<": ";
        for(i=1; i<=1001; i++)
            aok[i]=bok[i]=0;
        dw=w=0;
        ok=0;
        f>>n;
        for(i=1; i<=n; i++)
            f>>a[i];
        for(i=1; i<=n; i++)
            f>>b[i];
        ordonare(a,n);
        ordonare(b,n);
        for(i=1; i<=n; i++)
        {
            ok=0;
            for(j=1; j<=n && ok==0; j++)
                if(a[i]<b[j] && aok[i]==0 && bok[j]==0)
                {
                    w++;
                    ok=1;
                    aok[i]=1;
                    bok[j]=1;
                }
        }
        for(i=1; i<=1001; i++)
            aok[i]=bok[i]=0;

        for(i=1; i<=n; i++)
        {
            ok=0;
            for(j=1; j<=n && ok==0; j++)
                if(a[i]>b[j] && aok[i]==0 && bok[j]==0)
                {
                    dw++;
                    ok=1;
                    aok[i]=1;
                    bok[j]=1;
                }
        }


        g<<dw<<" "<<n-w<<'\n';
    }
}
