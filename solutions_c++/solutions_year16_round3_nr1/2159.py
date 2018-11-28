#include <iostream>
#include <string>
#include <fstream>
#include <sstream>
#include <vector>
#include <cstdlib>
using namespace std;

vector <int> party;
int main(int argc, char *argv[])
{
	fstream fin;
	fin.open(argv[1], ios::in);
	string input;
	getline(fin, input);
	
	int num = 0;
	int max = 0;
	int max_index = 0;
	int max_index2 = 0;
	bool move2 = false;
	bool end = true;
	int sum = 0;
	int counter = 0;
	int not0 = 0;
	while(getline(fin, input))
	{
		getline(fin, input);
		++counter;
		istringstream ss(input);
		cout<<"Case #"<<counter<<": ";
		party.clear();
		while(ss>>num)
		{
			party.push_back(num);
			num = 0;
		}
		end = true;
		max_index = 0;
		max_index2 = 0;
		max = 0;
		move2 = false;
		sum = 0;
		while(end)
		{
			not0 = 0;
			for(int i = 0; i < party.size(); ++i)
			{
				if(party[i]!=0)
					not0++;
				if(max < party[i])
				{
					max = party[i];
					max_index = i;
				
				}
				else if(max == party[i])
					max_index2 = i;	
			}
			if(party[max_index]==party[max_index2])
				move2 = true;
			else
				move2 = false;
			if(!move2)
			{
				party[max_index]--;
				cout<<(char)(max_index+65)<<" ";
			}
			else if(party[max_index]!=1)
			{
				party[max_index]--;
				party[max_index2]--;
				cout<<(char)(max_index+65)<<(char)(max_index2+65)<<" ";
			}
			else if(not0>3)
			{
				party[max_index]--;
				party[max_index2]--;
				cout<<(char)(max_index+65)<<(char)(max_index2+65)<<" ";
			
			}
			else if(not0==3)
			{
				party[max_index]--;
				cout<<(char)(max_index+65)<<" ";
			}
			else
			{
				party[max_index]--;
				party[max_index2]--;
				cout<<(char)(max_index+65)<<(char)(max_index2+65)<<" ";
			}
			max = 0;
			max_index2 = 0;
			max_index = 0;
			for(int i = 0; i < party.size(); ++i)
			{
				sum+=party[i];
			}
			if(sum!=0)
				end = true;
			else
				end = false;
			sum = 0;
		}		
		cout<<endl;
	}
	return 0;
}










