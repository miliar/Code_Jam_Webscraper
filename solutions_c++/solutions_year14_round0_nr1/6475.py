#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <iterator>
#include <fstream>
using namespace std;
int main()
{
	ifstream in("A-small-attempt6.in");
	ofstream out("o.out");


	//istringstream in(fin);
	int T;
	in >> T;
	int loop = 1;
	while (T--)
	{
		int cards1[4][4] = { { 1, 2, 3, 4 }, { 5, 6, 7, 8 }, { 9, 10, 11, 12 }, { 13, 14, 15, 16 } };
		int cards2[4][4] = { { 1, 2, 5, 4 }, { 3, 1, 6, 15 }, { 9, 10, 7, 12 }, { 13, 14, 8, 16 } };
		int n1 = 2;
		int n2 = 3;
		int cover[4] = { 0 };

		in >> n1;
		cout << n1 << endl;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				in >> cards1[i][j];
				cout << cards1[i][j] << " ";
			}
			cout << endl;
		}
		in >> n2;
		cout << n2 << endl;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				in >> cards2[i][j];
				cout << cards2[i][j] << " ";
			}
			cout << endl;
		}

		n1--;
		n2--;
		int count = 0;
/*		int bad = 0;


		for (int i = 0; i < 4; i++)
		for (int j = 0; j < 4; j++)
		for (int k = 0; k < 4; k++)
		if (cards2[j][k] == cards1[n1][i])//找这个数字
			cover[j] = 1;

		for (int i = 0; i < 4; i++)
		if (cover[i] == 1)
			count++;
		if (count < 4)
			bad = 1;

			*/

		int number = 0;
		count = 0;
		for (int i = 0; i < 4; i++)//遍历牌堆一中n1行的所有元素
		{
			for (int j = 0; j < 4; j++)//遍历牌堆二n2行中所有元素
			{
				if (cards1[n1][i] == cards2[n2][j])
				{
					//if (!bad)
					count++;
					number = cards1[n1][i];
						//找到了
				}
				//else count++;

			}
		}
		//cout << count << endl;
		if (count==1)
			out << "Case #" << loop << ": " << number << endl;//
		else if (count ==0)//没找到,cheat
			out << "Case #" << loop << ": " << "Volunteer cheated!" << endl;

		else if(count>0)
			out << "Case #" << loop << ": " << "Bad magician!" << endl;
		loop++;
		//getchar();
	}

	//getchar();
	//getchar();
}