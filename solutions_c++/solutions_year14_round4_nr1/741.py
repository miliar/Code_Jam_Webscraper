#include<iostream>
#include<algorithm>
#include<set>
using namespace std;

int solve(){
	int n, x, res = 0, a;
	multiset<int> s;
	cin >> n >> x;
	for(int i = 0;i < n;i++){
		cin >> a;
		s.insert(a);
	}
	while(!s.empty()){
		multiset<int>::iterator it = s.begin();
		int p = *it;
		s.erase(it++);
		it = s.upper_bound(x - p);
		if(it != s.begin()){
			it--;
			s.erase(it);
		}
		res++;
	}
	return res;
}

int main(){
  int t;
  cin >> t;
  for(int i = 1;i <= t;i++){
    cout << "Case #" << i << ": " << solve() << endl;
  }
  return 0;
}
