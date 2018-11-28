#include <stdio.h>
#include <stdlib.h>
#include <fstream>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
#include <sstream>

using namespace std;

bool isPal(long int x)
{
    bool ans = true;

    if (x > 10)
    {
        stringstream z;
        z << x;
        string y = z.str();
        int max = y.size()-1;
        int min = 0;
        while (max > min)
        {
            if (y[max] != y[min])
            {
                //cout << y[max] << " ? = ? " << y[min] << endl;
                ans = false;
                break;
            }
            --max;
            ++min;
        }
    }
    return ans;
}



int main(int argc, char *argv[]){


    if (argc == 2)
    {
        ifstream s;//(filename);
        s.open(argv[1]);
        string buf;

        ofstream answer;
        answer.open("fssol.txt");

        if (s.is_open())
        {
            s>>buf;
            int numcases = atoi(buf.c_str());
            //cout<< "numcases = " << numcases << endl;

            for (int i = 0; i < numcases; ++i)
            {
                answer << "Case #" << i+1 << ": ";
                int ans = 0;
                int high, low;
                s>>buf;
                low = atoi(buf.c_str());
                s>>buf;
                high = atoi(buf.c_str());
                int index = 0;
                vector<long int> pal;
                //pal.push_back(1);
                //pal.push_back(2);
                //pal.push_back(3);
                for (int j = 0; j < low; j++)
                {
                    if (isPal(j))
                    {
                        pal.push_back(j);
                    }
                }
                for(int j = low; j < high+1; j++)
                {
                    if (isPal(j))
                    {
                        pal.push_back(j);
                        while ((pal[index] * pal[index]) <= j)
                        {
                            //cout << pal[index] * pal[index] << " and " << j << endl;
                            if ((pal[index] * pal[index]) == j)
                            {
                                ++ans;
                            }
                            index++;
                        }
                        --index;
                    }

                }
                answer << ans << "\n";

        }

        s.close();
        answer.close();
        }
    }
    return 0;
}
