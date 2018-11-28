#include<iostream>

using namespace std;

int main(){
	int total_tc;

	cin >> total_tc;

	for(int tc=0; tc<total_tc; tc++){
		int r, w, c;
		cin >> r >> c >> w;

		int result;

		int minfirst = c/w;
		result = minfirst+w;
		if(c%w == 0) result--;

		result *= r;

		cout << "Case #" << tc+1 << ": "<<result << endl;
	}


	return 0;
}