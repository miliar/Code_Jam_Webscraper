#include<iostream>
#include<iomanip>
using namespace std;

long double eval(long double C, long double F, long double X)
{
   long double sum = 0.0, rate = 2.0;
   while((X / rate) > ((C / rate) + (X / (rate + F))))
   {
      sum += C / rate;
      rate += F;
   }

   return (sum + (X / rate));
}
int main()
{
   int T;
   cin >> T;
   long double C[T], F[T], X[T];
   long double op[T];
   for(int i = 0; i < T; i ++)
   {
      cin >> C[i] >> F[i] >> X[i];
      op[i] = eval(C[i], F[i], X[i]);
   }

   for(int i = 0; i < T; i ++)
      cout << "Case #" << i + 1 << ": " << fixed << showpoint << setprecision(7)<< op[i] << endl;
   return 0;

}
