#include <iostream>
#include <set>
using namespace std;

int main(){
	int t;
	long n,ndived;
	cin >> t;
	int multiCount;
	for (int i=0;i<t;++i){
		multiCount = 0;
		cin >> n;
		if (n == 0){
			cout << "Case #" << i+1 << ": INSOMNIA" << endl;
			continue;
		}
		set<int> count;
		while (count.size() != 10){
			++multiCount;
			ndived = n*multiCount;
			while (ndived != 0){
				count.insert(ndived % 10);
				ndived = ndived / 10;
			}			
		}
		cout << "Case #" << i+1 << ": "<< n*multiCount << endl;
	}
	system("pause");
	return 0;
}