#include <iostream>
#include <string>
#include <set>
#include <fstream>

using namespace std;


long long sheetCounting(long long n)
{
	if (n == 0) return 0;
	long long resultat = 1;
	set<int> data;  
	long long t = n;
	while (data.size() != 10) {
		
		//cout << t << endl;
		while (t > 0) {
			data.insert(t % 10);
			t /= 10;
		}
		resultat++;
		t = n* resultat;
	}
	return n*(resultat-1);
}

int main() {


	long long N;
	int T;

	ifstream input("input.txt");
	ofstream output("output.txt");
	//cin >> T;
	input >> T;
	for (int i(1); i <= T; ++i)
	{
		//cin >> N;
		input >> N;
		long long v = sheetCounting(N);
		if (v == 0) output << "Case #" << i << ": " << "INSOMNIA" << endl;
		else output << "Case #" << i << ": " << v << endl;
	}
	return 0;
}