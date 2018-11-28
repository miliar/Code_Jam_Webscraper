#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>

using namespace std;

int main(void) {
	int T;
	cin>>T;
	int goal[100][100];
	bool done[100][100];
	for (int i=0;i<T;++i){
		int N,M;
		cin>>N>>M;
		set<int> H;
		for (int j=0;j<N;++j) {
			for (int k=0;k<M;++k) {
				int x;
				cin>>x;
				goal[j][k] = x;
				H.insert(x);
				done[j][k]=false;
			}
		}
	//	for (int h : H) {
		for (int j=0;j<N;++j) {
			for (int k=0;k<M;++k) {
	//			if (goal[j][k]==h && !done[j][k]) {
					//test line j
				int m1=0;
				int m2=0;
				for (int j2=0;j2<N;++j2) {
					m1= max(m1,goal[j2][k]);
				}
				for (int k2=0;k2<M;++k2) {
					m2= max(m2,goal[j][k2]);
				}
				if (min(m1,m2)<=goal[j][k]) {
					done[j][k]=true;
				}
		//		}
			}
		}
		//}
		bool result = true;
		for (int j=0;j<N;++j) {
			for (int k=0;k<M;++k) {
				result = result & done[j][k];
			}
		}
		cout<<"Case #"<<i+1<<": "<<(string)(result?"YES":"NO")<<'\n';
	} // end test i
}