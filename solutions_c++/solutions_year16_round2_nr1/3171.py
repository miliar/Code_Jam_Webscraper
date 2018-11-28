#include <iostream>
#include <sstream>
#include <fstream>
#include <string>
#include <vector>
#include <map>

using namespace std;


const bool OUTPUT_TO_FILE = true;


int main()
{
	cout.sync_with_stdio(false);
	stringstream output;

	int t;
    int ans;
	string s;
    int lim;

    map<char,int> number_map;
    number_map['Z'] = 0;
    number_map['E'] = 1;
    number_map['R'] = 2;
    number_map['O'] = 3;
    number_map['N'] = 4;
    number_map['T'] = 5;
    number_map['W'] = 6;
    number_map['H'] = 7;
    number_map['F'] = 8;
    number_map['U'] = 9;
    number_map['I'] = 10;
    number_map['V'] = 11;
    number_map['S'] = 12;
    number_map['X'] = 13;
    number_map['G'] = 14;

    int count[15];
    int num_count[10];

	cin >> t;
    getline(cin, s);
	for (int run = 1; run <= t; run++)
	{
	    ans = 0;

        for (int i = 0; i < 15; i++)
        {
            count[i] = 0;
        }
        for (int i = 0; i < 10; i++)
        {
            num_count[i] = 0;
        }

	    getline(cin, s);

        for (char c : s)
        {
            count[number_map[c]]++;
        }

        lim = count[number_map['Z']];
        for (int i = 0; i < lim; i++)
        {
            ans++;
            count[number_map['Z']]--;
            count[number_map['E']]--;
            count[number_map['R']]--;
            count[number_map['O']]--;
            num_count[0]++;
        }

        lim = count[number_map['W']];
        for (int i = 0; i < lim; i++)
        {
            ans++;
            count[number_map['T']]--;
            count[number_map['W']]--;
            count[number_map['O']]--;
            num_count[2]++;
        }

        lim = count[number_map['X']];
        for (int i = 0; i < lim; i++)
        {
            ans++;
            count[number_map['S']]--;
            count[number_map['I']]--;
            count[number_map['X']]--;
            num_count[6]++;
        }

        lim = count[number_map['G']];
        for (int i = 0; i < lim; i++)
        {
            ans++;
            count[number_map['E']]--;
            count[number_map['I']]--;
            count[number_map['G']]--;
            count[number_map['H']]--;
            count[number_map['T']]--;
            num_count[8]++;
        }

        lim = count[number_map['U']];
        for (int i = 0; i < lim; i++)
        {
            ans++;
            count[number_map['F']]--;
            count[number_map['O']]--;
            count[number_map['U']]--;
            count[number_map['R']]--;
            num_count[4]++;
        }

        lim = count[number_map['F']];
        for (int i = 0; i < lim; i++)
        {
            ans++;
            count[number_map['F']]--;
            count[number_map['I']]--;
            count[number_map['V']]--;
            count[number_map['E']]--;
            num_count[5]++;
        }

        lim = count[number_map['H']];
        for (int i = 0; i < lim; i++)
        {
            ans++;
            count[number_map['T']]--;
            count[number_map['H']]--;
            count[number_map['R']]--;
            count[number_map['E']]--;
            count[number_map['E']]--;
            num_count[3]++;
        }

        lim = count[number_map['O']];
        for (int i = 0; i < lim; i++)
        {
            ans++;
            count[number_map['O']]--;
            count[number_map['N']]--;
            count[number_map['E']]--;
            num_count[1]++;
        }

        lim = count[number_map['S']];
        for (int i = 0; i < lim; i++)
        {
            ans++;
            count[number_map['S']]--;
            count[number_map['E']]--;
            count[number_map['V']]--;
            count[number_map['E']]--;
            count[number_map['N']]--;
            num_count[7]++;
        }

        lim = count[number_map['I']];
        for (int i = 0; i < lim; i++)
        {
            ans++;
            count[number_map['N']]--;
            count[number_map['I']]--;
            count[number_map['N']]--;
            count[number_map['E']]--;
            num_count[9]++;
        }

		output << "Case #" << run << ": ";
        for (int d = 0; d < 10; d++)
        {
            for (int j = 0; j < num_count[d]; j++)
            {
                output << d;
            }
        }
        output << "\n";
	}

	if (OUTPUT_TO_FILE)
	{
		ofstream output_file;
		output_file.open("out.txt");
		output_file << output.rdbuf();
		output_file.close();
	}
	else
	{
		cout << output.rdbuf();
	}
}
