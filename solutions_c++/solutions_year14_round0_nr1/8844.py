#include "stdafx.h"

#include <fstream>
#include <iostream>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;

void get_row_values(vector<int>& row_val, int ans, ifstream& in_file);

int _tmain()
{
    //File init
    ifstream in_file( "A-small-attempt0.in", ifstream::in );
    ofstream output_file( "output.txt", ostream::trunc);
    string line;

    //Get number of Test Cases
    int num_tc;
    in_file >> num_tc;
    getline(in_file, line);

    vector<int> row1(4);
    vector<int> row2(4);
    int ans;

    for(int tc=0; tc < num_tc; tc++ )
    {
        //Get first answer
        in_file >> ans;
        getline( in_file, line );
        get_row_values(row1, ans, in_file);

        in_file >> ans;
        getline(in_file, line);
        get_row_values(row2, ans, in_file);

        set<int> row2_set(row2.begin(), row2.end());

        int card_num = -1;
        for( int& r1 : row1 )
        {
            if( row2_set.count(r1) > 0 ) {
                if( -1 == card_num ) {
                    card_num = r1;
                }
                else {
                    card_num = -2;
                    break;
                }
            }
        }


        if( -2 == card_num ) {
            output_file << "Case #" << tc + 1 << ": " << "Bad magician!" << endl;
        }
        else if( -1 == card_num ) {
            output_file << "Case #" << tc+1 << ": " << "Volunteer cheated!" << endl;
        } else {
            output_file << "Case #" << tc+1 << ": " << card_num << endl;
        }
    }

    //Close all files
    in_file.close();
    output_file.close();
    return 0;
}

void get_row_values(vector<int>& in_row, int ans, ifstream& in_file)
{
    string line;

    //Skip to the target row
    for(int i = 0; i < ans - 1; i++ )
    {
        getline(in_file,line);
    }

    //Store the potential values
    getline(in_file, line);
    istringstream iss(line);
    int temp;
    int i = 0;
    while (iss >> temp) {
        in_row[i++] = temp;
    }

    for (int i = ans; i < 4; i++)
    {
        getline(in_file, line);
    }
}
