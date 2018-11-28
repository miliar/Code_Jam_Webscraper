#include <iostream>
#include <set>


using namespace std;

void add(unsigned long long int n, set<int> &s){
	while(n){
		s.insert(n%10);
		n/=10;
	}
}

int main(){
	set<int> s;
	int numbs=0;
	int t;
	cin>>t;
	unsigned long long int i;
	for (int j = 1; j <= t; ++j)
	{
		cin >> i;
		if(i==0){
			cout << "Case #" << j << ": INSOMNIA" << endl;
			continue;
		}
		unsigned long long int sum=i;
		add(sum, s);
		while(s.size()<10){
			sum+=i;
			add(sum, s);
		}
		cout << "Case #" << j << ": " << sum << endl;
		s.clear();
	}
}