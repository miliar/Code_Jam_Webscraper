#include<iostream>
#include<vector>
#include<cmath>
#include<bitset>
using namespace std;
typedef long long ll;
vector<int> primes{2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97};
ll bb[15];


ll pp (ll n, ll len){
	if (len ==1) return n;
	if (len == 0) return 1;
	ll res = pp(n,len/2);
	if (len%2 ==0) return res*res;
	return res*res*n;
}
void addB(int len){
	for(int i = 2; i <=10; i++){
		bb[i] = pp(i, len-1);
	}
}
ll conver(ll num, ll base){
	ll res= bb[base];
	ll po = 0; 
	while(num){
		int x = num%2;
		if(x) {
			res += pp(base,po);
		}
		po++;
		num = num >>1;
	}
	return res;
}

int cP(ll num){
	int res = -1;
	for(auto v :primes){
		if ((num %v) ==0) {
			res = v; break;
		}
	}
	return res;
}
int main(){
	int ts; cin>>ts;
	int tt = 1;
	while(ts--){
		int n, j; cin>>n >>j;
		int res = 0;
		addB(n);
		vector<int> op;
		cout << "Case #" << tt++ << ":\n";
		for(int i = 1; i < ((1<<(n-1)) -1); i+=2){
			bool check = true;
			op.clear();
			if (res == j) break;
			for(int j = 2; j<=10; j++){
				ll cb = conver(i,j);
				//cerr << cb << "\n";
				int ress = cP(cb);
				if (ress == -1) {
					check = false;
					break;
				}
				op.push_back(ress);

			}
			if (check){
				res++;
				ll tm = (1<<(n-1));
				tm +=i;
				cout << bitset<16>(tm) << " ";
				for (auto v: op){
					cout << v  << " "; 
				}
				cout << "\n";
			}
		}
	}
}
