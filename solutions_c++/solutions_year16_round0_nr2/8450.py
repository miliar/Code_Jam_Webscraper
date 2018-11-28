#include <iostream>
#include <vector>
#include <string>
using namespace std;

int transitions(std::vector<bool> &a, std::vector<bool> &rev) {

	//cout<<"probem of size "<<a.size()<<"  "<<rev.size()<<endl;

	if (a.size() == 0) {
		return 0;
	}

	if (a.size() == 1) {
		if (a[0]) {
			return 0;
		}
		else {
			return 1;
		}
	}
	int t;
	if (a[a.size() - 1]) {
		//remove all the plus from end
		int i;
		for (i = a.size() - 1; i >= 0 ; i--) {
			if (!a[i]) {
				break;
			}
		}
		a=std::vector<bool>(a.begin(), a.begin() + i + 1);
		rev=std::vector<bool>(rev.begin() + rev.size() - 1 - i , rev.end() );
		return transitions(a,rev);

	}
	else {
		if (!a[0]) {
			//reverse the vector and recurse
			return 1 + transitions(rev,a);
		}
		else {
			// remove all + from start make the - , reverse the new array and remove all the + frome end and recurse
			int i;
			for (i = 0; i < a.size(); i++) {
				if (a[i]) {
					a[i] = !a[i];
					rev[a.size() - 1 - i] = !rev[a.size() - 1 - i];
				}
				else{
					break;
				}
			}

			
			return 2 + transitions(rev,a);
		}
	}

}

int main() {

	int n;
	cin >> n;
	for (int k = 0; k < n; k++) {
		string temp;
		cin >> temp;
		std::vector<bool> v(temp.size());
		std::vector<bool> v_rev(temp.size());
		for (int i = 0; i < temp.size(); i++) {
			if (temp[i] == '+') {
				v[i] = true;
				v_rev[temp.size() - 1 - i] = false;
			}
			else {
				v[i] = false;
				v_rev[temp.size() - 1 - i] = true;
			}

		}
		int ans = transitions(v,v_rev);
		cout << "CASE #" << k + 1 << ": " << ans << endl;



	}

}