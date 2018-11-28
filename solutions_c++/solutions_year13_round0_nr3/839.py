#include<iostream>
#include<vector>
#include<algorithm>
#include<iterator>
#include<cmath>
#include<fstream>
#include<string>
#include<sstream>
#include<cstdlib>
using namespace std;

// alll fair and square numbers are of form 3, 2002, 20002, 20102, 1aa1 (a has only 0s and 1s, and at most 3 1s), 
// and 1aba1 (b<=2, a has only 0s and 1s, and at most (7-b^2)/2 1s)
// their sqaures all have odd number of digits



// return n choose m
int choose(int n, int m)
{
	if (n < m)
		return 0;

	int result = 1;
	for (int i = 1; i <= m; i++)
	{
		result = result * (n+1-i) / i;
	}
	return result;
}

// [10^{digit-1}, 10^digit -1]
int count_complete(int digit)
{
	int result = 0;
	if (digit == 1)
		return 3;

	// 22 and aa
	if (digit % 2 == 0)
	{
		result = 1 + 1 + choose(digit/2-1, 1) + choose(digit/2-1, 2) + choose(digit/2-1, 3);
		return result;
	}
	if (digit % 2 == 1)
	{
		result = 2 + 3 + 3*choose(digit/2-1, 1) + 2*choose(digit/2-1, 2) + 2*choose(digit/2-1, 3); 
		return result;
	}
}

// [10^{digit-1}, ubub]
// here ub has (digit+1)/2
int count_partial(int digit, int ub)
{
	if (digit == 1)
	{
		if (ub <= 0)
			return 0;
		else if (ub <= 3)
			return 1;
		else if (ub <= 8)
			return 2;
		else
			return 3;
	}
}

int count_stupid(int lb, int ub, vector<int> all)
{
	int index_lb = 0;
	int index_ub = 0;
	for (vector<int>::size_type i = 0; i < all.size(); i++)
	{
		if (lb > all[i])
			index_lb++;
		if (ub >= all[i])
			index_ub++;
		else
			break;
	}

	return index_ub - index_lb;
}



int main(int argv, char* argc)
{


	vector<int> count_digit;
	for (int i = 1; i <= 7; i++)
	{
		count_digit.push_back(count_complete(i));
	}
	for (vector<int>::iterator i = count_digit.begin(); i != count_digit.end(); i++)
		cout << *i << endl;

	vector<int> all;
	all.push_back(1);
	all.push_back(2);
	all.push_back(3);
	all.push_back(11);
	all.push_back(22);
	all.push_back(101);
	all.push_back(111);
	all.push_back(121);
	all.push_back(202);
	all.push_back(212);
	all.push_back(1001);
	all.push_back(1111);
	all.push_back(2002);
	all.push_back(10001);
	all.push_back(10101);
	all.push_back(10201);
	all.push_back(11011);
	all.push_back(11111);
	all.push_back(11211);
	all.push_back(20002);
	all.push_back(20102);
	all.push_back(100001);
	all.push_back(101101);
	all.push_back(110011);
	all.push_back(111111);
	all.push_back(200002);
	all.push_back(1000001);
	all.push_back(1001001);
	all.push_back(1002001);
	all.push_back(1010101);
	all.push_back(1011101);
	all.push_back(1012101);
	all.push_back(1100011);
	all.push_back(1101011);
	all.push_back(1102011);
	all.push_back(1110111);
	all.push_back(1111111);
	all.push_back(2000002);
	all.push_back(2001002);

	cout << all.size() << endl;

	ifstream infile("test.txt");
	ofstream outfile("result.txt");
	if (!infile || !outfile)
	{
		cout << "wrong" << endl;
		return -1;
	}

	int numCase;
	infile >> numCase;

	for (int i = 0; i < numCase; i++)
	{
		double lbs, ubs;
		infile >> lbs >> ubs;
		int lb, ub;
		lb = ceil(sqrt(lbs));
		ub = floor(sqrt(ubs));

		outfile << "Case #" << i+1 << ": " << count_stupid(lb, ub, all) << endl;
	}
	infile.close();
	outfile.close();

}