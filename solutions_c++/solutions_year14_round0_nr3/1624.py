#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <sstream>
#include <utility>
#include <stdlib.h>
#include <algorithm>
#include <iomanip>
#include <math.h>

using namespace std;

vector<string> explode(string inputstring, string delimiter)
{
    vector<string> explodes;
    inputstring.append(delimiter);
    while(inputstring.find(delimiter)!=string::npos){
        explodes.push_back(inputstring.substr(0, inputstring.find(delimiter)));
        inputstring.erase(inputstring.begin(), inputstring.begin()+inputstring.find(delimiter)+delimiter.size());
    }
    return explodes;
}

int main()
{
    ifstream file("file.txt");

    vector<string> data(3);

    ofstream fichier("result.txt", ios::out | ios::trunc);


    if(file)
    {
        string row;
        getline(file, row);

        int nb_case = atoi(row.c_str());

        int counter = 0;

        int r = 0, c = 0, m = 0, r_ = 0, c_ = 0, m_ = 0;

        bool impossible;

        string result;

        for(int a = 0; a < nb_case; a++)
        {
            result = "";
            impossible = false;

            getline(file, row);

            data = explode(row, " ");

            r = atoi(data[0].c_str());
            c = atoi(data[1].c_str());
            m = atoi(data[2].c_str());

            r_ = r, c_ = c, m_ = m;

            counter = m;

            if(r < 1 || c < 1 || m < 0 || m > r*c)
                impossible = true;

            // case r or c equal 1

            if(r == 1 || c == 1 || m == r*c - 1)
            {
                counter = 0;
                for(int i = 0; i < r; i++)
                {
                    for(int j = 0; j < c; j++)
                    {
                        if(counter < m)
                        {
                            result += "*";
                            counter++;
                        }
                        else if(i!=r-1 || j!=c-1)
                            result += ".";
                        else
                            result += "c";
                    }
                    result += "\n";
                }

            }

            // the problem is equivalent to a problem with smaller values or r, c and m.

            while(m_ >= r_ + c_ - 1 && r_ >= 3 && c_ >= 3)
            {
                m_ -= r_ + c_ - 1;
                r_--; c_--;
            }

            // then only a few cases are impossible

            if(((r_ == 1 && r != 1) || (c_ == 1 && c != 1) )&& m != r*c - 1)
                impossible = true;

            // case r_ or c_ equal 2

            if(!impossible && (r_ == 2 || c_ == 2) && m != r*c - 1 && r_ + c_ >= 4)
            {
                if(m_ % 2 != 0 || r_*c_ - m_ < 4)
                    impossible = true;
                else
                {
                    counter = 0;
                    for(int i = 0; i < r; i++)
                    {
                        for(int j = 0; j < c; j++)
                        {
                            if((i < r-r_ || j < c-c_) && counter <m)
                            {
                                result += "*";
                                counter++;
                            }
                            else if(((r_ == 2 && j < c-c_+m_/2) || (c_ == 2 && i < r-r_ + m_/2)) && counter < m)
                            {
                                result += "*";
                                counter++;
                            }
                            else if(i!=r-1 || j!=c-1)
                                result += ".";
                            else
                                result += "c";
                        }
                        result += "\n";
                    }
                }

            }

            // case r_ or c_ equal 3

            if(!impossible && ((r_ == 3 && c_ > 2) || (r_ > 2 && c_ == 3)) && m != r*c - 1)
            {
                if((m_ == 5 && r_ + c_ == 7) || ((m_ == 2 || m_ == 4) && r_ + c_ == 6))
                    impossible = true;
            }

            // general case

            if(!impossible && ((r_ > 2 && c_ > 2)) && m != r*c - 1)
            {
                if(m_ % r_ == 0 || m_ % c_ == 0)
                {
                    counter = 0;
                    for(int i = 0; i < r; i++)
                    {
                        for(int j = 0; j < c; j++)
                        {
                            if((i < r-r_ || j < c-c_))
                            {
                                result += "*";
                            }
                            else if(counter < m_ && m_ % r_ == 0 && j < c - c_ +  m_/r_)
                            {
                                result += "*";
                                counter++;
                            }
                            else if(counter < m_ && m_ % c_ == 0 && i < r - r_ + m_/c_)
                            {
                                result += "*";
                                counter++;
                            }
                            else if(i!=r-1 || j!=c-1)
                                result += ".";
                            else
                                result += "c";
                        }
                        result += "\n";
                    }

                }
                else
                {

                    counter = 0;
                    for(int i = 0; i < r; i++)
                    {
                        for(int j = 0; j < c; j++)
                        {
                            if((i < r-r_ || j < c-c_) && counter < m)
                            {
                                result += "*";
                            }
                            else if(counter < m_ && i < r - 2 && j < c - 2)
                            {
                                result += "*";
                                counter++;
                            }
                            else if(counter < m_ && j < c - 2)
                            {
                                result += "*";
                                counter++;
                            }
                            else if(i!=r-1 || j!=c-1)
                                result += ".";
                            else
                                result += "c";
                        }
                        result += "\n";
                    }
                }

            }

            if(impossible)
                result = "Impossible\n";

            cout << "Case #" << a+1 << ": " << endl << result;
            fichier << "Case #" << a+1 << ": " << endl << result;
        }


    }
    else
    {
        cout << "Not found." << endl;
    }

    return 0;
}
