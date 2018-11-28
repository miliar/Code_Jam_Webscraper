#include<iostream>
#include<iomanip>
#include<vector>
#include<string>
#include<algorithm>
#include<list>
#include<map>
#include<math.h>
using namespace std;
long long num=100000000;

bool checkPalindrome(long long num){
	long long palin=0, n=num;
	int d;
	while(n>0){
		d=n%10;
		palin=palin*10+d;
		n=n/10;
	}
	if(palin==num)
		return true;
	else
		return false;
}

int main()
{	
	vector<long long> palindrome;
	for(long long k=1; k<=num; k++){
		if(checkPalindrome(k)){
			if(checkPalindrome(k*k))
				palindrome.push_back(k*k);
		}
	}
	
	int t;
	cin>>t;
	for(int l=1; l<=t; l++){
		long long a, b, i, count=0;;
		cin>>a>>b;
		
		for(i=0; i<palindrome.size(); i++){
			if(palindrome[i]>=a && palindrome[i]<=b){
				count++;
			}
		}
		cout<<"Case #"<<l<<": "<<count<<endl;
	}
	
	return 0;
}