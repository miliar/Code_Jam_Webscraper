#include<iostream>
#include<fstream>
#include<stdlib.h>
using namespace std;
ifstream fin;
ofstream fout;
void deal(int);

const long long modulo=1000002013;
const int maxn=4000;

struct station
{
    long long pos,on,off;
};

station a[maxn];
station s[maxn];

long long n,m,top;

long long fee(long long o,long long e,long long p)
{
//    cout<<o<<' '<<e<<' '<<p<<endl;
    long long d=e-o;
    return (-d*d+(2*n+1)*d)/2*p;
}
    
bool compair(station a,station b)
{
    if (a.pos == b.pos)
        return a.on>b.on;
    else return a.pos<b.pos;
}


int main()
{
    fin.open("gcj2013_2_A.in");
    fout.open("gcj2013_2_A.out");
    int t;
    fin>>t;
    for (int i=0;i<t;i++)
        deal(i);
}


void deal(int p)
{
    fin>>n>>m;
    long long sum0=0,sum=0,top=-1;
    for (int i=0;i<m;i++)
    {
        long long e,o,p;
        fin>>o>>e>>p;
        a[i*2].pos=o;
        a[i*2].on=p;
        a[i*2].off=0;
        a[i*2+1].pos=e;
        a[i*2+1].on=0;
        a[i*2+1].off=p;
        sum0=(sum0+fee(o,e,p))%modulo;
    }
    sort(a,a+m*2,compair);
 //   cout<<sum0<<endl;
//    for (int i=0;i<m*2;i++)
//        cout<<a[i].pos<<' '<<a[i].on<<' '<<a[i].off<<endl;
    for (int i=0;i<m*2;i++)
    {
//        cout<<s[top].pos<<' '<<s[top].on<<endl;
        if (a[i].on>0)
        {
            top++;
            s[top]=a[i];
        }
        else
        {
            while (a[i].off>0)
            {
//                cout<<top<<' '<<s[top].pos<<' '<<s[top].on<<endl;
                if (s[top].on>=a[i].off)
                {
                    sum=(sum+fee(s[top].pos,a[i].pos,a[i].off))%modulo;
                    s[top].on-=a[i].off;
                    a[i].off=0;
                }
                else
                {
                    sum=(sum+fee(s[top].pos,a[i].pos,s[top].on))%modulo;
                    a[i].off-=s[top].on;
                    top--;
                }
            }
        }
    }
 //   cout<<sum<<endl;
    fout<<"Case #"<<p+1<<": "<<(sum0-sum+modulo)%modulo<<endl;
   // system("pause");
}
