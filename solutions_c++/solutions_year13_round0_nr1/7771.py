#include <iostream>
#include <sstream>
#include <map>
#include <set>

using namespace std;

int getline_int(istream& ist)
{
    string line;
    getline(ist,line);
    istringstream ss(line.c_str());

    int res = 0;
    ss >> res;
    return res;
}

string getln_string(istream& ist)
{
    string line;
    getline(ist,line);
    return line;
}

class Solver
{
public:
    Solver(const string& t) : _tablet(t)
    {

    }

private:
    //O,X,D,P
    string line(int num)
    {
        return _tablet.substr(num*4,4);
    }
    string row(int num)
    {
        string r;
        for (int i = 0; i < 4; ++i)
        {
            r += _tablet[i + 4*num];
        }
        return r;
    }
    string col(int num)
    {
        string c;
        for (int i = 0; i < 4; ++i)
        {
            c += _tablet[num + 4*i];
        }
        return c;
    }
    string ldiag(int num)
    {
        string d;
        for (int i = 0; i < 4; ++i)
        {
            int x = (num + i) % 4;
            d += _tablet[x + 4*i];
        }
        return d;
    }
    string rdiag(int num)
    {
        string d;
        for (int i = 0; i < 4; ++i)
        {
            int x = (4+num - i) % 4;
            d += _tablet[x + 4*i];
        }
        return d;
    }
    char examine(const string& line)
    {
        if (line.find('.') != string::npos)
        {
            return 'P';
        }
        
        char state = 'N';
        for (int i = 0; i < 4; ++i)
        {
            char c = line[i];
            switch (state)
            {
            case 'N':
                if (c == 'O')
                {
                    state = 'O';
                }
                else if (c == 'X')
                {
                    state = 'X';
                }
                break;
            case 'O':
                if (c == 'X')
                {
                    return 'D';
                }
                break;
            case 'X':
                if (c == 'O')
                {
                    return 'D';
                }
                break;
            }
        }

        return state;
    }

    int count (const string& s, char c)
    {
        int res = 0;
        for (int i = 0; i < s.size(); ++i)
        {
            if (s[i] == c)
            {
                ++res;
            }
        }
        return res;
    }
public:
    char result()
    {
        if (count(_tablet,'X') < 3)
        {
            return 'P';
        }
        for (int i = 0; i < 4; ++i)
        {
            char r = examine(row(i));
            if (r == 'X' || r == 'O')
            {
                return r;
            }
            r = examine(col(i));
            if (r == 'X' || r == 'O')
            {
                return r;
            }
            r = examine(ldiag(i));
            if (r == 'X' || r == 'O')
            {
                return r;
            }
            r = examine(rdiag(i));
            if (r == 'X' || r == 'O')
            {
                return r;
            }
        }

        return _tablet.find('.') == string::npos ? 'D' : 'P';
    }
private:
    string _tablet;
};


void show(int c, const char* outcome)
{
    cout << "Case #" << (c+1) << ": " << outcome << endl;
}

int main (int argc, char *argv[])
{
    int cases = getline_int(cin);
    for (int c = 0; c < cases; ++c)
    {
        string tablet;
        for (int l = 0; l < 4; ++l)
        {
            tablet += getln_string(cin);
        }
        getln_string(cin);

        Solver s(tablet);
        switch (s.result())
        {
        case 'X':
            show(c,"X won");
            break;
        case 'O':
            show(c,"O won");
            break;
        case 'P':
            show(c,"Game has not completed");
            break;
        case 'D':
            show(c,"Draw");
            break;
        }
    }
    return 0;
}

