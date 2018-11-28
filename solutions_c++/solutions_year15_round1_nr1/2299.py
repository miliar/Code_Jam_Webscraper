#include <bits\stdc++.h>
//#define in cin
//#define out cout
using namespace std;

int main()
{
   fstream in("A-large.in",ios::in);
   fstream out("out.out",ios::out);
   int64_t t , n,sum1 = 0 , sum2 = 0 , diff , tmp; in >> t;
   int64_t arr[1005];
   for(int64_t q = 0; q < t; q++)
   {
       in >>n;
       sum1 =  0;
       sum2 = 0;
       diff = 0;
       for(int64_t i = 0; i < n; i ++){
        in >> arr[i];
       }
       bool ok = false;
       for(int64_t i = 0; i < n-1; i++)
       {
           if(arr[i+1] < arr[i]){
            sum1 += arr[i]-arr[i+1];
            diff = max(diff , abs(arr[i+1]-arr[i]));
           }
       }
       tmp = diff;
       int64_t u = arr[0];
       for(int i = 0; i < n-1; i++)
       {
           sum2 += min(tmp , arr[i]);
       }
       out << "Case #" << q+1 << ": " << sum1 << ' ' << sum2 << '\n';
   }
}
