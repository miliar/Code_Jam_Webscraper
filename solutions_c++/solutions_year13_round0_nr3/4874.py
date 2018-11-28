#include<iostream>
#include<fstream>
#include<string>
#include<cmath>
using namespace std;

int main()
{
	ifstream infile("sampleC.in");
	streambuf* inStream_buf(cin.rdbuf());
	cin.rdbuf(infile.rdbuf());
	ofstream outfile("sampleC.out");
	streambuf* outStream_buf(cout.rdbuf());
	cout.rdbuf(outfile.rdbuf());
	int i,j,k,n,a,b,lowerbound,upperbound,sum,temp,node,flag;
	int digit[20];
	cin >> n; 
	for (i = 0;i < n;++i)
	{
		cin >> a >> b;
		sum = 0;
		lowerbound = (int)sqrt(a);
		upperbound = (int)sqrt(b - 1) + 1;
		for (j = lowerbound;j <= upperbound;++j)
		{
			flag = 1;
			temp = j;
			node = 0;
			while (temp > 0)
			{
				digit[node] = temp % 10;
				temp /= 10;
				++node;
			}
			for (k = 0;k <= ((node - 2) / 2);++k)
			{
				if (digit[k] != digit[node-1-k])
				{
					flag = 0;
					break;
				}
			}
			if (!flag) continue;
			temp = j * j;
			if (temp < a) continue;
			if (temp > b) break;
			node = 0;
			while (temp > 0)
			{
				digit[node] = temp % 10;
				temp /= 10;
				++node;
			}
			for (k = 0;k <= ((node - 2) / 2);++k)
			{
				if (digit[k] != digit[node-1-k])
				{
					flag = 0;
					break;
				}
			}
			if (flag) ++sum;
		}
		cout << "Case #" << i+1 << ": " << sum << endl;
	}
	cin.rdbuf(inStream_buf);
	cout.rdbuf(outStream_buf);
	return 0;
}
