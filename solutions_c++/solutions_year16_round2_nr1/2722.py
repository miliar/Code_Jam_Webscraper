#include <vector>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <string>
#include <map>

using namespace std;

int main()
{
    //ifstream fin("input.in");
    ifstream fin("A-large.in");
   // ifstream fin("D-large.in");
    ofstream fout("output.out");

    //-- check if the files were opened successfully
    if (!fin.is_open()) cout << "input.in was not opened successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;
    int numCase;
    fin >> numCase;

    int smax = 0;
    std::string number;
    for (int i = 0; i < numCase; i++)
    {
        fin >> number;
        //cout << number << endl;
        std::map<int, int> finalNumber = {{0,0}, {1,0}, {2,0}, {3,0},
                                          {4,0},{5,0},{6,0},{7,0},{8,0},{9,0}};

        std::map<char, int> m = {{'Z',0}, {'E', 0},{'R', 0}, {'O', 0},
                            {'N', 0},{'T',0},{'W', 0},{'H', 0}, {'F', 0}, {'U', 0},
                            {'I', 0}, {'V', 0}, {'S', 0}, {'X', 0}, {'G',0}};

        for(auto &c : number)
        {
            //cout << c << endl;

            m[c]++;
            //cout << m[c] << endl;
        }

        while (m['Z'] > 0)
        {
            //cout << "m['Z'] > 0" << endl;
            m['Z']--;
            m['E']--;
            m['R'] --;
            m['O'] --;
            finalNumber[0]++;
        }

        while (m['W'] > 0)
        {
            m['T']--;
            m['W']--;
            m['O'] --;
            finalNumber[2]++;
        }
        while (m['X'] > 0)
        {
            m['S']--;
            m['I']--;
            m['X'] --;

            finalNumber[6]++;
        }
        while (m['G'] > 0)
        {
            m['E']--;
            m['I']--;
            m['G'] --;
            m['H'] --;
            m['T'] --;
            finalNumber[8]++;
        }

        while (m['S'] > 0)
        {
            m['S']--;
            m['E']--;
            m['E'] --;
            m['V'] --;
            m['N'] --;
            finalNumber[7]++;
        }
        while (m['T'] > 0)
        {
            m['T']--;
            m['H']--;
            m['R'] --;
            m['E'] --;
            m['E'] --;
            finalNumber[3]++;
        }

        while (m['V'] > 0)
        {
            m['F']--;
            m['I']--;
            m['V'] --;
            m['E'] --;
            finalNumber[5]++;
        }

        while (m['I'] > 0)
        {
            m['N']--;
            m['I']--;
            m['N'] --;
            m['E'] --;
            finalNumber[9]++;
        }
        while (m['R'] > 0)
        {
            m['F']--;
            m['O']--;
            m['U'] --;
            m['R'] --;
            finalNumber[4]++;
        }
        while (m['O'] > 0)
        {
            m['O']--;
            finalNumber[1]++;
        }

        string nr;

        for (auto &n : finalNumber)
        {
            //cout << n.first << " " << n.second <<endl;
            for (int  i = 0; i < n.second; ++i)
            {
                nr.append(std::to_string(n.first));
                //cout << nr << endl;
            }
        }
        //cout << nr << endl;

        fout << "Case #" << (i + 1) << ": " << nr<< endl;
    }
    fin.close();
    fout.close();
    return 0;
}
