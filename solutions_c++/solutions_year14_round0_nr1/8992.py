#include <iostream>
#include <vector>
using namespace std;

int main(){
	int T;
	cin >> T;
	for(int t=0;t<T;t++){
		vector<bool> a(17,0);
		int r;
		cin >> r;
		for(int i=0;i<4;i++){
			int k;
			for(int j=0;j<4;j++){
				cin >> k;
				if(i==(r-1))
					a[k]=true;
			}
		}
		vector<int> ans;
		cin >> r;
		for(int i=0;i<4;i++){
			int k;
			for(int j=0;j<4;j++){
				cin >> k;
				if(i==(r-1)&&a[k])
					ans.push_back(k);
			}
		}

		cout << "Case #" << t+1 << ": ";
		if(ans.size()==0)
			cout << "Volunteer cheated!";
		else if(ans.size()>1)
			cout << "Bad magician!";
		else
			cout << ans[0];
		cout << "\n";
	}

	return 0;
}
