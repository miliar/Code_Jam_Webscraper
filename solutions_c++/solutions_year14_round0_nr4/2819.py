#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

int main(){
	int T;
	cin>>T;
	for(int i=0;i<T;i++){
		int size;
		cin>>size;
		vector <double> a;
		vector <double> b;
		for(int j=0;j<size;j++){
			double r;
			cin>>r;
			a.push_back(r);
		}
		sort(a.begin(),a.end());
		for(int j=0;j<size;j++){
			double l;
			cin>>l;
			b.push_back(l);
		}
		sort(b.begin(),b.end());
		int ans=0;
		int fool=0;
		for(int j=0;j<size;j++){
			int tmp1=0;
			int tmp2=0;
			for(int k=j;k<size;k++){
				if(a[k]>b[k-j]){
					tmp1++;
				}
				if(b[k]>a[k-j]){
					tmp2++;
				}
			}
			ans=max(ans,tmp1);
			fool=max(fool,tmp2);
		}

		cout<<"Case #"<<i+1<<": "<<ans<<' '<<size-fool<<endl;
	}
	return 0;
}