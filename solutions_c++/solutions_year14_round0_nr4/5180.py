#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <cstdlib>
#include <stdio.h>
#include <algorithm>

using namespace std;

class War
{
public:
	War() : 
	num_test(0),
	num_blocks(0),
	guess2(0),
	ans(0)	   		
	{};
	
	~War(){};
	
	void go()
	{
		//ifstream inFile("D-small-attempt0.in");
		ifstream inFile("D-large.in");
		//ifstream inFile("small.in");
		ofstream outFile("output.txt");
		string line;
		float x;

		
		getline(inFile, line);
		num_test = atoi(line.c_str());
		
		//cout << "Total tests are: " << num_test << endl;
		
		for (int t = 0; t<num_test; t++)
		{
			inFile >> num_blocks;
			
			for (int i = 0; i < num_blocks; i++)
		     	{
				inFile >> x;
				naomi.push_back(x);
			}
			
			for (int i = 0; i < num_blocks; i++)
		     	{
				inFile >> x;
				ken.push_back(x);
			}
			
			sort(naomi.begin(), naomi.end());
			sort(ken.begin(), ken.end());
			
			//show();
			outFile << "Case #" << t+1 << ": " << playDeceitfulWar() << " " << playWar() << endl;
			
			reset();	
		}
			


	}
	
	int playWar()
	{
		int count=0;
		int n_cnt=0;
		int k_cnt=0;
		int size=naomi.size();  
		
		while ((n_cnt<size) && (k_cnt<size))
		{
			//cout << "N: " << naomi[n_cnt] << ", K: " << ken[k_cnt] << endl;
			if (naomi[n_cnt] > ken[k_cnt])
			{
				k_cnt++;
			}
			else
			{
				n_cnt++;
				k_cnt++;			
			}
		}
		
		return size-n_cnt;
	}
	
	int playDeceitfulWar()
	{
		int count=0;
		int n_cnt=naomi.size()-1;
		int k_cnt=ken.size()-1;
		
		while ((n_cnt>=0) && (k_cnt>=0))
		{
			//cout << "N: " << naomi[n_cnt] << ", K: " << ken[k_cnt] << endl;
			if (naomi[n_cnt] > ken[k_cnt])
			{
				count++;
				n_cnt--;
				k_cnt--;
			}
			else
			{
				k_cnt--;			
			}
		}
		
		return count;
	}
	
	void reset()
	{
		naomi.clear();
		ken.clear();
	}
	
	void show()
	{
		cout << endl << endl;
	       cout << "Naomi" << endl;
	       for (int i = 0;i<num_blocks;i++)
	       {
		       cout << naomi[i] << " ";
	       }
	       cout << endl;

	       cout << "Ken" << endl;
	       for (int i = 0;i<num_blocks;i++)
	       {
		       cout << ken[i] << " ";
	       }
	       cout << endl;
	}
	
	
	
private:
	int num_test;
	int num_blocks;
	int guess2;
	vector<float> naomi;
	vector<float> ken;
	int ans;
};

int main()
{

	War mg;
	mg.go();
	
	return 1;
}
