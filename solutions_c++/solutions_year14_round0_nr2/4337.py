#include <iostream>
#include<iomanip>
using namespace std;

int main()
{
   int T, testcase=1;
   double C,F,X;
   int j;
   int R;
   double sum=0.0, prev=0.0;

   cin >> T;
   do
   {

       cin >> C >> F>> X;
       R=0;
       do
       {
        prev = sum;
        sum = 0.0;
        if(R==0)
        {
            sum = X/2;
            prev = sum;
        }
        else
        {

            for(j=1;j<=R;j++)
            {
                sum += C/(2+(j-1)*F);
            }
            sum += X/(2+R*F);
        }
        R++;
        //cout<< std::fixed << setprecision(7) << sum << endl;
       }while(sum<=prev);
       cout <<"Case #"<<testcase<<": ";
       cout<< std::fixed << setprecision(7) << prev << endl;

       testcase++;
   }while(testcase<=T);
}
