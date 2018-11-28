#include<iostream>
#include<string>
#include"ordered_list.h"
using namespace std;
int main()
{
	int t;
	cin >> t;
	for (int i = 0; i < t; i++)
	{
		int x, r, c;
		string winner="GABRIEL";
		cin >> x >> r >> c;
		if (r*c%x != 0)
			winner = "RICHARD";
		else
		{
			if (x==3&&r*c==3||(x==4&&(r*c == 4 || r*c == 8)))
			{
				winner = "RICHARD";
			}
		}
		cout << "case #" << i + 1 << ": "<< winner << endl;
	}


	return 0;
}