#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>
#include <algorithm>

#define rep(x,y,z,t) for (int x=y; x<=z;x+=t)
#define req(x,y,z,t) for (int x=y; x>=z;x-=t)

#define min(a,b) ((a<b)? (a):(b))
#define max(a,b) ((a>b)? (a):(b))
#define abs(a) ((a>0) ? (a):((-1)*a))
using namespace std;

    //#define TEST
    #ifndef TEST
    ifstream fin("input.in");
    ofstream fout("output.out");
    #else
    #define fin cin
    #define fout cout
    #endif // TEST


    #define inf 1000000001    //10^9+1


int n;
string s;

    void write(int x, int y)
    {
        fout<<"Case #"<<x<<": "<<y<<"\n";


    }
int t,k,p,x;
char c;
    void read()
    {
        fin>>p;
        rep(i,1,p,1)
        {
            fin>>n;
            k=0;
            //fin>>c;
            fin>>c;
            t=c-'0';
            rep(j,1,n,1)
            {
                fin>>c;
                x=c-'0';
                if (x && k+t<j) k=j-t;
                t+=x;
            }
            write(i,k);

    }
    }
int main()
{
    read();



}
