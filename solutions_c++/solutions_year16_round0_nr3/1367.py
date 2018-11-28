#include <bits/stdc++.h>
using namespace std;

long long factor(long long n){
	long long rt=sqrt(n), i;
	for(i=2;i<=min(rt, (long long)1000001);i++){
		if(n%i==0) return i;
	}
	return 1;
}

long long convert(string s, long long b){
	long long ans=0, t=1, i;
	for(i=s.size()-1;i>=0;i--){
		if(s[i]=='1') ans += t;
		t *= b;
	}
	return ans;
}

int main(){
	ios_base::sync_with_stdio(0);
	cin.tie(0);
	
	long long i, t, x, f, j, T, cas, total, N, J;
	string s, init;
	vector<long long> arr;
	
	cin >> T;	
	for(cas=1;cas<=T;cas++){
		cin >> N >> J;
		
		init.push_back('1');
		for(i=1;i<N-1;i++) init.push_back('0');
		init.push_back('1');
		
		cout << "Case #" << cas << ":\n";
		total=0;
		
		for(i=0;i<pow(2, N-2) and total<J;i++){
			s=init;
			t = i;
			for(j=N-2;j>0;j--){
				if(t%2){
					s[j] = '1';
				}
				t /= 2;
			}
			f=1;
			for(j=2;j<11;j++){
				t = convert(s, j);
				x = factor(t);
				if(x==1){
					f=0;
					break;
				}
				else arr.push_back(x);
			}
			if(f){
				cout << s << ' ';
				for(j=0;j<arr.size();j++) cout << arr[j] << ' ';
				cout << '\n';
				total++;
			}
			arr.clear();
		}
	}
	return 0;
}
