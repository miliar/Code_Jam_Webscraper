#include <iostream>
#include <cmath>
#include <vector>
#include <fstream>

using namespace std;

vector<long int> interval;

bool square(long int nbr)
{
    bool rp=false;
     long double c=sqrt(nbr);
    long int d=c;
   long double  e= c-d;
    if(e==0) rp=true;
   return rp;
}

bool pal(long int a)
{

    bool rp= false;
    if(a<10) rp= true;
bool tmp=false;
if(a>=10 && a<100)
{
    int b= a%10;
    int c= a/10;
    if(b==c) tmp=true;
    }
if(tmp) rp= true;
bool cent= false;
if(a>=100 && a<1000)
{
    int b= a%10;
    int c= a/100;
    if(b==c) cent=true;
    }
    if(cent) rp=true;
   bool mil= false;
if (a=1000) mil= false;
if(mil) rp= true;
return rp;
}


int main()
{
    ifstream fin("C:/C-small-attempt0.in.txt");
    ofstream fout("C:/response.out");
    int n;
    fin>>n;
    for(int k=1; k<=n; k++)
    {
        int result=0;
        long int a,b;
        fin>>a>>b;
        for(long int i=a; i<=b; i++)
        {
            bool car=false;
            bool rp=false;
            bool res=false;

            car=square(i);
            if(car) {
            long int nbr= sqrt(i);
            rp=pal(nbr);
            }
            res=pal(i);

            if(res==true && rp==true) result++;
        }
        fout<<"Case #"<<k<<": "<<result<<endl;
    }

    return 0;
}
