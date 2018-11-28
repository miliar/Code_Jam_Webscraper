#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>

using namespace std;

int main()
{
    int ncases;
    cin >> ncases;

    for (int i = 0; i < ncases; i++)
    {
        int nwords;
        cin >> nwords;

        vector<string> words;
        for (int j = 0; j < nwords; j++)
        {
            string word;
            cin >> word;
            words.push_back(word);
        }
    
        bool can_win = true;
        int moves = 0;
        while(true)
        {
            int length[101];//# of occurrances of ea. length
            for (int l = 0; l <= 100; l++)
                length[l] = 0;

            if (words[0].length() == 0) 
            {
                for (int j = 0; j < nwords; j++)
                {
                    if (words[j].length() != 0)
                    {
                        can_win = false;
                        break;
                    }
                }
                break;
            }

            char letter = words[0].at(0);
            for (int j = 0; j < nwords; j++)
            {
                int pos = 0;
                if (words[j].length() == 0)
                {
                    can_win = false;
                    break;
                }
                while(letter == words[j].at(pos))
                {
                    pos++;
                    if (words[j].length() == pos)
                    {
                        break;
                    }
                }
                if (pos == 0)
                {
                    can_win = false;
                    break;
                }
                length[pos]++;
                words[j] = words[j].substr(pos);
            }
            
            int min = nwords*100;
            for (int l = 0; l <= 100; l++)
            {
                if (length[l] == 0)
                    continue;

                int curr = 0;
                for (int k = 0; k <= 100; k++)
                {
                    curr += (abs(k-l)*length[k]);
                    
                }
                if (curr < min)
                    min = curr;
            }
            moves += min;
        }
        cout << "Case #" << i+1 << ": ";
        if (!can_win)
            cout << "Fegla Won" << endl;
        else
            cout << moves << endl;

    }
    return 0;
}
