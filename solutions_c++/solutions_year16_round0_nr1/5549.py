#include <iostream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <cmath>
#include <math.h>

using namespace std;

set <long long> s;

void add(long long a){
	while(a>0){
		s.insert(a%10);
		a/=10;
	}
	return;
}

int main()
{	
	long long t,n;
	cin>>t;
	long long in = 0;
	while(t--){
		s.clear();
		in++;
		cin>>n;
		if(n==0){
			cout<<"Case #"<<in<<": INSOMNIA"<<endl;
			continue;
		}
		long long i=0;
		while(s.size() < 10){
			i++;
			add(n*i);
		}
		
		cout<<"Case #"<<in<<": "<<i*n<<endl;
	}
	
	
	return 0;
}