#include <iostream>
#include <set>

using namespace std;

int main() {

	int T; cin>>T;

	for(int count = 1; count <= T; count++) {
		int a1; cin>>a1; a1--;
		set<int> c1;

		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++) {
				int v; cin>>v;

				if(i == a1)
					c1.insert(v);
			}

		int a2; cin>>a2; a2--;
		set<int> c2;

		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++) {
				int v; cin>>v;
				if(i == a2)
					c2.insert(v);
			}

		set<int> c;
		for(set<int>::iterator it = c1.begin(); it != c1.end(); it++)
			if(c2.find(*it) != c2.end())
				c.insert(*it);

		cout<<"Case #"<<count<<": ";
		if(c.size() == 0)
			cout<<"Volunteer cheated!";
		else if(c.size() > 1)
			cout<<"Bad magician!";
		else
			cout<<*(c.begin());
		cout<<endl;
	}

	return 0;
}
