//
//  main.cpp
//  counting_sheep
//
//  Created by YIQI CAI on 4/9/16.
//
//

#include <iostream>
#include <fstream>
#include <string>
#include<unordered_set>
using namespace std;

int end_number(int N)
{
	if (N == 0)
		return 0;
	unordered_set<int> s;
	for (int i = 0; i < 10; i++)
		s.insert(i);
	int test_num = 0;
	while (s.size())
	{
		test_num += N;
		int temp = test_num;
		while (temp)
		{
			s.erase(temp % 10);
			temp /= 10;
		}	
	}
	return test_num;
}

int main()
{
	ifstream ifile("A-large.in");
	ofstream ofile("A-large_Practice.out");
	int n_test;
	ifile >> n_test;
	for (int i = 0; i<n_test; i++)
	{
		int N;
		ifile >> N;
		int res = end_number(N);
		ofile << "Case #" << i + 1 << ": " << (res==0? "INSOMNIA" : to_string(res)) << endl;
	}
	ofile.close();
}

