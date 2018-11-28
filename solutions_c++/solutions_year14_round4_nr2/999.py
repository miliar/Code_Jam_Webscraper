#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
long long A[1010];
struct St{
	long long idx;
	long long num;
	bool operator < (const St&t)const{
		return num < t.num;
	}
}S[1010];

int main(){
	int T;
	cin >> T;
	int idx=0;
	while(T--){
		++idx;
		int N;cin >> N;
		for(int i=0;i<N;++i)
			cin >> A[i];
		for(int i=0;i<N;++i){
			S[i].idx=i;
			S[i].num=A[i];
		}
		sort(S,S+N);
		long long ans=0;
		int id1=0,id2=N-1;
		for(int i=0;i<N;++i){
			int cidx = S[i].idx;
			ans += min(cidx, N-i-cidx-1);
			for(int j=i;j<N;++j){
				if(S[j].idx>cidx)
					--S[j].idx;
			}
		}
		cout << "Case #"<<idx<<": "<<ans<<endl;
	}
	return 0;
}
