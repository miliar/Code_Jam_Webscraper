#include <bits/stdc++.h>
using namespace std;
const int limit = 1000 + 5;
int f[limit][limit];
int main(){
	freopen("file.inp","r",stdin);
	freopen("data.txt","w",stdout);
	int test; scanf("%d",&test);
	for(int T = 1; T <= test; ++T){
		printf("Case #%d: ",T);
		
		int n; scanf("%d",&n);
		vector<int> a;
		map<int,int> d;
		for(int i = 0; i < n; ++i){
			int k; scanf("%d",&k);
			a.push_back(k);
			d[k] = 0;
		}
		
		int k = 0;
		for(auto &p: d) p.second = ++k;
		for(int i = 0; i < n; ++i) a[i] = d[ a[i] ];
		
		memset(f, 0x3f, sizeof f);
		f[0][0] = 0;
		for(int i = 1; i <= n; ++i){
			int Left = 0, Right = 0;
			bool isLeft = true;
			int pos = 0;
			for(int j = 0; j < n; ++j) {
				if (a[j] < i) {
						if (isLeft) Left++; 
							else Right++;
					}
				if (a[j] == i) pos=j+1, isLeft = false;
			}
			
			int moveLeft = pos - Left - 1;
			int moveRight = n-pos - Right;
			//cout << pos << " " << Left << " " << Right << endl;
			//int curLeft = pos-Left;
			
		
			for(int j = 0; j < i; ++j){
				int k = i-j-1;
				
				f[j+1][k] = min(f[j+1][k], f[j][k] + moveLeft);
				f[j][k+1] = min(f[j][k+1], f[j][k] + moveRight);
			}
		}
		
		
		int kq = (int)1e9;
		for(int i = 0; i <= n; ++i)
			kq = min(kq , f[i][n-i] );
			
		/*
		for(int i = 0; i <= n; ++i)
		for(int j = 0; j <= n; ++j) cout << i << " " << j << " " << f[i][j] << endl;
		//*/
		printf("%d\n",kq);
		
	}

}