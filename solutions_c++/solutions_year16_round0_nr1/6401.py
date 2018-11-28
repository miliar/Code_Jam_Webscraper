#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <algorithm>
#include <fstream>

using namespace std;

int main(void)
{
	ifstream fin("in.txt");
	ofstream fout("out.txt");
	int testCase;
	fin >> testCase;
	for (int test = 0; test < testCase; ++test) {
		fout << "Case #" << test+1 << ": ";
		int n;
		fin >> n;
		//cout << "n: " << n << endl;
		if (n == 0)
			fout << "INSOMNIA" << endl;
		else {
			vector<int> nums;
			while (n>0) {
				nums.push_back(n % 10);
				n /= 10;
			}
			set<int> numsSet;
			int count = 0;
			vector<int> tempNums;
			do {
				++count;
				int addSize = sqrt(sqrt(sqrt((double)count)));
				tempNums.resize(0);
				tempNums.resize(nums.size()+1+addSize);
				for (int i = 0; i < nums.size(); ++i) {
					tempNums[i] += nums[i]*count;
					tempNums[i + 1] += tempNums[i] / 10;
					tempNums[i] %= 10;
				}
				for (int i = nums.size()+1; i < tempNums.size(); ++i) {
					tempNums[i] += tempNums[i-1] / 10;
					tempNums[i-1] %= 10;
					if (tempNums[i-1] == 0) break;
				}
				while (tempNums.back() == 0) tempNums.pop_back();
				//cout << "tempNums: ";
				//for (auto data : tempNums)
				//	cout << data << ' ';
				//cout << endl;
				for (auto data : tempNums)
					numsSet.insert(data);
			} while (numsSet.size() < 10);
			//cout << "count: " << count << endl;
			//cout << "numsSet: " << numsSet.size() << endl;
			//for (auto data : numsSet)
			//	cout << data << ' ';
			//cout << endl;
			reverse(tempNums.begin(), tempNums.end());
			for (auto data : tempNums)
				fout << data;
			fout << endl;
		}
	}
	fin.close();
	fout.close();

	return 0;
}