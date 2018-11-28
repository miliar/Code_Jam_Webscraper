#include<iostream>
#include<algorithm>
#include<fstream>
using namespace std;

int main()
{
    ifstream fin ("A-large.in");
    ofstream fout ("Alarge.out");
    int t, numletters[26], holder;
    string s, finalanswer;
    fin >> t;
    for (int i = 0; i < t; i++)
    {
        for (int a = 0; a < 26; a++)
            numletters[a] = 0;
        finalanswer = "";
        s = "";
        fin >> s;
        for (int j = 0; j < s.length(); j++) // Converting input to number of each letter
        {
            if (s[j] == 'A') numletters[0]++;
            else if (s[j] == 'B') numletters[1]++;
            else if (s[j] == 'C') numletters[2]++;
            else if (s[j] == 'D') numletters[3]++;
            else if (s[j] == 'E') numletters[4]++;
            else if (s[j] == 'F') numletters[5]++;
            else if (s[j] == 'G') numletters[6]++;
            else if (s[j] == 'H') numletters[7]++;
            else if (s[j] == 'I') numletters[8]++;
            else if (s[j] == 'J') numletters[9]++;
            else if (s[j] == 'K') numletters[10]++;
            else if (s[j] == 'L') numletters[11]++;
            else if (s[j] == 'M') numletters[12]++;
            else if (s[j] == 'N') numletters[13]++;
            else if (s[j] == 'O') numletters[14]++;
            else if (s[j] == 'P') numletters[15]++;
            else if (s[j] == 'Q') numletters[16]++;
            else if (s[j] == 'R') numletters[17]++;
            else if (s[j] == 'S') numletters[18]++;
            else if (s[j] == 'T') numletters[19]++;
            else if (s[j] == 'U') numletters[20]++;
            else if (s[j] == 'V') numletters[21]++;
            else if (s[j] == 'W') numletters[22]++;
            else if (s[j] == 'X') numletters[23]++;
            else if (s[j] == 'Y') numletters[24]++;
            else numletters[25]++;
        }
        if (numletters[25] > 0) // Finding all zeros and adding to the final answer
        {
            holder = numletters[25];
            for (int k = 0; k < holder; k++)
            {
                numletters[4]--;
                numletters[14]--;
                numletters[17]--;
                numletters[25]--;
                finalanswer += '0';
            }
        }
        if (numletters[22] > 0) // Finding all twos and adding to the final answer
        {
            holder = numletters[22];
            for (int k = 0; k < holder; k++)
            {
                numletters[14]--;
                numletters[19]--;
                numletters[22]--;
                finalanswer += '2';
            }
        }
        if (numletters[20] > 0) // Finding all fours and adding to the final answer
        {
            holder = numletters[20];
            for (int k = 0; k < holder; k++)
            {
                numletters[5]--;
                numletters[14]--;
                numletters[17]--;
                numletters[20]--;
                finalanswer += '4';
            }
        }
        if (numletters[5] > 0) // Finding all fives and adding to the final answer
        {
            holder = numletters[5];
            for (int k = 0; k < holder; k++)
            {
                numletters[4]--;
                numletters[5]--;
                numletters[8]--;
                numletters[21]--;
                finalanswer += '5';
            }
        }
        if (numletters[23] > 0) // Finding all sixes and adding to the final answer
        {
            holder = numletters[23];
            for (int k = 0; k < holder; k++)
            {
                numletters[8]--;
                numletters[18]--;
                numletters[23]--;
                finalanswer += '6';
            }
        }
        if (numletters[21] > 0) // Finding all sevens and adding to the final answer
        {
            holder = numletters[21];
            for (int k = 0; k < holder; k++)
            {
                numletters[4]--;
                numletters[4]--;
                numletters[13]--;
                numletters[18]--;
                numletters[21]--;
                finalanswer += '7';
            }
        }
        if (numletters[6] > 0) // Finding all eights and adding to the final answer
        {
            holder = numletters[6];
            for (int k = 0; k < holder; k++)
            {
                numletters[4]--;
                numletters[6]--;
                numletters[7]--;
                numletters[8]--;
                numletters[19]--;
                finalanswer += '8';
            }
        }
        if (numletters[14] > 0) // Finding all ones and adding to the final answer
        {
            holder = numletters[14];
            for (int k = 0; k < holder; k++)
            {
                numletters[4]--;
                numletters[13]--;
                numletters[14]--;
                finalanswer += '1';
            }
        }
        if (numletters[7] > 0) // Finding all threes and adding to the final answer
        {
            holder = numletters[7];
            for (int k = 0; k < holder; k++)
            {
                numletters[4]--;
                numletters[4]--;
                numletters[7]--;
                numletters[17]--;
                numletters[19]--;
                finalanswer += '3';
            }
        }
        if (numletters[8] > 0) // Finding all nines and adding to the final answer
        {
            holder = numletters[8];
            for (int k = 0; k < holder; k++)
            {
                numletters[4]--;
                numletters[8]--;
                numletters[13]--;
                numletters[13]--;
                finalanswer += '9';
            }
        }
        sort(finalanswer.begin(), finalanswer.end());
        fout << "Case #" << i + 1 << ": " << finalanswer << endl;
    }
}
