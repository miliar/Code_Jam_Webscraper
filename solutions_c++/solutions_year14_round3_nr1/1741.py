#include <iostream>
#include <math.h>
using namespace std;

int ispow(int n){
	double x = log(n)/log(2);
	int y = x;
	if(x == (double)y) return 1;
	else return 0;
}

int gcd(int u, int v) {
return (v != 0)?gcd(v, u%v):u;
}

int main(int argc, char const *argv[])
{
	int T, P, Q, count, mygcd;
	cin >> T;
	for (int i = 0; i < T; ++i)
	{
		scanf("%d/%d", &P, &Q);
		count = 1;

		cout << "Case #" << i+1 << ": ";
		mygcd = gcd(P,Q);
		P/=mygcd;
		Q/=mygcd;

		if(!ispow(Q)) {
			cout << "impossible";
		}
		else{
			while(P*2 < Q){
				Q /= 2;
				count++;
			}
			cout << count;
		}
		cout << endl;
	}
	return 0;
}