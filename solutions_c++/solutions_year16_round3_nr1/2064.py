#include <iostream>
#include <vector>

using namespace std;
int a[30];

char getChar(int i) {
	return i + 'A';
}
// 100 50 50
int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	//cout << "es" << endl;
	int t;
	cin>>t;
	for (int cas=0;cas<t;cas++) {
		int n;
		cin>>n;
		int sum = 0;
		for (int i=0;i<n;i++) {
			cin>>a[i];
			sum += a[i];
		}
		vector <pair<int,int> > p;
		while(sum > 1) {
			int maxid1 = -1;
			int maxid2 = -1;
			for (int i=0;i<n;i++) {
				if (a[i] == 0) continue;
				if (maxid1 == -1 || a[i]>a[maxid1]){
					maxid2 = maxid1;
					maxid1 = i;
				}
				else if (maxid2 == -1 || a[i]>a[maxid2]) maxid2 = i;
			}
			//cout << maxid1 << " " << maxid2 << endl;
			a[maxid1]--;
			a[maxid2]--;
			sum -= 2;
			p.push_back(make_pair(maxid1, maxid2));
		}
		cout << "Case #" << cas+1 << ":";
		if (sum!=0)
			for (int i=0;i<n;i++) { if (a[i])cout << " " << getChar(i); }
		for (int i=0;i<p.size();i++) {
			cout << " " << getChar(p[i].first) << getChar(p[i].second);
		}
		cout << endl;
	}
}