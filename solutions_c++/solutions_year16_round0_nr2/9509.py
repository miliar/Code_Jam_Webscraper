#include <fstream>
#include <string>
#include <iostream>
#include <algorithm>

void flip(std::string* str, int f)
{
    int i;
    // inverse
    for (i = 0; i <= f; ++i)
    {
        str->at(i) = str->at(i) == '-' ? '+': '-';
    }

    // backward
    std::reverse(str->begin(),str->begin() + f+1);
}

bool is(std::string* str, char symb)
{
    for (int i = 0; i < str->length(); ++i)
    {
        if (str->at(i) == symb) {}
        else return false;
    }
    return true;
}

int main()
{
    int T;
    std::ifstream ifs("/home/levon/input.txt", std::ifstream::in);
    if (ifs.is_open())
    {
        ifs >> T;
    }
    else
    {
        std::cout << "cannot open file\n";
    }

    std::string* str = new std::string[T];
    ifs.ignore(1);
    for (int i = 0; i < T; ++i)
    {

        std::getline(ifs,str[i]);
    }

    std::ofstream ofs("/home/levon/output.txt",std::ofstream::out);
    //std::string s("--+-");
    //flip(&s,s.length()-1);
    //std::cout << s << std::endl;


    // find bottom +
    for (int i = 0; i < T; ++i)
    {
        int k = 0;
        while (!is(&str[i],'+'))
        {
            for (int j = 0; j < str[i].length(); ++j)
            {
                if ((str[i][j] != str[i][0]))
                {
                    ::flip(&str[i],j-1);
                    k++;
                    break;
                }
                else if (is(&str[i],'-'))
                {
                    ::flip(&str[i],str[i].length()-1);
                    k++;
                    break;
                }
            }
        }

        ofs << "Case #" << i + 1 << ": " << k << std::endl;
    }
    return 0;
}