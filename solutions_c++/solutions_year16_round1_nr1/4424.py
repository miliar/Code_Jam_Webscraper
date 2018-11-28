#include <fstream>
#include <string>
#include <iostream>
#include <cstdlib>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	ofstream myfile;
	myfile.open("output.txt");
	ifstream file("A-large.in");
    string str;
    
    if (file) {
        getline(file, str);
        int T = atoi(str.c_str());
		
		for (int t = 1; t <= T; ++t) {
			getline(file, str);
			string out;
			out.push_back(str[0]);
			for(int i = 1; i < str.length(); ++i) {
				cout << str[i] << endl;
				if (str[i] >= out[0])
					out.insert(0, 1, str[i]);
				else
					out.push_back(str[i]);
			}
			
			myfile << "Case #" << t << ": " << out << endl;
		}
    }
	myfile.close();
    return 0;
}