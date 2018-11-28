#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

#define f(i,N) for(int i = 0; i != N; i++)
#define fl(i,N) for(int i = 1; i <= N; i++)
#define pb(x) push_back(x)
#define s(A) sort(A.begin(),A.end)

using namespace std;
typedef vector<int> vi;
long long int X = 9999999999;
long long int N;
vector <bool> V(1000000);
vi A(1000000);
long long int fun(long int i) {
	if(i == N)
		return 1;
	if(i > N)
		return X;
	if(V[i])
		return A[i];
	else
		V[i] = true;
	long int temp = i;
	long int R=0;
	while(temp > 0) {
		R=10*R+temp%10;
		temp/=10;
	}
	if(R<=i)
		A[i] = fun(i+1)+1;
	else
		A[i] = min(fun(i+1),fun(R))+1;
	return A[i];
}

int main() {
	int T;
	cin >> T;
	fl(i,T) {
		cin >> N;
		f(j,N)
			V[j] = false;
		long long int U = fun(1);
		cout << "Case #"<< i << ": " << U << endl;
	}
	return 0;
}
