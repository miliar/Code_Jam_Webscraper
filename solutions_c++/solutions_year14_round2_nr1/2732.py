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
        int n;
        vector <string> words;
        vector <string> merged;

        vector <vector <int> > dupl;

        vector <int[100]> dist;

        string m;


        vector <int> actions;
        // = atoi(line.c_str());
        file >> count;
        //cout << count << " cases;" << endl;
        for(int i=1; i<=count; i++){

            cout << "Case #" << i << ": ";

            file >> n;
            if(file.peek() == '\n')
                file.ignore();
            //cout << n << endl;
            words.clear();
            merged.clear();
            dupl.clear();

            bool check = false;
            bool imp = false;

            for(int j=1; j<=n; j++){
                
                getline(file, line);
                //cout << "ans1: " << ans1 << endl;
                words.push_back(line);

                string s;
                unsigned sLen = 1;
                s=line[0];
                unsigned d = 1;

                vector<int> currD;
                currD.clear();

                for(int l=1; l<line.length(); l++)
                {
                    
                    if(line[l] != s[sLen-1])
                    {
                        s+=line[l];
                        currD.push_back(d);
                        d=1;
                        sLen++;
                    }
                    else
                        d++;
                }
                currD.push_back(d);

                merged.push_back(s);

                if(check && s != m)
                {
                    cout << "Fegla Won" << endl;
                    imp = true;

                    continue;
                }

                check = true;
                m = s;
/*
                cout << line << ", " << s << endl;
                for (vector<int>::iterator it = currD.begin() ; it != currD.end(); ++it)
                    cout << *it << ", ";
                cout << endl;*/

                dupl.push_back(currD);
            }
            if(!imp)
            {

                int total = 0;

                for (int j=0; j<m.length(); j++)
                {
                    int min = 100;
                    for (int k=1; k<=100; k++)
                    {                    
                        int r = 0;
                        for (vector<vector <int> >::iterator it = dupl.begin() ; it != dupl.end(); ++it)
                        {
                            r += abs((*it)[j] - k);

                        }
                        if (r<min)
                        {
                            min = r;
                            //cout << "k: " << k << " j: " << j << " abs: " << r << endl;
                        }
                    }
                    total+= min;
                }
                cout << total << endl;
            }
        }


        /*





        	cout << "Case #" << i << ": ";

        	switch (found)
        	{
        		case 0: cout << "Volunteer cheated!" << endl; break;
        		case 1: cout << lastFound << endl; break;
        		default: cout << "Bad magician!" << endl; break;
        	}*/
        
    
	return 0;
}