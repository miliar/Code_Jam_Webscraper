#include "../jam.h"

typedef unsigned long long ull;

bool isPal(ull num)
{
   ull n = num;
   ull rev = 0;
   while(n > 0)
   {
       int dig = n % 10;
       n = n / 10;
       rev = rev * 10 + dig;
   }
   return (rev == num);
}


void solve(int casenum) {
   int ans = 0;
   ull A, B;
   in >> A >> B;
   ull n1 = int(sqrt(A));
   ull n2 = int(sqrt(B)) + 1;

   for(int i = n1; i <= n2; i++)
   {
       if(!isPal(i)) continue;

       ull n = i*i;
       if(!isPal(n) || n < A || n > B) continue;
       else ans++;
   }

   out << "Case #" << casenum << ": " << ans << endl;
}




int main() {
	cout << "!!!Hello World!!!" << endl;

	in.open("C-small-attempt0.in");
	out.open("output.txt");
	int T;
	in >> T;
	for (int i=0;i<T;i++) {
        solve(i+1);
    }    
    system ("pause");
	return 0;
}
