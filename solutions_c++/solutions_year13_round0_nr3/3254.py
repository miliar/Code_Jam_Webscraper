#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

ifstream in("smallC.in");
ofstream out("smallC.out");

bool Polindrom(long long N)
{
   long long copyN = N;
   long long newN = 0;
   while (N > 0)
   {
      newN = newN*10 + N % 10;
      N /= 10;
   }
   return newN == copyN;
}

long long Solve(long long N)
{
   long long answer = 0;
   for (long long i = 1; i*i <= N; ++i)   
      if (Polindrom(i) && Polindrom(i*i))
         answer++;
   return answer;
}

int main()
{
   int test;
   in >> test;   
   for (int t = 1; t <= test; ++t)
   {      
      long long A, B;
      in >> A >> B;
      int answer = Solve(B) - Solve(A - 1);
      out << "Case #" << t << ": " << answer << endl;
   }  

   return 0;
}




