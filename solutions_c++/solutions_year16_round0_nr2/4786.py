#include <cstdlib>
#include <fstream>
#include <cstring>
#include <iostream>

using namespace std;

string unificate_str(string str);
int count_steps(string str);

int main()
{
    ifstream in;
    in.open("in.txt");
    ofstream out;
    out.open("out.txt");

    int case_num;
    in >> case_num;

    for (int i_case = 1; i_case <= case_num; i_case++)
    {

        string in_str;
        in >> in_str;

        string str = unificate_str(in_str);

        out << "Case #" << i_case << ": " << count_steps(str) << endl;

    }

    in.close();
    out.close();

    return 0;
}

string unificate_str(string str)
{
    string result = "1";
    result[0] = str[0];

    int j = 0;
    for (int i = 1; i < str.length(); i++)
            if (str[i] != str[i-1])
            {
                string appendant = "1";
                appendant[0] = str[i];
                result.append(appendant);
            }

    return result;
}

int count_steps(string str)
{
    int result = str.length();
    if (str[str.length()-1] == '+')
        result--;
    return result;
}
