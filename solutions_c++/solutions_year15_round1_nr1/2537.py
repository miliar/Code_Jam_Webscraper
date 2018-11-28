#include<bits/stdc++.h>
using namespace std;
int main(){
	vector<int> a;
	int t,n,pp,maxx,tsum, i,sum,tmp,tt;
	cin >> t;
	for(pp=1;pp<=t;++pp){
		maxx=0;
		sum=0;
		a.clear();
		cin >> n;
		while(n--){
			cin >> tmp;
			a.push_back(tmp);
		}
		for(i=1,sum=0;i<a.size();++i){
			if(a[i-1]>a[i]){
				sum+=(a[i-1]-a[i]);
			}
			maxx = max(maxx, (a[i-1]-a[i]));
		}
		for(tsum=0,i=0;i<(a.size()-1);++i){
			if(a[i]<=maxx) tsum+=a[i];
			else{
				tsum+=maxx;
			}
		}
		cout << "Case #" <<pp << ": " << sum << " "<< tsum << endl;
	}
}
