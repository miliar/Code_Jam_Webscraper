#include <iostream>
#include <set>

using namespace std;

int main() {
	int tc;
	int a[4][4];
	int b[4][4];
	int x,y;
	set<int> s;
	cin >> tc;
	int ret;

	for (int t = 1; t <= tc; ++t) {

		cin>>x;
		for (int i = 0; i < 4; ++i)
			cin >> a[i][0] >> a[i][1] >> a[i][2] >> a[i][3];

		cin>>y;
		for (int i = 0; i < 4; ++i)
			cin >> b[i][0] >> b[i][1] >> b[i][2] >> b[i][3];

		ret = -1;
		s.clear();
		s.insert(a[x-1][0]);
		s.insert(a[x-1][1]);
		s.insert(a[x-1][2]);
		s.insert(a[x-1][3]);

		set<int>::iterator it;
		int matches = 0;
		for (int i = 0; i < 4; ++i) {
			if ((it = s.find(b[y-1][i])) != s.end()){
				matches++;
				ret = *it;
			}
		}
		switch(matches){
		case 0:
			cout<<"Case #"<<t<<": Volunteer cheated!"<<endl;
			break;
		case 1:
			cout<<"Case #"<<t<<": "<<ret<<endl;
			break;
		default:
			cout<<"Case #"<<t<<": Bad magician!"<<endl;
		}

	}
return 0;
}

