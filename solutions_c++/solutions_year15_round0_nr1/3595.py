#include <fstream>
#include <iostream>
#include <string>

using namespace std;


int main()
{
	/*int a[10] = {6,2,8,1,0,4,7,3,9,5};
	int tmp,i,j;

	for (i = 1; i<10; i++)
	{
		tmp = a[i];

		for (j = i - 1; j > 0; j--)
		{
			if (a[j] > tmp)
			{
				a[j + 1] = a[j];
			}
			else
				break;
		}

		a[j + 1] = tmp;

	}


	cout << a[7] << "  " << a[8] << "  " << a[9] << "  " << endl;*/


	ofstream out("output.txt");
	ifstream in("A-large.in");
	int n, m, ans, tmp;
	string num;
	in >> n;

	for (int j = 0; j < n; j++)
	{
		tmp = 0;
		ans = 0;
		in >> m;
		in >> num;


		for (int i = 1; i < num.length(); i++)
		{
			tmp += num[i - 1] - 48;

			if (tmp < i)
			{
				ans += i - tmp;
				tmp += i - tmp;
			}
		}


		out << "Case #" << j + 1 << ": " << ans << endl;
	}
	

	return 0;
}


