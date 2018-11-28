#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <stdio.h>

using namespace std;

class MagicTrick
{
public:
	MagicTrick() : 
	num_test(0),
	guess1(0),
	guess2(0),
	ans(0)	   		
	{

		for (int i =0; i <17; i++)
		{
			cards.push_back(0);
		}
	};
	
	~MagicTrick(){};
	
	void doMagic()
	{
		ifstream inFile("A-small-attempt0.in");
		ofstream outFile("output.txt");
		string line;
		const char* numbers;
		
		getline(inFile, line);
		num_test = atoi(line.c_str());
		
		//cout << line << endl;
		//cout << "Total tests are: " << num_test << endl;
		
		for (int t = 0; t<num_test; t++)
		{
		     getline(inFile, line);
		     guess1 = atoi(line.c_str());
		     //cout << "Guess 1 is: " << guess1 << endl;

		     int x, y, z, w;

		     for (int i = 0; i < guess1; i++)
		     {
			     getline(inFile, line);

		     }

		     sscanf(line.c_str(), "%d %d %d %d", &x, &y, &z, &w);
		     cards[x]++;
		     cards[y]++;
		     cards[z]++;
		     cards[w]++;

		     for (int i = 0; i < (4-guess1); i++)
			     getline(inFile, line);


		     getline(inFile, line);
		     guess2 = atoi(line.c_str());
		     //cout << "Guess 2 is: " << guess2 << endl;

		     for (int i = 0; i < guess2; i++)
			     getline(inFile, line);


		     sscanf(line.c_str(), "%d %d %d %d", &x, &y, &z, &w);
		     cards[x]++;
		     cards[y]++;
		     cards[z]++;
		     cards[w]++;

		     for (int i = 0; i < (4-guess2); i++)
			     getline(inFile, line);

		     ans = 0;
		     for (int i =0; i<17;i++)
		     {
		             if (cards[i] != 0)
			     	//cout << i << " = " << cards[i] << endl;
			     if (cards[i] == 2)
				     if (ans != 0)
					     ans = -1;
				     else
					     ans = i;

		     }
		     
		     
		     outFile << "Case #" << (t+1) << ": ";
		     if (ans == -1)
		        outFile << "Bad magician!" << endl;
	 	     else if (ans == 0)
		     	outFile << "Volunteer cheated!" << endl;
		     else
		     	outFile << ans << endl;
			
		     reset();

		}
		

	}
	
	void reset() 
	{
		for (int i =0; i < 17; i++)
			cards[i] = 0; 
	}
	
	
private:
	int num_test;
	int guess1;
	int guess2;
	vector<int> cards;
	int ans;
};

int main()
{

	MagicTrick mg;
	mg.doMagic();
	
	return 1;
}
