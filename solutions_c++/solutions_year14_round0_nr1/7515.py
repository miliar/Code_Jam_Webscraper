#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void skip_lines(int lines)
{
	for(int i = 0; i < lines; ++ i) {
		int tmp[4];
		cin >> tmp[0] >> tmp[1] >> tmp[2] >> tmp[3];
	}
}

void process_case(int case_id)
{
	int ans1;
	cin >> ans1;
	
	skip_lines(ans1 - 1);
	vector<int> v1(4);
	for(int i = 0; i < 4; ++ i) {
		cin >> v1[i];
	}
	sort(v1.begin(), v1.end());
	skip_lines(4 - ans1);
	
	int ans2;
	cin >> ans2;
	skip_lines(ans2 - 1);
	vector<int> v2(4);
	for(int i = 0; i < 4; ++ i) {
		cin >> v2[i];
	}
	sort(v2.begin(), v2.end());
	skip_lines(4 - ans2);
	
	vector<int> res(4);
	vector<int>::iterator it = set_intersection(v1.begin(), v1.end(), v2.begin(), v2.end(), res.begin());
	res.resize(it - res.begin());
	
	cout << "Case #" << case_id << ": ";
	if(res.size() == 0) {
		cout << "Volunteer cheated!" << endl;
	} else if(res.size() == 1) {
		cout << res[0] << endl;
	} else {
		cout << "Bad magician!" << endl;
	}
}

int main()
{
	int T;
	cin >> T;
	
	int i = 1;
	while(i <= T) {
		process_case(i);
	
		++ i;
	}
	
	return 0;
}