#include <iostream>
#include <unordered_map>
#include <string>
using namespace std;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T; int S; string p;
	cin >> T;
	for (int t = 0; t < T; t++) {
		cin >> S >> p;
		int haveStoodUp = 0;
		int toAdd = 0;
		for (int i = 0; i < p.size(); i++) {
			int curr = p[i]-'0';
			if(haveStoodUp>=i) {
				haveStoodUp+=curr;
			} else if (curr>0) {
				toAdd += i-haveStoodUp;
				haveStoodUp+=curr+(i-haveStoodUp);
			}
		}
		cout << "Case #" << t+1 << ": " << toAdd << endl;
	}
}