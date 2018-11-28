#include<iostream>
using namespace std;
int main()
{
	int test, testcase;
	int g1, g2;
	int i, j;
	freopen("D:\\codejam\\A-small-attempt0.in", "r", stdin);
	freopen("D:\\codejam\\outa.in", "w", stdout);
	int first[5], second[5], save[5], temp, count = 0;
	cin >> testcase;
	for(test = 1;test<=testcase;test++)
	{
		cout << "Case #" << test <<": ";
		cin >> g1;
		count = 1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin >> temp;
				if(count == g1)
				{
					first[j] = temp;
				}
			}
			count++;
		}
		
		cin >> g2;
		count = 1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				cin >> temp;
				if(count == g2)
				{
					second[j] = temp;
				}
			}
			count++;
		}
		count = 0;
		int save = -1;
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
				if(first[i] == second[j])
				{
					save = first[i];
					count++;
				}
			}
		}

		if(count>1)
		{
			cout << "Bad magician!" << endl;
		}
		else if(count == 1)
		{
			cout << save << endl;
		}
		else
		{
			cout << "Volunteer cheated!" << endl;
		}
	}
	return 0;
}