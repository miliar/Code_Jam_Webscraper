#include <iostream>
#include <vector>
#include <string>
#include <math.h>
using namespace std;
/*
A jamcoin is a string of N ≥ 2 digits with the following properties:

Every digit is either 0 or 1.
The first digit is 1 and the last digit is 1.
If you interpret the string in any base between 2 and 10, inclusive, the resulting number is not prime.

	2 to 10
	-
	-
	-


*/
int check_prime(string a){
	vector<long long> sol;
	for(int base=2;base<=10;base++){
		long long x=0;
		long long prod=1;
		for(int i=a.size()-1;i>=0;i--){
			x+=(a[i]-'0')*prod;
			prod=prod*base;
		}
		long long y=(long long)sqrt(x);
		int check=0;
		for(long long i=2;i<=y+1;i++)
		{
			if(x%i==0){
				check=1;
				sol.push_back(i);
				break;
			}
		}

		if(check==0) return 0;
	}
	cout<<a<<" ";
	for(int i=0;i<9;i++)
	{	cout<<sol[i];
		if(i!=8)cout<<" ";
	}
	cout<<"\n";
	return 1;
}

void coinjam(int N,int J,int i,string &sol,int &cnt){
	if(cnt==J) return;
	else if(i==1){ 
		sol.push_back('1');
		coinjam(N,J,i+1,sol,cnt);
	}else if(i==N){
		
		sol.push_back('1');
		//cout<<sol<<"\n";
		if(check_prime(sol)) cnt++;
		sol.erase(sol.size()-1);
		//sol.clear();
		//if(cnt==J) return;
	}else{
		sol.push_back('0');
		coinjam(N,J,i+1,sol,cnt);
		sol.erase(sol.size()-1);
		sol.push_back('1');
		coinjam(N,J,i+1,sol,cnt);
		sol.erase(sol.size()-1);
	}
}

main(){

	int T;
	cin>>T;
	for(int t=0;t<T;t++){
		int N,J;
		cin>>N;
		cin>>J;
		string sol;
		cout<<"Case #"<<t+1<<":\n";
		int cnt=0;
		coinjam(N,J,1,sol,cnt);
	}
}