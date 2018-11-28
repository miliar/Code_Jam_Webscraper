#include <iostream>
#include <string.h>
#include <math.h>
#include <fstream>

using namespace std;

int main()
{

    ifstream fin("input.in");
    ofstream fout("output.out");

    if (!fin.is_open()) cout << "BAD STUFF HAPPENED" << endl;;
    if (!fout.is_open()) cout << "MORE BAD STUFF" << endl;;

    int amount;
    fin >> amount;

    unsigned int number[amount];
    for (int i = 0; i < amount; i++)
    {
        fin >> number[i];
    }


    for (int i = 0; i < amount; i++)
    {
        unsigned int x = number[i];
        int zero = 0, one = 0, two = 0, three = 0, four = 0, five = 0, six = 0, seven = 0, eight = 0, nine = 0;

        bool found = false;
        if(x == 0)
        {
            fout << "Case #" << i + 1 << ": INSOMNIA" << endl;
            found = true;
        }

        int j = 0;
        while(found == false)
        {

            int digits = 0;
            unsigned int newx = x;
            if(newx < 0) digits = 1;
            while(newx)
            {
                newx /= 10;
                digits++;
            }
            newx = x;
            for(int i = digits; i > 0; i--)
            {
                int digit = newx % 10;
                newx /= 10;

                if(digit == 0)
                    zero++;
                else if (digit == 1)
                    one++;
                else if(digit == 2)
                    two++;
                else if(digit == 3)
                    three++;
                else if(digit == 4)
                    four++;
                else if(digit == 5)
                    five++;
                else if(digit == 6)
                    six++;
                else if(digit == 7)
                    seven++;
                else if(digit == 8)
                    eight++;
                else if(digit == 9)
                    nine++;

            }

            if((zero > 0) && (one > 0) && (two > 0) && (three > 0) && (four > 0) && (five > 0) && (six > 0) && (seven > 0) && (eight > 0) && (nine > 0))
            {
                found = true;
                fout << "Case #" << i + 1 << ": " << x << endl;
            }
            else{
                j++;
                x = number[i] * j;
            }

        }
    }


    return 0;

}
