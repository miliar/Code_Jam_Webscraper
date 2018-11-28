#include <iostream>
#include <cstdio>
#include <vector>
#include <map>
#include<cmath>
#include <sstream>
#include <algorithm>
#include <iomanip>
using namespace std;


int  main()
{
    freopen("B-large.in",  "r", stdin);
    freopen("Blarge.out",  "w", stdout);

    int t;
    cin>>t;
    for(int i=1; i<=t; i++)
    {
        double c,f,x,p=2,result=0;
        cin>>c>>f>>x;

          while(true)
        {
            double ansA = x/p;
            double ansB = (c / p)+( x/(f+p) );

            if(ansB < ansA )
            {
                result+=(c/p);
                p+=f;
            }
            else
            {
                result+=x/p;
                break;
            }
        }
        cout<<"Case #"<<i<<": "<<fixed<< std::setprecision(7) << result<<endl;
    }

    return 0;
}
