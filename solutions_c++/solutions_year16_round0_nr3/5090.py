#include <iostream>
using namespace std;

int bit_count = (32-4)/2;
int main() {
	cout <<"Case #1:\n"; 
	for(unsigned int i =0; i < 500; ++i)
	{
		cout << "11";
		for(int j =bit_count -1; j >=0; --j)
		{
			if(i & (1 << j))
			{
				cout << "11";
			}
			else
			{
				cout << "00";
			}
		}
		cout << "11";
		for(int k =2; k <=10;++k)
		{
			cout << " " << k+1;
		}
		cout << "\n";
	}
	// your code goes here
	return 0;
}