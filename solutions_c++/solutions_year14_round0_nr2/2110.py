#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <iomanip>
using namespace std;
int main(){
	int T;cin>>T;
	int idx =0 ;
	while(T--){
		++idx;
		double C,F,X;
		cin >> C >> F >> X;
		int a = X/C-1-2/F;
		double ans = X/2;
		for(int i=a;i<a+2;++i){
			if(a<0)continue;
			double tans = X/(2+i*F);
			for(int j=0;j<i;++j)
				tans += C/(2+j*F);
			if(tans < ans)ans=tans;
		}
		cout << "Case #" << idx << ": "<<setprecision(30)<<ans << endl;
	}
	return 0;
}
