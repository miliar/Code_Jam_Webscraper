#include<string>
#include<iostream>

using namespace std;

#define		MAX		1010

int p[MAX];

int d[MAX][MAX];

int main(){

	for (int i=0;i<MAX;i++){
		d[i][i] = 0;
		for (int j=0;j<i;j++){
			d[i][j] = MAX;
			for (int k=1;k<i;k++) d[i][j] = min(d[i][j],d[i-k][j]+d[k][j]+1);
		}
	}

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);

	int ntc,res,mx,r,n,x;
	cin >> ntc;
	for (int tc=1;tc<=ntc;tc++){
		cin >> n;
		memset(p,0,sizeof(p));
		mx = 0;
	
		for (int i=0;i<n;i++) cin >> x,p[x]++,mx = max(x,mx);
		
		r = 0;
		res = MAX;
		for (int i=1;i<=mx;i++){
			r = 0;
			for (int j=i;j<=mx;j++) 
				r += p[j]*d[j][i];
			res = min(res,r+i);
		}

		cout << "Case #" << tc << ": " << res << endl;
	}

	return 0;
}