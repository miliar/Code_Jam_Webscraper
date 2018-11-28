#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
	int T;
	cin >> T;
	int idx=0;
	while(T--){
		++idx;
		int N,X;
		cin >> N >> X;
		vector<int> A(N);
		for(int i=0;i<N;++i)
			cin >> A[i];
		sort(A.begin(),A.end());
		int id1=0,id2=N-1;
		int ans=0;
		while(id2>=id1){
			if(A[id1]+A[id2]<=X)
				++id1;
			--id2;
			++ans;
		}
		cout << "Case #"<<idx<<": "<< ans <<endl;
	}
	return 0;
}
