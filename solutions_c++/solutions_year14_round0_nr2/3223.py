#include <bits/stdc++.h>
#define _ ios_base::sync_with_stdin(0);cin.tie(0);
using namespace std;
int N; double C,F,X, rate;
int main(){ cin >> N; for(int M=1;M<=N;M++){
	cin >> C >> F >> X;  rate = 2.0; double min = X/rate; double arr[100000]; arr[0] = 0;
	for (int i=1; ;i++)
	{ arr[i]= C/rate+arr[i-1]; rate+= F;  if (min<(X/rate+arr[i])) break; else min = X/rate+arr[i]; }
	cout << "Case #"<< M << ": "; printf("%.7f\n", min);
}return 0;}