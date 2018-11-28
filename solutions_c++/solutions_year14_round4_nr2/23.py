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

int n,a[M];

void read(){
	cin>>n;
	for (int i=0; i<n; ++i)
		cin>>a[i];
}

void kill(){
	int ans = 0;
	for (int i=0; i<n; ++i){
		int x = 0, y = 0;
		for (int j=0; j<n; ++j)
			if (a[j]>a[i])
				if (j<i)
					++x;
				else
					++y;
		ans += min(x,y);
	}
	cout<<ans<<"\n";
}