#include <iostream>
#include <fstream>
using namespace std;
ifstream f("data.in");
ofstream g("data.out");
int functie(int r,int c,int w)
{
    int a;
    if(w==1)
    {
        return r*c;
    }
    if((r*c)%w==0)
    {
        a=(r*c)/w;
    }
    else
    {
        a=(r*c)/w +1;
    }
    int b=(r*c)%w;
    if (w>r || w>c)
    {
        return a+w-1;
    }
    else
    {
        if (b==w-1)
            return a+w;
        else
            return a+w+1;
    }


}
int main()
{
    int t,r,c,w;
    f>>t;
    for (int i=1;i<=t;i++)
    {
        f>>r>>c>>w;
        g<<"Case #"<<i<<": "<<functie(r,c,w)<<"\n";
    }
    return 0;
}
