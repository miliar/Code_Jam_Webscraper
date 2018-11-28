#include <iostream>
#include <cmath>
#include <vector>
using namespace std;

bool Primal[100000];

void fillP(void){

	Primal[1] = 0;
	for(int i=2;i<100000;i++)
		Primal[i] = true;

	for(int i=2;i<100000;i++){
		if(!Primal[i])
			continue;

		int j = 2;
		while(i*j<100000){
			Primal[i*j] = false;
			j++;
		}
	}
}

long long int D[40];

void fillB(int i,int n){
	for(int j=0;j<n-2;j++){
		D[j] = i%2;
		i/=2;
	}
}

long long int power(long long int j,long long int k,long long int d)
{
	long long int s = 1;
	for(int i = 0;i<k;i++)
		s = (s*j)%d;
	return s;
}


long long int calrem(long long int b,long long int n,long long int d)
{
	long long int c = 0;
	c = (c + power(b,n-1,d) + 1)%d;

	for(int i=0;i<n-2;i++)
	{
		c = (c + (D[i]*power(b,i+1,d))%d)%d;
	}
	return c;
}

void countCoins(int n,vector<long long int> V,int J){
	int count = 0;
	for(long long i=2;i<pow(2,n-2);i++){
		fillB(i,n);
		long long num;
		bool  flag = true;
		vector<int> divisors;
		for(long long int j=2;j<=10;j++){
			int ch = 0;
			for(int l=0;l<30;l++){
				int rem  = calrem(j,n,V[l]);
				if(rem)
					ch++;
				else{
					divisors.push_back(V[l]);
					break;
				}
			}
			if(ch==30){
				flag = false;
				break;
			}
		}
		if(flag)
		{
			cout << "1";
			for(int k=n-3;k>=0;k--)
				cout << D[k];
			cout << "1 ";
			for(int s=0;s<divisors.size();s++)
				cout << divisors[s] << " ";
			cout << endl;
			count++;
		}
		if(count==J)
			break;
	}
}


int main()
{
	fillP();

	vector< long long int> primes;
	for(int i=2;i<100000;i++){
		if(Primal[i])
			primes.push_back(i);
	}

	long long int N,J;
	int T;

	cin >> T;
	int I = T;

	while(T--)
	{
		cin >> N >> J;
		cout << "Case #" << I-T << ":" << endl;
		countCoins(N,primes,J);
	}
	return 0;
}