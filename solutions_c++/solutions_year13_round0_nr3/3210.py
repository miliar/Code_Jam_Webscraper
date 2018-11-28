# include <iostream>
# include <string>
# include <map>
# include <fstream>
using namespace std;

ifstream fin ("C-small-attempt0.in");
ofstream fout ("C-small-attempt0.out");


int Isqrt(int num){
    if (0 == num) { return 0; }  // Avoid zero divide
    int n = (num / 2) + 1;       // Initial estimate, never low
    int n1 = (n + (num / n)) / 2;
    while (n1 < n)
    {
        n = n1;
        n1 = (n + (num / n)) / 2;
    } // end while
    return n;
} // end Isqrt()


bool IsPerfectSquare(int num){
    return Isqrt(num) * Isqrt(num) == num;
}

bool isPal (int num){
	int rev=0;
	int x = num;
	while (x > 0){
		int d = x%10;
		rev = rev*10 + d;
		x /= 10;
	}
	return (num == rev);
}

int main (){
	
	int T;
	fin >> T;

	for (int i=0;i<T;i++){
		int A,B;
		fin >> A >> B;
		int cnt = 0;
		for (;A<=B;A++){
			if (IsPerfectSquare(A))
				if (isPal(A) && isPal(Isqrt(A)))
					cnt ++;
		}
		fout << "Case #" << i+1 << ": " << cnt << endl;
	}
}