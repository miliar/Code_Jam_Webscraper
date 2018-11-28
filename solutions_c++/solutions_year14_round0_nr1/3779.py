#include <iostream>
#include <vector>
#include <algorithm>

int main()
{
	using namespace std;

	vector<int> in_a, in_b;
	int row_a, row_b;
	int n_cases;
	
	cin >> n_cases;
	
	in_a.reserve(16);
	in_b.reserve(16);
	for (int case_no=1; case_no<=n_cases; ++case_no) {
		in_a.clear();
		in_b.clear();
	
		cin >> row_a;
		for (int i=0; i<16; ++i) {
			int n;
			
			cin >> n;
			in_a.push_back(n);
		}
		
		cin >> row_b;
		for (int i=0; i<16; ++i) {
			int n;
			
			cin >> n;
			in_b.push_back(n);
		}
		
		// get the rows, could have been optimized above, but
		// not worth it for small inputs
		vector<int> case_a_row, case_b_row;
		copy_n(in_a.begin() + (row_a-1)*4, 4, back_inserter(case_a_row));
		copy_n(in_b.begin() + (row_b-1)*4, 4, back_inserter(case_b_row));
		
		sort(case_a_row.begin(), case_a_row.end());
		sort(case_b_row.begin(), case_b_row.end());
		
		vector<int> result;
		set_intersection(case_a_row.begin(), case_a_row.end(),
		                 case_b_row.begin(), case_b_row.end(),
		                 back_inserter(result));
		                      
		cout << "Case #" << case_no << ": ";
		if (result.size() == 1)
			cout << result.front();
		else if (result.size() == 0)
			cout << "Volunteer cheated!";
		else
			cout << "Bad magician!";
		cout << endl;
	}
	
	return 0;
}

