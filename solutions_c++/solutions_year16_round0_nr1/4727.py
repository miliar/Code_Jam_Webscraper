#include <fstream>
#include <iostream>
#include <vector>
using namespace std;


int main()
{
	ifstream in("A-large.in");
	ofstream out("1.txt");
	int T, i, j;
	long n, tmp, tmp1;
	bool num[10], flag, flag1;
	in >> T;
	for (i = 0; i < T; i++)
	{
		in >> n;
		out << "Case #"<< i + 1 <<": ";
		if (n == 0) 
			out << "INSOMNIA" << endl;
		else
		{
			flag1 = true;
			for (j = 0; j < 10; j++)
				num[j] = false;
			tmp = n;
			while (flag1)
			{
				flag = true;
				tmp1 = tmp;
				while (tmp1 > 0)
				{
					num[tmp1 % 10] = true;
					tmp1 /= 10;
				}
				for (j = 0; j < 10; j++)
					if (!num[j])
						flag = false;
				if (flag)
					break;
				tmp += n;
			}
			out << tmp << endl;
		}
	}
}