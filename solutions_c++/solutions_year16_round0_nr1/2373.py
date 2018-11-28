#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char * argv[])
{
    int ans = 0;
    int checknum = 0;
    bool digits[10];
    int tickedoff = 0;

    int n = 0;
    int cases = 0;

    ifstream fin("A-large.in");
    ofstream fout("write1a.txt");

    if(fin.is_open())
    {
        //cout << "Open" << endl;

        fin >> cases;

        for(int onebyone = 1; onebyone <= cases; onebyone++)
        {
            fout << "Case #" << onebyone << ": ";

            fin >> n;
            ans = 0;

            if(n == 0)
            {
                fout << "INSOMNIA" << endl;
            }
            else
            {
                for(int i = 0; i < 10; i++)
                {
                    digits[i] = false;
                }
                tickedoff = 0;

                for(int i = 1;tickedoff != 10; i++)
                {
                    checknum = i * n;

                    while(checknum != 0)
                    {
                        if(digits[checknum%10] == false)
                        {
                            digits[checknum%10] = true;
                            tickedoff++;
                        }
                        checknum /= 10;
                    }

                    if(tickedoff == 10)
                    {
                        ans = i * n;
                    }
                }

                fout << ans << endl;
            }
        }

        fin.close();
        fout.close();
    }
    else
    {
        cout << "Error opening file" << endl;
    }

    return 0;
}
