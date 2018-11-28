#include <fstream>
#include <string>

using namespace std;

ofstream fileout("output.txt");

bool all_plus_checking(string p)
{
    for (int i = 0; i < p.length(); i++)
    {
        if (p[i] != '+')
        {
            return(false);
        }
    }
    return(true);
}

void find_answer(string pancakes, int t)
{
    int answer = 0;
    while (all_plus_checking(pancakes) != true)
    {
        char selected_symbol = pancakes[0];
        int count = 0;
        while (pancakes[count] == selected_symbol)
        {
            count++;
        }
        for (int i = 0; i < count; i++)
        {
            pancakes[i] = (pancakes[i] == '+') ? '-' : '+';
        }
        answer++;
    }
    fileout << "Case #" << t << ": " << answer << "\n";
}

int main()
{
    ifstream filein("input.txt");
    int T;
    string S;
    filein >> T;
    for (int i = 1; i <= T; i++)
    {
        filein >> S;
        find_answer(S, i);
    }
    filein.close();
    fileout.close();
    return(0);
}