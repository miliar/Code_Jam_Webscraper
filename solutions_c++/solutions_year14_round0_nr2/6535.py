#include<iostream>
#include<fstream>
#include<iomanip>

#define TEST 1

#ifdef TEST
#define CIN in
#define COUT out
#else
#define CIN cin
#define COUT cout
#endif
using namespace std;
int main(){
int t;
double c,f,x,rate=2,curr=0,time=0;
#ifdef TEST
fstream in("binp.txt"),out("bout.txt");
#endif
CIN>>t;
int caseno=1;
while(t--)
{
    CIN>>c>>f>>x;
    rate=2;curr=0;time=0;
    COUT.precision(10) ;
    if(c>x){time=(double)x/2;}
    else
    while(curr<x)
    {
        if(curr<c){
            time+=(double)(c-curr)/rate;
            curr=c;
        }
        if(x<=curr)break;
        if((x-curr)/rate > ((x-(curr-c))/(rate+f)))
        {
            rate+=f;
            curr-=c;
        }
        else {
            time+=(double)(x-curr)/rate;
            curr=x;
        }
    }
    COUT<<"Case #"<<caseno<<": ";
    COUT<<setprecision(10)<<time;
    caseno++;
    COUT<<endl;
}
}
