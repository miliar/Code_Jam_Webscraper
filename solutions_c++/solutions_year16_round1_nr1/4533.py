#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;

int main(int argc, char * argv[])
{
    int cases = 0;
    char read = 0;
    ifstream fin("A-small-attempt2.in");
    ofstream fout("outputA.txt");
    char s[1000] = {};
    int len = 0;
    char sorted[2000] = {};
    int above = 14;
    int below = 14;

    if(fin.is_open())
    {
        //cout << "Opened File." << endl;
        fin >> cases;
        fin.get(read);
        for(int test = 1; test <= cases; test++)
        {
            fout << "Case #" << test << ": ";
            for(int i = 0; i < 1000; i++)
            {
                s[i] = 0;
            }

            fin.getline(s,1000,'\n');
            len = strlen(s);
            above = 999;
            below = 999;
            sorted[above] = s[0];
            for(int sorts = 1; sorts < len; sorts++)
            {
                if(s[sorts] >= sorted[above])
                {
                    above--;
                    sorted[above] = s[sorts];
                }
                else
                {
                    below++;
                    sorted[below] = s[sorts];
                }
            }
            if(len != 0)
            {for(int i = above; i <= below; i++)
            {
                fout << sorted[i];
            }
            }
            fout << endl;
        }
        fin.close();
        fout.close();
    }
    else
    {
        cout << "Could not open file" << endl;
    }
    return 0;
}
