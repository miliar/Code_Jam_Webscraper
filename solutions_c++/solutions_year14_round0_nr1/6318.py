#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<unsigned> get_row(unsigned x)
{
	vector<unsigned> result;
	for (unsigned i = 1; i <= 4; i++){
		vector<unsigned> row(4);
		cin >> row[0] >> row[1] >> row[2] >> row[3];
		if (i == x)
			copy(row.begin(), row.end(), back_inserter(result));
	}
	return result;
}

template <typename It>
void print_result(It start, It end)
{
	for (; start != end; start++)
		cerr << *start << " ";
	cerr << "\n";
}

int main()
{
	unsigned num_cases;
	cin >> num_cases;
	for (unsigned i = 1; i <= num_cases; i++) {
		unsigned x;
		cin >> x;
		vector<unsigned> first = get_row(x);
		cin >> x;
		vector<unsigned> second = get_row(x);
		vector<unsigned> result;
		sort(first.begin(), first.end());
		sort(second.begin(), second.end());
		set_intersection(first.begin(), first.end(),
				second.begin(), second.end(),
				back_inserter(result));
		//print_result(first.begin(), first.end());
		//print_result(second.begin(), second.end());
		//print_result(result.begin(), result.end());
		cout << "Case #" << i << ": ";
		if (result.size() == 1)
			cout << result[0] << "\n";
		else if (result.size() > 1)
			cout << "Bad magician!\n";
		else
			cout << "Volunteer cheated!\n";
	}
}
