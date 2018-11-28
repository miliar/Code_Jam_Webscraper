#include <iostream>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	int T;
	string if_name ="D-small-attempt0.in",of_name = "answerD.txt";
	ifstream input(if_name.c_str());
	ofstream output(of_name.c_str());
	input>>T;
	for (int i = 0;i < T;i++)
	{
		int X,R,C;
		input>>X>>R>>C;
		if (R < C) swap(R,C);
		string winner;
		switch (X)
		{
		case 1:
			winner = "GABRIEL";
			break;
		case 2:
			if (R%2 == 0 || C%2 == 0) winner = "GABRIEL";
			else winner = "RICHARD";
			break;
		case 3:
			if ((R%3 == 0 && C > 1) || (C % 3 == 0 && R > 1)) winner = "GABRIEL";
			else winner = "RICHARD";
			break;
		case 4:
			if (R < 4 || C < 3){
				winner = "RICHARD";
				break;
			}
			if (R%4 == 0 || C%4 == 0 || (R%2 == 0 && C%2 == 0))	winner = "GABRIEL";
			else winner = "RICHARD";
			break;
		}
		output<<"Case #"<<i+1<<": "<<winner<<endl;
	}

	return 0;
}