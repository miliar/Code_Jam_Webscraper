#include <iostream>
#include <set>
using namespace std;

void separate(int t,set<int> &new_set) {
	int k = t;
	while(k>0) {
		int temp = k%10;
		new_set.insert(temp);
		k/=10;
	}
}

int main(int argc, char const *argv[])
{
	int t;
	cin >> t;
	int begin = 0;
	while(t--) {
		set<int> new_set;
		int n;
		cin >> n;
		begin++;
		if(n==0) {
			cout << "Case #" << begin << ": INSOMNIA" << endl;
			continue;
		}
		int start = n;
		int counter = 1;
		while(new_set.size()<10) {
			separate(start,new_set);
			start = n * (++counter);
			//cout << "start " << start << endl;
		}
		cout << "Case #" << begin << ": " << n* (--counter) << endl; 
	}
	return 0;
}
