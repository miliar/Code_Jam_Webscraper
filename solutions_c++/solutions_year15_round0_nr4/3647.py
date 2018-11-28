#include <iostream>
#include <fstream>

using namespace std;

// true = gabriel, false = richard
bool checkGrid(size_t ominoSize, size_t length, size_t width)
{
    if (ominoSize == 1)
    {
        return true;
    }
    else if (ominoSize == 2)
    {
        if ((length*width)%ominoSize != 0)
        {
            return false;
        }
        else
        {
            return true;
        }
    }
    else if (ominoSize == 3)
    {
        if ((length*width)%ominoSize != 0)
        {
            return false;
        }
        else
        {
            if (length == 1 || width == 1)
                return false;
            else
                return true;
        }
    }
    else
    {
        if ((length*width)%ominoSize != 0)
        {
            return false;
        }
        else
        {
            if (length == 1 || width == 1)
                return false;
            else if (length == 2 || width == 2)
                return false;
            else
                return true;
        }
    }
}

int main()
{
    ifstream infile("input.txt");
    ofstream outfile("output.txt");
    size_t x, r, c, count(1);
    string tempIn, ans;

    getline(infile, tempIn);
    while (getline(infile, tempIn))
    {
        x = tempIn[0]-'0';
        r = tempIn[2]-'0';
        c = tempIn[4]-'0';
        if (checkGrid(x, r, c))
            ans = "GABRIEL";
        else
            ans = "RICHARD";
        outfile << "Case #" << count++ << ": " << ans << endl;
    }
    return 0;
}

