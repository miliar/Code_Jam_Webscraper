#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

void read();
void kill();

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int t;

	cin>>t;

	for (int i=1; i<=t; ++i){
		read();
		cout<<"Case #"<<i<<": ";
		kill();
	}

	return 0;
}

#define M 100100

int n,a[M],x;

void read(){
	cin>>n>>x;
	for (int i=0; i<n; ++i)
		cin>>a[i];
	sort(a,a+n);
}

void kill(){
	int ans = 0, l = 0, r = n - 1;
	while (l<r){
		if (a[l]+a[r]<=x){
			++l;
			--r;
		}
		else
			--r;
		++ans;
	}
	if (l==r)
		++ans;
	cout<<ans<<"\n";
}