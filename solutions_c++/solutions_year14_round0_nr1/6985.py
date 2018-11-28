#include <iostream>
#include <set>
using namespace std;

int main(){
	int T, ans, v, i, j;
	cin >> T;
	int k = 0;
	set<int> m;

	while(k<T){
		
		int count = 0, res;
		cin >> ans;
		ans--;
		i = 0;
		while(i<ans*4){
			cin >> v; i++;
		}
		for(j=0; j<4; j++){
			cin >> v;
			m.insert(v);
		}
		i += 4;
		while(i<16) {
			cin >> v; i++;
		}
		cin >> ans;
		ans--;
		i = 0;
		while(i<ans*4){
			cin >> v; i++;
		}
		for(j=0; j<4; j++){
			cin >> v;
			if(m.find(v)!=m.end()) {
				res = v;
				count++;
			}
		}
		i += 4;
		while(i<16) {
			cin >> v; i++;
		}
		if(count == 1)
			cout << "Case #" << k+1 << ": " << res << endl;
		else if(count == 0)
			cout << "Case #" << k+1 << ": Volunteer cheated!" << endl;
		else 
			cout << "Case #" << k+1 << ": Bad magician!" << endl;

		k++;
		m.clear();
	}
	return 0;
}