#include <iostream>
using namespace std;

int main() {
	unsigned int T, start, end, count;
	cin >> T;
	for(int i=1;i<=T;++i) {
		count = 0;
		cin >> start >> end;
		if(1>=start && 1<=end)
			++count;
		if(4>=start && 4<=end)
			++count;
		if(9>=start && 9<=end)
			++count;
		if(121>=start && 121<=end)
			++count;
		if(484>=start && 484<=end)
			++count;
		cout << "Case #" << i << ": " << count << '\n';
	}
	return 0;
}