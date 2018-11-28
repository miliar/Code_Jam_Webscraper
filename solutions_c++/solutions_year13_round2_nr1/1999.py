#include <iostream>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <string>
#include <algorithm>

#define inf 987654321

using namespace std;

int m;

typedef struct aa{
	int val;
	int k;
}node;

node check(long long int a,long long int b){
	long long int k = 0;
	while(b >= a){
		if(a == 1){
			k = inf;
			break;
		}
		a = a + a-1;
		k++;
	}
	node w;
	w.k = k;
	w.val = a;
	return w;
}

int main(){
	long long int test,C = 0;
	cin>>test;
	while(test--){
		C++;
		long long int a;
		long long int n;
		long long int c;
		cin>>a>>n;
		vector<long long int>v(n);
		for(int i = 0;i < n;i++)
			cin>>v[i];
		sort(v.begin(),v.end());
		c = 0;
		long long ans = inf;
		for(int i = 0;i < n;i++){
			ans = min(ans, c+n-i);
//			cout<<ans<<endl;
			if(a > v[i]){
				a = a + v[i];
//				cout<<"a--> "<<a<<endl;
			}
			else if(a <= v[i]){
				node q = check(a,v[i]);
//				cout<<q.k<<" a--> "<<q.val<<endl;
				if(q.k >= n-i){
					c = c + n-i;
					break;
				}
				else{
					a = q.val + v[i];
					c = c + q.k;
//					cout<<"c--> "<<c<<endl;
				}	
			}
		}
		ans = min(ans, c);
		cout<<"Case #"<<C<<": "<<ans<<endl;
	}
	return 0;
}