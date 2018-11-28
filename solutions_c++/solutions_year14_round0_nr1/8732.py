#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
	
	int T;
	cin >> T;
	int count=1;
	string out1= "Bad magician!";
	string out2= "Volunteer cheated!";

	while (count <= T){
		int deck1[4][4];
		int deck2[4][4];
		int row1[17]={0};
		int ans1;
		int ans2;
		
		cin >> ans1;
		for (int i = 0; i < 4; ++i)	{
			for (int j = 0; j < 4; ++j)	{
				cin >> deck1[i][j];
			}
		}

		for (int i = 0; i < 4; ++i)	{
			row1[deck1[ans1-1][i]]=1;
		}

		cin >> ans2;
		for (int i = 0; i < 4; ++i)	{
			for (int j = 0; j < 4; ++j)	{
				cin >> deck2[i][j];
			}
		}

		int matchFound=0;
		int result;
		for (int i = 0; i < 4; ++i)	{
			if (row1[deck2[ans2-1][i]]){
				matchFound++;
				result = deck2[ans2-1][i];
			}
		}

		cout << "Case #" << count << ": ";
		if (matchFound == 1){
			cout << result<<endl;
		}else if ( matchFound >1 ){
			cout << "Bad magician!"<<endl;
		}else if ( matchFound ==0){
			cout << "Volunteer cheated!"<<endl;
		}
		count++;
	}
	return 0;
}