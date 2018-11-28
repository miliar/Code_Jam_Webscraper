#include <iostream>
#include <fstream>
#include <cstring>

using namespace std;

int main() {

    int numCase = 0;
    int len = 0;
    int flip = 0;
    char str[100];

    ifstream fin("B-small-attempt0.in");
    ofstream fout("B-small-attempt0.out");

    if (!fin.is_open()) cout << "input.in was not open successfully" << endl;
    if (!fout.is_open()) cout << "output.out was not open successfully" << endl;

    fin >> numCase;

    for (int j = 0; j < numCase; j++)
    {
        fin >> str;
        len = strlen(str);
        flip = 0;

        for(int i = len ; i > 0; i--)
        {
          if (str[i-1] == '-')
          {
            for(int j = i; j > 0; j--)
            {
              if(str[j-1] == '-')
                str[j-1] = '+';
              else
              if(str[j-1] == '+')
                str[j-1] = '-';

            }
            flip++;
          }
        }

        fout << "Case #" << (j + 1) << ": " << flip << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
