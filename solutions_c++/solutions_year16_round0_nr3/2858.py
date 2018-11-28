#include<bits/stdc++.h>
using namespace std;

long long get_num_base(long long num, long long base){
	long long result = 0;
	long long pot = 1;
	long long i = 0;
	while(num > 0){
		if(num & 1){
			result+=pot;
		}
		pot*=base;
		num>>=1;
	}
	return result;
}

bool isprime(long long n){
	for(long long i=2; i*i<=n; i++){
		if(n%i == 0){
			return false;
		}
	}
	return true;
}

string isbinary(long long x){
	string str="";
	while(x>0){
		if(x&1)str+='1';
		else str+='0';
		x>>=1;
	}
	reverse(str.begin(),str.end());
	return str;
}
		
int main() {
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	long long testes;
	cin>>testes;
	int cases=1;
	while(testes-->0) {
		int N, J;
		cin>>N>>J;
		vector<long long> numbers;
		for(long long i=(1LL << (N-1)) + 1; i<(1LL << N) && numbers.size()<J; i+=2){
			bool primo=false;
			for(int j=2; j<=10; j++){
				if(isprime(get_num_base(i,j))){
					primo=true;
					break;
				}
			}
			if(!primo){
				numbers.push_back(i);
			}
		}
		printf("Case #%d:\n", cases++);
		for(int k=0; k<numbers.size(); k++){
			long long num=numbers[k];
			cout << isbinary(num);
			for(int i=2; i<=10; i++){
				long long cur_num=get_num_base(num,i);
				for(long long j=2; j*j<=cur_num; j++){
					if(cur_num%j == 0){
						cout<<" "<<j;
						break;
					}
				}
			}
			cout<<endl;
		}
		cout<<endl;
	}
	return 0;
}
