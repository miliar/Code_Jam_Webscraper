#include <iostream>
#include <string>
#include <vector>

using namespace std;

int main() {
	int cases=0;
	cin >> cases;
	int caseNum=0;
	while (caseNum < cases) {
		caseNum++;
		cout << "Case #" << caseNum << ":";
		int n=0;
		cin >> n;
		vector<int> p;
		char largeName='A';
		int largeP=0;
		char secName='A';
		int secP=0;
		for (int i=0;i<n;i++) {
			int x=0;
			cin >> x;
			p.push_back(x);
			if (x>largeP) {
				secP=largeP;
				secName=largeName;
				largeP=x;
				largeName='A'+i;
			} else if (x>secP) {
				secP=x;
				secName='A'+i;
			}
		}
		p[largeName-'A']=0;
		p[secName-'A']=0;
		for (int i=0; i< largeP-secP; i++)
			cout << ' ' << largeName;
		for (int i=0; i<p.size();i++)
			for (int j=0; j<p[i];j++)
				cout << ' ' << char('A'+i);
		for (int i=0; i<secP; i++)
			cout << ' ' << largeName << secName;
		cout << endl;

	}
	return 0;
}

