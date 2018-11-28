#include <iostream>
#include <vector>
#include<string>
using namespace std;
int main()
{
	vector<int> Flag;
	typedef vector<vector<int> > shuzu;
	shuzu a;
	vector<vector<int> > vec;
	vector<int> result;
//cin;
	int T;
	cin >> T;
//cin T groups number
	for (int i = 0; i != T; i++)
	{
        int er(0);
		int flag(0);
		int answer[2];
		//cin one group number
		for (int j = 0; j != 2; j++)
		{
			cin >> answer[j];
			for (int m = 0; m != 4; m++)
			{
				vector<int> Temp;
				for (int n = 0; n != 4; n++)
				{
					int temp;
					cin >> temp;
					Temp.push_back(temp);
				}
				vec.push_back(Temp);
			}
		}
		for (int m = 0; m != 4; m++)
		{

			for (int n = 0; n != 4; n++)
			if (vec[answer[0]-1][m] == vec[answer[1]+3][n])
			{
                er=1;
				flag++;
				if(flag==1)
				result.push_back(vec[answer[0]-1][m]);
			}
		}
		if(er==0)
		result.push_back(0);
		else
        er=0;


		Flag.push_back(flag);
		vec.clear();
	}
	for (int i = 0; i != T; i++)
	{
		if (Flag[i] == 0)
			cout << "Case #" << i + 1 << ": " << "Volunteer cheated!" << endl;
		else if (Flag[i] == 1)
			cout << "Case #" << i + 1 << ": " << result[i]<< endl;
		else
			cout << "Case #" << i + 1 << ": " <<"Bad magician!"<< endl;
	}
	Flag.clear();
	result.clear();
	return 0;

}

