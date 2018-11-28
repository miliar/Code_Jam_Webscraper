#include <string>
#include <iostream>
#include <fstream>
#include <sstream>
#include <stdlib.h>
#include <iterator>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
	ifstream file("test.inp", ifstream::in);
    if (!file) {
            string error_message = "No valid input file was given, please check the given filename.";
            cout << error_message;
        }
        string line;
        //getline(file, line);
        int count;
        int ans1, ans2;
        int s11, s12, s13, s14, s21, s22, s23, s24;
        vector<int> s1;
        int s2;
        // = atoi(line.c_str());
        file >> count;
        //cout << count << " cases;" << endl;
        for(int i=1; i<=count; i++){
        	vector<int> s1;
        	int s2;
        	//cout << "case " << i << endl;
        	file >> ans1;
        	getline(file, line);
        	//cout << "ans1: " << ans1 << endl;
        	for(int j=1; j<5; j++)
        	{
        		if (j==ans1)
        		{
        			for(int k=0; k<4; k++)
		        	{
		        		int val;
		        		file >> val;
		        		s1.push_back(val);
		        	}
		        	getline(file, line);
        		}
        		else
        		{
        			getline(file, line);
        			//cout << "discarded: " << line << endl;
        		}

        	}

        	int found = 0;
        	int lastFound;

        	file >> ans2;
        	getline(file, line);
        	for(int j=1; j<5; j++)
        	{
        		if (j==ans2)
        		{
        			for(int k=0; k<4; k++)
		        	{
		        		file >> s2;
		        		//int *pos = find(s1, s1+4, s2);
		        		if(find(s1.begin(), s1.end(), s2) != s1.end()){
		        			lastFound = s2;
		        			found ++;
		        		}
		        		

		        	}
		        	getline(file, line);
        		}
        		else
        		{
        			getline(file, line);        			
        			//cout << "discarded: " << line << endl;
        		}
        	}

        	cout << "Case #" << i << ": ";

        	switch (found)
        	{
        		case 0: cout << "Volunteer cheated!" << endl; break;
        		case 1: cout << lastFound << endl; break;
        		default: cout << "Bad magician!" << endl; break;
        	}
        }
	return 0;
}
