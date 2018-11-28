
#include <algorithm>

#include <string>
#include <iostream>

#include <fstream>


using namespace std;
int T;
long double C, F, X;

int main()
{

    ifstream cin("C:/B-large.in");
    ofstream cout("C:/response.out");

    cin>>T;
    for(int x=1; x<=T; x++)
    {
        cin>>C>>F>>X;

         long double ans= X/2.0;

           //the method


              long double pretime=0.0;
              long double curtime;

              for(long double i=0; i<=100000.0; i++)
              {
                  pretime += C/(2.0+i*F);
                  curtime=pretime + X/(2.0+((i+1.0)*F));
                  ans= min(ans,curtime);
              }

           cout.setf(ios::fixed,ios::floatfield);
           cout.precision(7);

           cout<<"Case #"<<x<<": "<<ans<<endl;


    }

	return 0;
}
