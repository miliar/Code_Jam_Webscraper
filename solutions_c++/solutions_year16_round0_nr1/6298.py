#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <iostream>
#include <string>
#include<vector>
using namespace std;
//typedef long long LL;

int main() {
	FILE *fin = freopen("A-large.in", "r", stdin);
	assert(fin != NULL);
	FILE *fout = freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;
	//cout<<"T: "<<T<<endl;
	long long int num;
	for (int t = 1; t <= T; t++)
	{
		cin >> num;
		//cout << "NUM: " << num << endl;


		if (num == 0)
		{
			cout << "Case #" << t << ": INSOMNIA" << endl;
		}
		else
		{
			vector<char> seen(10, 'n');
			int cont = 10;
			long long int mult = 1;
			long long int cnum;
			while (cont)
			{
				//num *= mult;

				cnum = num * mult;
				mult++;
				int test;
				while (cnum)
				{
					test = cnum % 10;
					cnum = cnum / 10;
					if (seen[test] == 'n')
					{
						seen[test] = 'y';
						cont--;
					}
				}
				//cout<<"cont: "<<cont<<endl;
			}

			cout << "Case #" << t << ": " << num * (mult -1) << endl;
		}
	}
	exit(0);
}















