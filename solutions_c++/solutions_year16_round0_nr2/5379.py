#include <iostream>
#include <vector>
#include <fstream>
#include <string>

using namespace std;

int flips;

bool happyPlate(vector<bool>& plate)
{
    for (bool p : plate)
        if (p == false)
            return false;
    return true;
}

void flipPancake (vector<bool>& plate, int i)
{
    for (unsigned int k=0; k<plate.size(); k++)
        if (plate[k] == true)
            cout << "+";
        else
            cout << "-";
    cout << endl;
    vector<bool> tmp = plate;
    for (int k=0; k<=i; k++)
        plate[k]=!tmp[i-k];
    flips++;
}

int main(int argc, char *argv[])
{
    ifstream infile(argv[1]);
    ofstream outfile("output.txt", fstream::trunc);
    int T;
    infile >> T;
    for (int i=0; i<T; i++)
    {
        flips = 0;
        vector<bool> plate;
        string s;
        infile >> s;
        for (unsigned int j=0; j<s.size(); j++)
            if (s[j] == '+')
                plate.push_back(true);
            else
                plate.push_back(false);
        while (!happyPlate(plate))
        {
            int bottomSad=-1;
            int topHappy=0;
            for (int j=plate.size()-1; j>=0 && bottomSad < 0; j--)
            {
                if (plate[j] == false)
                    bottomSad = j;
            }
            if (plate[0] == false)
                flipPancake(plate, bottomSad);
            else
            {
                for (int j=0; plate[j] == true; j++)
                    topHappy=j;
                flipPancake(plate, topHappy);
                flipPancake(plate, bottomSad);
            }
        }
        outfile << "Case #" << i+1 << ": " << flips << endl;

    }
    return 0;
}
