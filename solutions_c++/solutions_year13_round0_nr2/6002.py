#include <cstdio>
#include <iostream>
using namespace std;

//#define MAX_SIZE 100

int main() {
	freopen("B-small-attempt0.in", "rt", stdin);
	freopen("B-small-attempt0.out", "wt", stdout);

	int a[10][10];
	int T;
	cin>>T;

	for(int i=1; i<=T; i++) {
		bool work=true;
		int N, M, h, temp=0;
		cin>>N>>M;
		for(int j=0; j<N; j++) {
			for(int k=0; k<M; k++) {
				cin>>h;
				a[j][k] = h;
			}
		}

		for(int j=0; j<N; j++) {
			for(int k=0; k<M; k++) {
				bool wh=true, wv=true;
				if(a[j][k] == 1) {
					for(int m=0; m<M; m++) 
						if(a[j][m] != 1) 
							wh = false;
					for(int n=0; n<N; n++) 
						if(a[n][k] != 1) 
							wv = false;

					if(wh==false && wv==false) work=false;
				}
			}
		}

		cout<<"Case #"<<i<<": ";
		if(work==true) cout<<"YES";
		else cout<<"NO"; 
		cout<<endl;
	}
}