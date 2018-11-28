#include<iostream>
#include<iomanip>
#include<vector>
using namespace std;

int main(){
	int T;
	cin >> T;
	vector<double> ans(T,0.0);
	for(int i=0;i<T;i++){
		double c,f,x;
		cin >> c >> f >> x;
		double nfarm_f = (f*x-2*c)/c/f;
		//cout << nfarm_f << endl;
		int nfarm = nfarm_f+1;
		//cout << nfarm << endl;
		int n = 2*c-f*x+c*nfarm*f<0 ? nfarm:nfarm-1;
		if(nfarm_f < 0) n = 0;
		//cout << "n: " << n << endl;
		for(int j = 0;j < n;j++)
			ans[i] += c/(2+f*j);
			
		ans[i] += x/(2+n*f);
	}
	for(int i = 0;i<T;i++)
		cout << "Case #" << i+1 <<": " << fixed << setprecision(7) << ans[i] << endl;
		
	return 0;
}
