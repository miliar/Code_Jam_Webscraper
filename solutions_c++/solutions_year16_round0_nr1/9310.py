#include <fstream>

using namespace std;
ifstream f("countingsheep.in");
ofstream g("countingsheep.out");
unsigned long long v[10],nr,c,i,t,pas,x,cnt,ok,ig,j;
void extractCifre(int nr)
{
    while(nr)
    {
        c=nr%10;
        nr=nr/10;
        v[c]++;
    }

}
int main()
{
    f>>t;
    for(j=1;j<=t;j++)
    {
        f>>nr; //incepe testul pt nr
        ig=0;
        if (nr==0) {g<<"Case #"<<j<<": "<<"INSOMNIA"<<'\n'; ig = 1;}
        pas=1;
        ok=0;
        while(ok==0 && ig==0)
        {
            x=nr*pas;
            extractCifre(x);
            cnt=0;
            for(i=0;i<=9;i++)
                {
                    if (v[i]>0) cnt++;
                }
            if (cnt==10) ok=1;
                else
                {
                    pas++;
                }
        }
    if(ig==0)
        g<<"Case #"<<j<<": "<<x<<'\n';
    for(i=0;i<=9;i++)
        {
            v[i]=0;
        }
    }
    return 0;
}
