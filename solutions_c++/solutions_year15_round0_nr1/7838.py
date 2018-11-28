#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("out.txt");

    int cs = 0;
    int sm, standing, friends;
    int t, temp;

    string digit;

    fin >> t;

    while(t--)
    {
        cs++;

        fin >> sm;
        sm++;

        fin >> digit;
        vector<int> shy;

        for(int i=0; i<sm; i++)
        {
            temp = (int) (digit[i] - '0');
            shy.push_back(temp);
        }
        standing = shy[0];
        friends = 0;

        for(int i=1; i<sm; i++)
        {
            if(shy[i] != 0)
            {
                if(standing >= i)
                    standing += shy[i];
                else
                {
                    friends += (i-standing);
                    standing = shy[i] + i;
                }
            }
        }
        fout << "Case #" << cs << ": " << friends << "\n";
    }

    return 0;
}
