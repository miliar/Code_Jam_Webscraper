#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
	int n;
	cin >> n; 
	for(int y=0;y<n;++y) {
		int a1,a2;
		cin>>a1;
		vector<int> v1(4),v2(4);
		for(int i=0;i<4;++i) {
			for(int j=0;j<4;++j) {
				int b;
				if(i == a1 - 1)
					cin >> v1[j];
				else
					cin >> b;
			}
		}
		cin>>a2;
		for(int i=0;i<4;++i) {
			for(int j=0;j<4;++j) {
				int b;
				if(i == a2 - 1)
					cin >> v2[j];
				else
					cin >> b;
			}
		}
		int x2=0,k=0;
		bool f1=false;
		for (int i =0; i < 4; ++i) {
			for (int j =0;j<4;++j) {
				if(v1[i] == v2[j]) {f1=true; x2=v1[i]; ++k;}			
			}
		} 
		if (y!=n-1) {
			if(f1 && k == 1) cout << "Case #"<<y+1<<": "<<x2<<endl;
			else if(k > 1) cout << "Case #"<<y+1<<": Bad magician!"<<endl;
				else cout << "Case #"<<y+1<<": Volunteer cheated!"<<endl;
		}
		else {
			if(f1 && k == 1) cout << "Case #"<<y+1<<": "<<x2<<endl;
			else if(k > 1) cout << "Case #"<<y+1<<": Bad magician!"<<endl;
				else cout << "Case #"<<y+1<<": Volunteer cheated!"<<endl;
		}
	}
}