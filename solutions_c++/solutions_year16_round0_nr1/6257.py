#include <iostream>
#include <fstream>

using namespace std;
long long diez[14]={1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000,10000000000,100000000000,1000000000000,10000000000000};
/*long long diez(int n)
{
    int i,ret=1;
    for(i=1;i<=n;i++)
    {
        ret*=10;
    }
    return ret;
}*/
int calc(int n)
{
int64_t i,diji[11],k,dies,h,m,j,a=1,pix,sali,f;
for(i=0;i<=9;i++)
{
    diji[i]=0;
}
j=1;
while((a==1))
{
    m=n*j;

dies=1;
k=0;
do
{
    dies*=10;
    k++;
    h=m%dies;
}while(h!=m);
    for(i=1;i<=k;i++)
    {
       pix=m%diez[i];
       f=diez[i-1];
       pix=pix/(f);
       diji[pix]=1;
    }

    pix=1;
    for(i=0;i<=9;i++)
    {
        if(diji[i]==0)
        {
            pix=0;
        }
    }
    if(pix==1)
    {
        a=0;
        sali=m;

    }
 j++;
}
return sali;
}



int main()
{
    ifstream in("A-large.in");
    ofstream out("salida.out");
    long long t,n,i,salida[100000];

  /*  for(i=1;i<=100000;i++)
    {
        salida[i]=-1;
    }*/
    /*for(i=1;i<=100000;i++)
    {
        salida[i]=calc(i);
    }*/

in>>t;
for(i=1;i<=t;i++)
{
    in>>n;
    if(n==0)
    {
        out<<"Case #"<<i<<": INSOMNIA"<<endl;
    }
    else
    {
    out<<"Case #"<<i<<": "<<calc(n)<<endl;
    }
}
    in.close();
    out.close();
    return 0;
}
