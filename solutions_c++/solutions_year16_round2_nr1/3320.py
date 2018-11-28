#include <iostream>
#include <vector>
#include <sstream>
#include <bitset>
#include <algorithm>
#include <cstdlib>
#include <cmath>
#include <string>

#define SZ(x) (int)(x.size())
#define F0(i,n) for(int i=0;i<n;i++)
#define F1(i,n) for(int i=1;i<=n;i++)

using namespace std;

int main() {
	
	string line;

	getline(cin, line); // get n case

	int nCase = 0;
	vector<string> n;
	n.push_back("TWO");
	n.push_back("ZERO");
	n.push_back("SIX");
	n.push_back("FOUR");
	n.push_back("THREE");
	n.push_back("EIGHT");
	n.push_back("FIVE");
	n.push_back("SEVEN");
	n.push_back("ONE");
	n.push_back("NINE");
	vector<int> nn;
	nn.push_back(2);
	nn.push_back(0);
	nn.push_back(6);
	nn.push_back(4);
	nn.push_back(3);
	nn.push_back(8);
	nn.push_back(5);
	nn.push_back(7);
	nn.push_back(1);
	nn.push_back(9);

	while(getline(cin, line)) // actual cases
	{
		cout << "Case #" << ++nCase << ": ";
string ss=line;
		vector<int> r;
		int i,j,o,p;

		F0(i,SZ(n))
		{
			F0(p,2000)
			{
				int cnt = 0;
				string temp = line;
				F0(j,SZ(n[i]))
				{
					F0(o,SZ(temp))
					{
						if (n[i][j]==temp[o])
						{
							temp[o]='-';
							cnt++;
							break;
						}
					}
					if (cnt==0)
						break;
				}

				if (SZ(n[i])==cnt)
				{
					r.push_back(nn[i]);
					line=temp;
				}

				if (cnt==0)
					break;
			}
		}

		sort(r.begin(),r.end());
		F0(x,SZ(r))
		{
			cout << r[x] ;
		}
		

		cout << endl;
	}

	return 0;
}