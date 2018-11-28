/*
Mid_Night
C++
*/
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<algorithm>
#include<vector>
#include<iomanip>
#include<math.h>
#include<stack>
#define f0(i,n) for(int i=0;i<=n;i++)
#define fn(i,n) for(int i=n;i>0;i--)
#define f1(i,a,n) for(int i=a;i<=n;i++)
#define f2(i,a,n) for(int i=a;i>=n;i--)

using namespace std;

int main()
{
    ofstream fout ("frac1.out");
    ifstream fin ("frac1.in");
    int t,T,i,j,k,fg;
    double c,f,x,n,n1,n2,r,r1;
    fin>>T;
    for(t=1;t<=T;t++)
    {
        fg=1;n1=0.0;n2=0.0,r1=0.0,n=0.0,r=2.0;
        fin>>c>>f>>x;
        n=x/r;
        while(fg==1)
        {
        n2+=c/r;
        r1=r+f;
        n1=n2+x/r1;
        if(n1>=n)
        {
            fg=0;
        }
        else{
            n=n1;r=r1;
        }
        }
    fout<<"Case #"<<fixed<<setprecision(7)<<t<<": "<<n<<endl;
    }
    return 0;
}
