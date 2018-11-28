// GoogleCodeJam2014Cplusplus.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <fstream>
#include <string>
#include <list>
#include <vector>
#include <math.h>

using namespace std;



int main()
{

    ifstream input("A-small-attempt1.in");
    ofstream output("Output.txt");

    vector<string> lst;
            
    int amountOfTasks;

	input >> amountOfTasks;

    int amountOfLines = 0;

    int countt = 0;
    bool possible = true;
    int amount = 0;
    char temp = ' ';

    for (int i = 1; i <= amountOfTasks; i++)
    {
        countt = 0;
        possible = true;
        amount = 0;

        input >> amountOfLines;

        vector<vector<pair<char, int>>> maps;
		maps.clear();

        for (int j = 0; j < amountOfLines; j++)
        {
			string line;
			input >> line;
			vector<pair<char, int>> temp;
			temp.clear();
			temp.push_back(make_pair(line[0], 1));
			for(int k = 1; k < line.size(); k++)
			{
				if(line[k] == temp.back().first)
				{
					temp.back().second++;
				}
				else
				{
					temp.push_back(make_pair(line[k], 1));
				}
			}
			maps.push_back(temp);
        }

		for (int j = 1; j < amountOfLines; j++)
        {
			if(maps[j].size() != maps[j-1].size())
			{
				possible = false;
				break;
			}
        }

		if(possible)
		{

		for(int k = 0; k < maps[0].size(); k++)
		{
			if(possible == false)
			{
				break;
			}
			auto it = maps[0].begin();
			advance(it, k);

			amount =  it->second;
			for (int j = 1; j < amountOfLines; j++)
			{
				auto it1 = maps[j-1].begin();
				auto it2 = maps[j].begin();
				advance(it1, k);
				advance(it2, k);

				if(it1->first != it2->first)
				{
					possible = false;
					break;
				}

				amount += it2->second;
			}

			if(amount % maps.size() > 5)
				amount += (maps.size() - amount % maps.size());
			amount /= maps.size();

			for (int j = 0; j < amountOfLines; j++)
			{
				
				auto it2 = maps[j].begin();
				
				advance(it2, k);

				countt += abs(amount - it2->second);
			}
		}
		}


        if (!possible)
        {
            output << "Case #" << i <<": Fegla Won\n";
        }
        else
        {
            output << "Case #" << i <<": " << countt << "\n";
        }

    }

    input.close();
    output.close();
	return 0;
}



