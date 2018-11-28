#include<iostream>
#include<vector>

using namespace std;






int main(){
	int T; cin >>T;
	for(int t=0;t<T; ++t){
		int d; cin >> d;
		int x;
		int ret = 99999;
		vector<double> vec;
		for(int i=0;i<d;++i){
			cin >> x;
			vec.push_back(x);
		}
		for(int i=1; i<1002; ++i){
			int aaa=i;
			for(int j=0;j<d;++j){
				double y = vec[j]/i;
				if(y<=1) continue;
				aaa += (y-0.000000001);
			}
			ret = min(aaa, ret);
		}
		cout << "Case #" << t+1 << ": " <<  ret << endl;
			
	}
	return 0;
}

