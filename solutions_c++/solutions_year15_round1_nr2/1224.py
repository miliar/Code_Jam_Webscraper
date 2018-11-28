#include<string>
#include<vector>
#include<iostream>
#include<algorithm>

using namespace std;

#define		MAX		1010
#define		LL		unsigned long long

LL b[MAX];

int main(){

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	LL mx,k;
	int ntc,n;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> n >> k;


		mx = 0;
		for (int i=0;i<n;i++){ 
			cin >> b[i];
			mx = max(mx,b[i]);
		}
	
		if (k<=n){
			cout << "Case #" << tc << ": " << k <<endl;
			continue;
		}

		k -= n;

		LL l = 0,h = mx*k,m,r;

		while(l!=h){
			m = (l+h+1)/2;
			r = 0;
			for (int i=0;i<n;i++) r+=m/b[i];
			if (r>=k) h = m-1;
			else l = m;
		}



		r = 0;
		for (int i=0;i<n;i++) r+=l/b[i];

		vector<int> res;

		l++;
		for (int i=0;i<n;i++) if (l%b[i]==0) res.push_back(i+1);

		cout << "Case #" << tc << ": " << res[k-r-1] <<endl;
	}

	return 0;
}