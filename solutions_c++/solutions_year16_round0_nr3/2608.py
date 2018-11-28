/**
*	
*	BY : Rajan Parmar
*/
#include <iostream>
#include <string>
#include <cmath>
#include <time.h>
#include <cstdio>
#include <vector>
#include <map>
#include <algorithm>
#include <memory.h>
using namespace std;
#pragma warning(disable:4996)
#define fi first
#define se second
#define mp make_pair
#define gc getchar_unlocked
#define mod 1000000007

typedef long long int ll;
typedef pair<ll, ll > pi;
typedef pair<ll, pi > pii;
vector < ll > vec ;

int isPrime[65600] ;

ll base(ll a,ll b,ll len){
	ll res = 0;
	for(int i=0; i < len ; i++){
		
		res += ( pow(b,i) * (a%10) ) ;		
		a/=10;
	}
	return res;
}

ll base2(ll a){
	ll res = 0;
	ll mul = 1;
	while(a){		
		res += (a%2)*mul ;
		mul*=10;
		a/=2;
	}
	return res;
}

int is_prime_not(ll num)
{
	int isprime = 0;
	if(num%2 == 0)
		return 2;
	
	for(int i = 3; i <= sqrt(num); i += 2)
	{		

		if(((num)% i) == 0)
		{
			return i;
		}
		
	}

	return 0;
}

int main() {


	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0-sol.out", "w", stdout);
	int t;
	int c;
	int N, J;
	ll no, i, j;
	memset(isPrime , 0 , sizeof(isPrime));
	
	//if isPrime = 0 i.e it is prime
	for(i = 2 ; i < 65600 ; i++){
		if(isPrime[i]==0){
			for(j = i*2 ; j < 65600 ; j+=i){
				isPrime[j] = 1;
			}
		}
	}
	
	cin >> t;
	cin >> N >> J ;
	c = 1;	
	//no =  pow( 10 , N - 1 ) ; 
	no = 1;
	for(i = 1 ; i<N ;i++){
		no*=10;
	}
	no += 1;
				//cout << no << "\n";
				//cout << base(no,2,N) << "\n";
				cout << "Case #" << c++ <<":\n" ;
				for(i=no ; J > 0 ;){
					int bs = 2;
					vec.push_back(i);
					int flag = 1;
					for(j = 2 ; j <= 10 ; j++){
						ll curr = base(i,j,N);
						
						ll check = is_prime_not(curr);
						if(check != 0){
							vec.push_back(check) ;	
						}
						else{
							
							flag = 0;
						}
					}
					if(flag){
						for(int k = 0 ; k < vec.size() ; k++){
							cout << vec[k] <<" ";
						}
						cout << "\n";
						
						J--;
					}
					i = base(i,2,N);
					i+=2 ;
					i = base2(i);
					vec.clear();
				}
				//cout << "Case #" << c++ <<":\n" ;
		
					
	
	
	return 0;
}
