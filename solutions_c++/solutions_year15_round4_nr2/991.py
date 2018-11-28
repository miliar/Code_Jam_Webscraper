#include<iostream>
#include<cstdio>
#include<vector>
#include<algorithm>

using namespace std;

int main() {

	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);

	int T;
	cin>>T;

	for(int t=1 ; t<=T ; t++) {
		int N;
		double V,X;

		cin>>N>>V>>X;
		vector<double> R(N), C(N);
		for(int i=0 ; i<N ; i++)
			cin>>R[i]>>C[i];

		double ans=0.0;
		if(N==1) {
			if(C[0]!=X) ans=-1.0;
			else ans=V/R[0];
		}
		else if(N==2) {
			if(C[0]==C[1]) {
				if(X!=C[1]) ans=-1.0;
				else ans=V/(R[0]+R[1]);
			}
			else if(C[0]>X && C[1]>X) ans=-1.0;
			else if(C[0]<X && C[1]<X) ans=-1.0;
			else {
				double t1=V*(X-C[1])/(R[0]*(C[0]-C[1]));
				double t2=(V-R[0]*t1)/R[1];

				if(t1>t2) ans=t1;
				else ans=t2;
			}
		}

		cout<<"Case #"<<t<<": ";
		if(ans>=0.0) printf("%.9lf\n", ans);
		else cout<<"IMPOSSIBLE\n";
	}

	return 0;
}