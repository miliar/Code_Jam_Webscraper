#include <iostream>
#include <vector>
#include <queue>
#include <set>
#include <algorithm>
#include <map>
#include <cstdio>
#include <cmath>
#include <fstream>

using namespace std;

bool allTruth(const vector<bool>& v){
	for(bool value : v){
		if(!value){
			return false;
		}
	}
	return true;
}

int main() {
	int t = 0;
	cin >> t;
	for(int tIndex = 1; tIndex <= t; tIndex++){
		vector<bool> digits_seen(10, false);
		long long n;
		long long i = 1;
		cin>>n;
		if(n == 0){
			cout<<"Case #"<<tIndex<<": INSOMNIA"<<endl;
			continue;
		}
		do{
			long long tmp = n * i;
			while(tmp > 0){
				digits_seen[tmp%10] = true;
				tmp/=10;
			}
			i++;
		} while(!allTruth(digits_seen));
		--i;
		cout<<"Case #"<<tIndex<<": "<<i * n<<endl;
	}
}
