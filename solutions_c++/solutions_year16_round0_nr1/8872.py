#include <iostream>
#include <set>
using namespace std;
#define ll long long int
void insertDigits(set<int> &s, ll a){
	while( a != 0){
		s.insert(a%10);
		a /= 10;
	}
}

int main(){
	int t;
	cin>>t;
	int i = 1;
	ll ans;
	int a;
	set<int> s;
	while(i <= t){
		set<int> empty;
		swap(s,empty);
		cin>>a;
		if(a == 0){
			cout<<"Case #"<<i<<": INSOMNIA"<<endl;
		} else {
			insertDigits(s,a);
			int inc = 1;
			while(s.size() != 10){
				inc++;
				insertDigits(s,inc*a);
			}
			cout<<"Case #"<<i<<": "<<inc*a<<endl;
		}
		i++;
	}
	return 0;
}