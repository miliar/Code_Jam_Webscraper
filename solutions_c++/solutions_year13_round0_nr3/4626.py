#include <iostream> 
#include <string> 
#include <algorithm> 
#include <map> 
#include <set> 
#include <vector> 
#include <string.h> 
#include <stdio.h> 
#include <math.h> 
#include <sstream> 

using namespace std; 
bool palindrome (long long x){
	long long b[15];
	int point = 0;
	while(x > 0){
		b[point] = x%10;
		x /= 10;
		point ++;
	}
	for(int i=0 ; i<point ; i++){
		if(b[point-i-1] != b[i])
			return false;
	}
	return true;
}
int t;
int main(){
	cin>>t;
	long long mx = 10e7;
	std::vector<long long> v;
	int pointer = 0;
	for(int i=0 ; i<=mx ; i++){
		if(palindrome(i) && palindrome(i*i)){
			v.push_back (i*i);
			pointer++;
		}
	}
	for(int i=0 ; i<t ; i++){
		long long a,b;
		cin>>a>>b;
		long long count = 0;
		for(int j=0 ; j<v.size() ; j++){
			if(v[j]<=b && v[j]>=a)
				count++;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}

return 0; 
}