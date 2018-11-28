#include <fstream>
#include <iostream>
using namespace std;

void main(){
	ifstream infile("A-large.in");
	cin.rdbuf(infile.rdbuf());

	ofstream outfile("output.txt");
	cout.rdbuf(outfile.rdbuf());

	int t,n;
	bool arr[10] = { false };
	int c = 1;
	cin >> t;
	for (; t; t--){
		bool check = false;
		int count = 2;
		memset(arr, false, 10);
		cin >> n;
		if (!n){
			cout << "case #" << c << ": INSOMNIA" << endl;
			c++;
			continue;}
		int res = n;
		while (1){
			int x = res;
			while (x > 0){
				arr[x % 10] = true;
				x /= 10;
			}
			int i;
			for (i = 0; i < 10; i++){
				if (!(arr[i]))
					break;
			}
			if (i == 10)
			{
				cout << "case #" << c << ": " << res << endl;
				break;
			}
			res=n* count;
			count++;
		}
		c++;
	}
}