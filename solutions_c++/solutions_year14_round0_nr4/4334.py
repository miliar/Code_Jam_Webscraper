#include <iostream>
#include <algorithm>    // std::sort
#include <vector>       // std::vector
#include <fstream>
using namespace std;

int main()
{
	ofstream myfile;
	myfile.open ("waro.txt");
	int test, lu, ld, ru, rd, p1, p2;
	int num;
	float in;
	cin >> test;
	
	for (int i = 0; i < test; ++i)
	{
		p1 = p2=0;
		cin >> num;
		vector<float> n, k;
		
		for (int j = 0; j < num; ++j)
		{
			cin >> in;
			n.push_back(in);
		}
		for (int j = 0; j < num; ++j)
		{
			cin >> in;
			k.push_back(in);
		}
		sort (n.begin(), n.end());  
		sort (k.begin(), k.end());

		lu = ru = num -1;
		ld = rd = 0;

		for (int j = num-1; j >= 0; --j)
		{
			// 	cout << n[lu] << k[ru] << endl;
			if (n[lu--] > k[ru])
			{
				p1++;rd++;
			}else{
				ru--;
			}
			if (ru<rd)
			{
				break;
			}
		}

		lu = ru = num -1;
		ld = rd = 0;

		for (int j = num-1; j >= 0; --j)
		{
			if (n[ld++] > k[rd])
			{
				rd++;p2++;
			}
		}

		myfile <<  "Case #" << i+1 << ": " << p2 << " " << p1 << endl;
		
	}
	return 0;
}