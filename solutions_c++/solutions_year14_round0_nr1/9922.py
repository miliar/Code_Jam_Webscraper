#include <string>
#include <sstream>
#include <array>
#include <iostream>
#include <fstream>
using namespace std;

int main(){
	
	fstream fs;
	fs.open("A-small-attempt6.in", fstream::in);
	string inStr;
	fstream fs2;
	fs2.open("output.txt", fstream::out);

	getline(fs, inStr);
	int tests = atoi(inStr.c_str());
	int answer;


	for(int n=0;n<tests;n++)
	{
		int cards[4][4] = {0};
		int cards2[4][4] = {0};

		getline(fs, inStr);
		int first = atoi(inStr.c_str())-1;


		for(int i=0;i<4;i++)
		{
			string cardrow;
			getline(fs, cardrow);
			istringstream iss(cardrow);
			int cardnum;
			int j=0;
			while(iss>>cardnum)
			{
				cards[i][j] = cardnum;
				j++;
			}	

		}
		getline(fs, inStr);

		int second = atoi(inStr.c_str())-1;

		for(int i=0;i<4;i++)
		{
			string cardrow2;
			getline(fs, cardrow2);
			istringstream iss(cardrow2);
			int cardnum2;
			int j=0;
			while(iss>>cardnum2)
			{
				cards2[i][j] = cardnum2;
				j++;
			}
		}

		int magiciancheck[17] = {0};
		int matches=0;

		for(int i=0;i<4;i++){
			magiciancheck[cards[first][i]]++;
			magiciancheck[cards2[second][i]]++;
		}

		for(int i=1;i<=16;i++){
			if(magiciancheck[i]==2){
				matches++;
				answer = i;
			}
		}

		fs2<<"Case #"<<n+1<<": ";
		if(matches>1) fs2 <<"Bad magician! \n";
		else if(matches==0) fs2<<"Volunteer cheated! \n";
		else fs2<< answer<<"\n";
	}

	
		fs2.close();
		return 0;
}