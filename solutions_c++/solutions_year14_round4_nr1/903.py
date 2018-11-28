#include<bits/stdc++.h>
using namespace std;

int sol(){
	int n,x;
	multiset<int> s;
	cin >> n >> x;
	for(int i=0;i<n;++i){
		int a;
		cin >> a; s.insert(-a);
	}
	int ans = 0;
	for(;s.size();++ans){
		int tmp=*s.begin()+x;
		//cerr << *s.begin();
		s.erase(s.begin());
		if(s.size() && -*s.rbegin()<=tmp){
			auto it =s.lower_bound(-tmp);
		//	cerr <<" "<< *it ;
			s.erase(it);
		}
		//cerr << endl;
	}
	return ans;
}
int main(){
	int T;
	cin >> T;
	for(int i=1;i<=T;++i)
		cout << "Case #"<<i <<": " << sol() << endl;
}
