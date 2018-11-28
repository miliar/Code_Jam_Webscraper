#include <iostream>
#include <vector>
#include <utility>
#include <cmath>

using namespace std;

long long changeBase(const std::vector<bool>&, const int);
long long getDivisor (const long long);
pair<vector<bool>, long long> getBinary (long long);
vector<long long> checkJamCoin(const long long);

long long changeBase(const std::vector<bool>& v, const int b) {
	long long n=0;
	for (int i=0; i<(int)v.size(); i++){
		n += v[i]*pow(b,i);
	}
	return n;
}

long long getDivisor (const long long n){
	for (long long i=2; i *i <= n; i++)
		if (n%i==0)
		{
			return i;
		}
	return 0;
}

pair<vector<bool>, long long> getBinary (long long n) {
	std::vector<bool> v;
	long long k=0, i=0;
	while (n>0) {
		v.push_back(n%2);
		k += (n%2)*pow(10,i);
		n /= 2;
		i++;
	}
	return make_pair(v,k);
}

vector<long long> checkJamCoin(const long long n) {
	vector<bool> bin;
	vector<long long> jamCoin;
	pair<vector<bool>, long long> p;
	p = getBinary(n);
	bin = p.first;
	// cout << p.second << endl;
	jamCoin.push_back(p.second);
	for (int b=2; b<=10; b++){
		long long baseChanged, divisor;
		baseChanged = changeBase(bin, b);
		// cout << "based " << b << " " << n << " "<< baseChanged << endl;
		divisor = getDivisor(baseChanged);
		if (divisor == 0) {
			// cout << divisor << baseChanged;
			jamCoin.clear();
			return jamCoin;
		}
		else
			jamCoin.push_back(divisor);
	}
	return jamCoin;
}

int main()
{
	int N;
    cin >> N;
    for (int iter=1; iter<=N; iter++){
    	int n, J, j=0;
    	cin >> n;
    	cin >> J;
    	// cout << n << J << endl;
    	cout << "Case #" << iter << ":" << endl;
    	// cout << pow(2,(n-1)+1) << endl;
    	for (long long i=pow(2,(n-1))+1; (i<pow(2,n) && j<J); i+=2){
    		std::vector<long long> v;
    		// cout << i << endl;
    		v = checkJamCoin(i);
    		if (!v.empty()) {
    			j++; //cout << j << endl;
    			for (auto& x : v) {
    				cout << x << " ";
    			}
    			cout << endl;
    		}
    	}
    }
	return 0;
}