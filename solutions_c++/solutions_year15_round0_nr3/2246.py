#include<iostream>
#include<fstream>
#include<vector>

using namespace std;

int main()
{
	ifstream in("in.txt");
	ofstream out("out.txt");
	int T;
	in >> T;

	int a[5][5];
	a[1][1] = 1;
	a[1][2] = 2;
	a[1][3] = 3;
	a[1][4] = 4;
	a[2][1] = 2;
	a[2][2] = -1;
	a[2][3] = 4;
	a[2][4] = -3;
	a[3][1] = 3;
	a[3][2] = -4;
	a[3][3] = -1;
	a[3][4] = 2;
	a[4][1] = 4;
	a[4][2] = 3;
	a[4][3] = -2;
	a[4][4] = -1;

	for (int k = 1; k <= T; k++)
	{
		bool result;
		int L;
		long long X;
		in >> L >> X;
		vector<int> v(L);
		for (size_t i = 0; i < L; i++)
		{
			char c;
			in >> c;
			v[i] = c - 'g';
		}

		
		bool findi = false; int findiloop = 0;
		bool findk = false; int findkloop = 0;
		bool p = true;
		int s = 1;
		for (int j = 1; j <= 8+X%8 && j<= X; j++)
		{
			for (int i = 0; i < L; i++)
			{
				s = a[s][v[i]];
				if (s < 0)
				{
					s = -s;
					p = !p;
				}
				if (findi == false && s == 2 && p == true)
				{
					findi = true;
					findiloop = j;
				}
				if (findi == true && findk == false && s == 4 && p == true)
				{
					findk = true;
					findkloop = j;
				}
			}
		}
		if (findi == true && findk == true && findkloop <= X && s==1 && p == false)
		{
			result = true;
		}
		else
		{
			result = false;
		}



		


		if (result == true)
		{
			out << "Case #" << k << ": " <<"YES"<< endl;
			cout << "Case #" << k << ": " <<"YES"<< endl;
		}
		else
		{
			out << "Case #" << k << ": " << "NO" << endl;
			cout << "Case #" << k << ": " << "NO" << endl;
		}
		

	}


	out.close();
	in.close();
}