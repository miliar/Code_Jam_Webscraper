#include <iostream>
#include <queue>
#include <string>
#include <vector>
#include <cmath>
using namespace std;
typedef long long i64;
#define fu(i,m,n) for(int i=m; i<n; i++)
#define fr(i,m,n) for(typeof(m) i=m; i!=n; i++)
#define fa(i,c) fr(i,(c).begin(),(c).end())


int main(void) {
	int T;
	cin >> T;
	for(int ts=1; ts<=T; ts++) {
		int N,X;
		cin >> N >> X;
		vector<int> files(N);
		fu(i,0,N) cin >> files[i];
		sort(files.begin(),files.end());
		int cnt=0;
		int i=0, j=N-1;
		while(i<N) if(files[i]==-1) { i++; continue;} else {
			cnt++;
			while(j>=0 && (files[j]==-1 || files[i]+files[j]>X || i==j)) j--;
			if(j>=0) files[j]=-1;
			files[i]=-1;
			i++;
		}
		cout << "Case #" << ts << ": " << cnt << endl;
	}
}
