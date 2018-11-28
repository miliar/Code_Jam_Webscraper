#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>
#include <vector>
#include <algorithm>


using namespace std;
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)

int main ()
{
    int test;
   READ("D-large.in");
    WRITE("D-large.out");

   scanf("%d", &test);
  //  cin >> test;

    int n = 1;
    while (test != 0 )
    {
        long double N;
        cin >> N;
        vector <long double>Naomi(N);
        vector <long double>Ken(N);


        for ( int i=0 ; i < N ; ++i)
        {
            cin >> Naomi[i];
        }

        for ( int i=0 ; i < N ; ++i)
        {
            cin >> Ken[i];
        }


        int WAR =0,DWAR=0;
        sort (Naomi.begin (), Naomi.end());
        sort (Ken.begin (), Ken.end());
        vector <long double> temp = Ken;

        for ( int i=0; i < Naomi.size();++i)
        {
            for ( int j=0; j<temp.size();++j)
                if ( Naomi[i] > temp[j] ) {
                        ++DWAR;
                        temp.erase(temp.begin()+j);
                        break;
                }
        }

        for ( int i=Naomi.size()-1; i >=0;--i)
        {
            for ( int j=Ken.size()-1;j>=0;--j)
            {
                if (Ken[j] > Naomi[i])
                {
                    Ken.erase(Ken.begin()+j);
                    break;

                }

            }
        }

        WAR = Ken.size();

        cout << "Case #" << n << ": " << DWAR << " " << WAR << endl  ;
    ++n;
    --test;
    }


//    file.close();


return 0;
}
