#include <math.h>
#include <iostream>
#include <fstream>
#include <vector>
#include <stdlib.h>
using namespace std;

class Solution {
private:
	vector<int>cur_number;
	bool Prime;
	int digital_num;
public:
	Solution(vector<int>cur_number, int digital_num)
	{
		this->cur_number = cur_number;
		Prime = false;
		this->digital_num = digital_num;
	}
	//  ~Solution()
	//  {
	//    vector<int>().swap(cur_number);
	//  }



	bool isPrime(long long int testNum) {
		for (int i = 2; i<=sqrt(testNum); i++)
		{
			if (testNum%i == 0)
			{
				return false;
			}
		}
		return true;
	}

	int nontrivial(long long int total) {
		int d = 2;
		while (total%d != 0)
		{
			d = d + 1;
		}
		return d;
	}


	void Permutation(){

		long long int total = 0;

		for (int j = 2; j <= 10; j++)
		{
      int index=0;
			for (int k = digital_num-1; k>=0; k--) {
				total += cur_number[k] * pow(j, index);
        index++;
			}
			if (isPrime(total)) { Prime = true; break; }
			cur_number.push_back(nontrivial(total));
			total = 0;
		}
	}
	void print() {
		if (!Prime)
		{
			for (int i = 0; i<digital_num; i++)
			{
				cout << cur_number[i];
			}
			for (int j = digital_num; j<digital_num + 9; j++)
			{
				cout << " " << cur_number[j];
			}
		}
	}
	bool getifPrime() const {
		return Prime;
	}

};


void permutation(vector<int>&output, int total, int mut_times, int digital)
{
	total += mut_times;
	for (int i = digital-2; i >0; i--)
	{
		output[i] = total % 2;
		total /= 2;
	}
}


int main()
{
  int test_case;
	int Number_digital;
	int rows;
	int cur_rows = 0;
	int try_num = 0;
	vector<int>output;
  cin>>test_case;
	cin >> Number_digital;
	cin >> rows;
  cout<<"Case #"<<test_case<<":"<<endl;
  output.push_back(1);
	for (int i = 1; i<Number_digital-1; i++)
	{
		output.push_back(0);
	}
  output.push_back(1);

	long long int total = 0;
	for (int k = 1; k<Number_digital - 1; k++) {
		total += output[k] * pow(2, k - 1);
	}

	while (cur_rows<rows) {
		Solution a(output, Number_digital);
		a.Permutation();

		if (!a.getifPrime()) {
			cur_rows++;
			a.print();
			cout << endl;
		}
		try_num++;
		permutation(output, total, try_num, Number_digital);
	}
	return 0;
}
