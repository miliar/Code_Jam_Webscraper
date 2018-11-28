#include <bits/stdc++.h>

using namespace std;

#define MAXN 300000007

bool isPrime[MAXN];
int nonTrivialDivisor[MAXN];

long long checkPrime(long long number){
	if(number < MAXN){
		if(!isPrime[number])
			return nonTrivialDivisor[number];
		else
			return -1;
	}
	else{
		if(number%2 == 0)
			return 2;

		for(long long i=3; i*i<=number; i+=2){
			if(number%i == 0)
				return i;
		}

		return -1;
	}
}

long long convertBase(string number, int base){
	long long ans = 0;
	for(int i=0; i<number.size(); i++){
		ans = ans*base + (number[i] - '0');
	}

	return ans;
}

string to_binary_string(int number, int length){
	string s = "";
	while(number){
		s+= (number%2) + '0';
		number/=2;
	}
	reverse(s.begin(), s.end());
	
	string temp = "";
	for(int i=0; i< length - s.length(); i++){
		temp += "0";
	}
	return temp + s;
}

int main(){
	int T,N;
	cin>>T;

	isPrime[0] = isPrime[1] = false;
	for(int i=2; i<MAXN; i++){
		isPrime[i] = true;
	}

	for(int i=2; i*i<MAXN; i++){
		if(isPrime[i]){
			for(int j=i*i; j<MAXN; j+=i){
				isPrime[j] = false;
				nonTrivialDivisor[j] = i;
			}
		}
	}

	for(int K=1; K<=T; K++){
		int J;
		cin>>N>>J;
		cout<<"Case #"<<K<<": "<<endl;

		int counter = 0;
		long long numGenerate = (1 << (N-2)) - 1;
		for(int i = 0; i<=numGenerate && counter!= J; i++){
			string generated = "1" + to_binary_string(i,N-2) + "1";
			bool jamCoin = true;
			for(int j=2; j<=10 && jamCoin; j++){
				if(checkPrime(convertBase(generated,j)) == -1)
					jamCoin = false;
			}

			if(jamCoin){
				counter++;
				cout<<generated<<" ";
				long long ans;
				for(int j=2; j<10; j++){
					cout<<checkPrime(convertBase(generated, j))<<" ";
				}
				cout<<checkPrime(convertBase(generated,10))<<endl;
			}
		}
	}
	cout<<"Completed"<<endl;

	return 0;
}