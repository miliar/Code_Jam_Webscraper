#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;

ofstream fout ("B-small-attempt0.out");
ifstream fin ("B-small-attempt0.in");
double ans=0;

double proc(double c, double f, double x){
        double newcoin = 2.0;
        ans=0;

         ans += ( x/ newcoin );
        newcoin += f;
        if ( x/newcoin + c/(newcoin-f) > ans )  return ans;
        ans = c/(newcoin-f) ;
         newcoin -= f;
       //  cout<<newcoin<<endl;
    while(1){
        newcoin += f;
        ans += ( c/ newcoin );

        if (  x/ (newcoin +f) > (x/newcoin - c/newcoin) )  break;
    }
    ans = ans - c/newcoin + x/newcoin ;
    return ans ;
}

int main()
{
        int t; fin>>t;
        double ou;
        double c,f,x;
   for(int i=0; i<t; i++){
        fin>>c>>f>>x;
        ou=proc(c,f,x);
 //       cout<<c<<" "<<f<<" "<<x<<endl;
        fout<<"Case #"<<i+1<<": "<<setprecision(9) <<ou<<endl;
   }
    return 0;
}
