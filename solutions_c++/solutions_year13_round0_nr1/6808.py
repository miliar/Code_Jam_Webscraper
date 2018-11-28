#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdlib>
using namespace std;

#define REP(i, n) for(int i=0;i<n;i++)
#define rep(n) REP(i,n)

int main()
{
	int problem_num;
	string tmp;
	string winner = "";
	vector<string> clum;
	vector<string> ox;
	ox.push_back("O");
	ox.push_back("X");
	cin >> problem_num;
	rep(problem_num)
	{
		winner = "";
		clum.clear();
		for(int j=0; j<4; j++)
		{
			cin >> tmp;
			clum.push_back(tmp);
		}

		// tate
		// yoko
		for (int j=0; j<ox.size(); j++)
		{
			for(int k=0; k<4; k++)
			{
				//cout << "clum[0][k] " << clum[0][k] << endl;
				//cout << "clum[1][k] " << clum[1][k] << endl;
				//cout << "clum[2][k] " << clum[2][k] << endl;
				//cout << "clum[3][k] " << clum[3][k] << endl;

				if ((clum[0][k] == ox[j][0] || clum[0][k] == 'T') 
				&& (clum[1][k] == ox[j][0] || clum[1][k] == 'T') 
				&& (clum[2][k] == ox[j][0] || clum[2][k] =='T') 
				&& (clum[3][k] == ox[j][0] || clum[3][k] == 'T'))
				{
					winner = ox[j] + " won";
					break;
				}
				if ((clum[k][0] == ox[j][0] || clum[k][0] == 'T') 
				&& (clum[k][1] == ox[j][0] || clum[k][1] == 'T') 
				&& (clum[k][2] == ox[j][0] || clum[k][2] =='T') 
				&& (clum[k][3] == ox[j][0] || clum[k][3] == 'T'))
				{
					winner = ox[j] + " won";
					break;
				}
			}
		}
		// naname
		if (winner == "")
		{
			for (int j=0; j<ox.size(); j++)
			{
				if ((clum[0][0] == ox[j][0] || clum[0][0] == 'T') 
				&& (clum[1][1] == ox[j][0] || clum[1][1] == 'T') 
				&& (clum[2][2] == ox[j][0] || clum[2][2] == 'T') 
				&& (clum[3][3] == ox[j][0] || clum[3][3] == 'T'))
				{
					winner = ox[j] + " won";
					break;
				}
				if ((clum[0][3] == ox[j][0] || clum[0][3] == 'T') 
				&& (clum[1][2] == ox[j][0] || clum[1][2] ==  'T') 
				&& (clum[2][1] == ox[j][0] || clum[2][1] == 'T') 
				&& (clum[3][0] == ox[j][0] || clum[3][0] == 'T'))
				{
					winner = ox[j] + " won";
					break;
				}

			}
		}
		// draw
		if (winner == "")
		{
			for(int j =0; j<4; j++)
			{
				if(clum[j].find_first_of(".") != string::npos)
				{
					winner = "Game has not completed";
					break;
				}
			}
		}
		
		if (winner == "")
			winner = "Draw";

		cout << "Case #" << i+1 << ": " << winner << endl;

	}
	return 0;
}
