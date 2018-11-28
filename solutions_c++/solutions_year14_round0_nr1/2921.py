//
//  main.cpp
//  MagicTricks2014
//
//  Created by Jieming Shi on 12/4/14.
//  Copyright (c) 2014 Jieming Shi. All rights reserved.
//

#include <fstream>
#include <iostream>
#include <set>
#include <string>
#include <sstream>
#include <vector>
using namespace std;

//input file stream getter, no mode constraints
void ifstreamGetter(string path, ifstream &f)
{
	f.open(path);
	if (!f.is_open())
	{
		std::cout << "Err path: " << path << std::endl;
		exit(-1);
	}
}

void SeparateStringByDelimiter(string &input, char delimiter, vector<string>& output)
{
	//std::cout << line << endl;
	istringstream iss(input);
	string segment;
	//interpret this line
	while (getline(iss, segment, delimiter))
	{
		output.push_back(segment);
	}
}

void LoadTheRowInArrangement(ifstream &fi, int rid, set<string>& rowset)
{
    string line;
    vector<string> line_segments;
    
    //read the first arrangement
    int lcnt = 1;
    while ( lcnt <= 4 && getline(fi, line)) {
        if (lcnt == rid) {
            SeparateStringByDelimiter(line , ' ', line_segments);
            rowset.insert(line_segments.begin(), line_segments.end());
        }
        lcnt++;
        line.clear();
    }
}

int main(int argc, const char * argv[])
{
    // insert code here...
    ifstream fi;
    ifstreamGetter("../../../A-small-attempt0.in", fi);
    
    string line;
    vector<string> line_segments;

    
    //get number of test cases
    int T = 0;
    getline(fi, line);
    T = stoi(line);
    
    line.clear();
    
    //one case includes 10 lines
    int case_cnt = 1;
    int row1 = 0;
    set<string> set1;
    int row2 = 0;
    set<string> set2;
    
    
    while (getline(fi, line)) {
        //enter a new case whose first line is already read
        cout << "Case #" << case_cnt << ": ";
        
        row1 = stoi(line);
        line.clear();
        
        //read the row of first arrangement into set1
        LoadTheRowInArrangement(fi, row1, set1);
        
        //second arrangement
        getline(fi, line);
        row2 = stoi(line);
        line.clear();

        LoadTheRowInArrangement(fi, row2, set2);
        
        set<string> result;
        set_intersection(set1.begin(), set1.end(), set2.begin(), set2.end(), inserter(result, result.begin()));
        if (result.size() == 0) {
            cout << "Volunteer cheated!\n";
        }
        else if(result.size() == 1)
        {
            cout << *result.begin() << endl;
        }
        else
            cout << "Bad magician!\n";
        
        set1.clear();
        set2.clear();
        case_cnt++;
    }
    
    
    return 0;
}

