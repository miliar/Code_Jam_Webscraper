#include <fstream>
#include <string>
using namespace std;

string find_answer(string str)
{
    string answer;
    answer[0] = str[0];
    for(int i = 0; i < str.length(); i++)
    {
        if (str[i] >= answer[0])
        {
            answer = str[i] + answer;
        }
        else
        {
            answer = answer + str[i];
        }
    }
    return(answer);
}

int main()
{
    int T;
    string str;
    ifstream fin("input.txt");
    fin >> T;
    ofstream fout("output.txt");
    for (int i = 0; i < T; i++)
    {
        fin >> str;
        fout << "Case #" << i + 1 << ": " << find_answer(str) << endl;
    }
    fin.close();
    fout.close();
}