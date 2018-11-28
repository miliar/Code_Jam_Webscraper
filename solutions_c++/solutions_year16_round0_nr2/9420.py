#include <fstream>
#include <string.h>
using namespace std;
ifstream f("pancakes.in");
ofstream g("pancakes.out");
char line[110],ch;
int v[110],i,ok,cnt,tstt,x,sw,step,n,j;
bool test(int x)
{
    for(i=0;i<x;i++)
    {
        if (v[i]==0) return 0;
    }
    return 1; //returns 0 if not well flipped. 1 if job done
}
int main()
{
    f>>n;
    f.getline(line,110);
    for(j=1;j<=n;j++)
    {
    f.getline(line,110);
    step=0;
    ch=line[0];
    i=0;
    //turn -+ into 01
    while(ch!='\000')
    {
        ch=line[i];
        if(ch=='+')
            v[i]=1;
            else
            v[i]=0;
        i++;
    }
    v[i-1]=5; //mark end
    // + test
    x=i-1;
    sw=0;
    do {
     if (test(x)==1) {sw=1; break;}
    i=1;
    ok=0;
    tstt=v[0];
    cnt=0;
    while (ok==0)
    {
        cnt++;
        if(v[i]!=tstt) ok=1;
        i++;
    }
    //flipping
    for(i=0;i<cnt;i++)
        if (v[i]==1) v[i]=0;
            else v[i]=1;
    step++;

    } while (sw==0);
    g<<"Case #"<<j<<": "<<step<<'\n';
    }
    return 0;
}
