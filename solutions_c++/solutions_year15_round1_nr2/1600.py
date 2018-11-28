using namespace std;
#include <iostream>
#include <numeric>



int gcd(int a, int b)
{
    for (;;)
    {
	if (a == 0) return b;
	b %= a;
	if (b == 0) return a;
	a %= b;
    }
}

int lcm(int a, int b)
{
    int temp = gcd(a, b);

    return temp ? (a / temp * b) : 0;
}

int main(){
	
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++){
		
		int B; int N;
		cin >> B >> N;
		int * M = new int[B];
		int * b = new int[B];
		for (int k = 0; k < B; k++) cin >> M[k];
		
		int lll = 1;
		for (int k = 0; k < B; k++) lll = lcm(lll, M[k]);

		int div = 0;
		for (int k = 0; k < B; k++) div += lll / M[k];
		N = ((N-1) % (div)+1);
		if (N > 0){
			int min;
			for (int i = 0; i < N; i++){
				min = 0;
				for (int k = 1; k < B; k++){
					if (b[k] < b[min]) min = k;
				}
				b[min] += M[min];
			}
			cout << "Case #" << t << ": " << min+1 << endl;
		} else {
			cout << "Case #" << t << ": 1" << endl;
		}
	}
	
}
