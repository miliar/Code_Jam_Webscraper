#include <iostream>
#include <set>
#include <cstdio>
#include <cstdlib>
using namespace std;
int main(){
	int T;cin >> T;
	int idx = 0;
	while(T--){
		++idx;
		int a,b;
		int A[4][4],B[4][4];
		cin >> a;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				cin >> A[i][j];
		cin >> b;
		for(int i=0;i<4;++i)
			for(int j=0;j<4;++j)
				cin >> B[i][j];
		set<int> ans;
		set<int>S;
		for(int i=0;i<4;++i)
			S.insert(A[a-1][i]);
		for(int i=0;i<4;++i){
			if(S.find(B[b-1][i])!=S.end())
				ans.insert(B[b-1][i]);
		}
		cout << "Case #"<<idx<<": ";
		if(ans.size()>1)
			cout << "Bad magician!"<<endl;
		else if(ans.size()==0)
			cout << "Volunteer cheated!"<<endl;
		else cout << (*ans.begin()) << endl;
	}
	return 0;
}
