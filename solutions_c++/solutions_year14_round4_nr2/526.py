#include <iostream>
#include <algorithm>
using namespace std;
const int maxn = 1000 + 10;
int a[maxn];
int l[maxn], r[maxn];
int main(){
	int cas = 0, T;
	for (cin>>T; T--;){
		cout<<"Case #"<<++cas<<": ";
		int n;
		cin>>n;
		for (int i = 0; i<n; i++){
			cin>>a[i];
		}
		int tot = 0;
		for (int i = 0; i<n; i++){
			l[i] = r[i] = 0;
			for (int j = 0; j<i; j++) if (a[j] > a[i]) l[i]++;
			for (int j = i+1; j<n; j++) if (a[j] > a[i]) r[i]++;
			tot += min(l[i], r[i]);
		}
		cout<<tot<<endl;
	}
	return 0;
}

