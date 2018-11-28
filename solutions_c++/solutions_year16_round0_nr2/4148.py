#include <iostream>
#include <fstream>

using namespace std;

int solve(string s)
{
    int partes = 1;

    for(int i=1; i<s.size(); i++)
        if(s[i] != s[i-1])
            partes++;
    if(s[s.size()-1] == '+')
        partes--;
    return partes;
}

int main()
{
    ifstream in("in");
    //ofstream out("out.txt");

    int n;
    in >> n;
    string s;

    for(int i=0; i<n; i++)
    {
        in >> s;
        cout << "Case #" << i+1 << ": " << solve(s) << endl;
    }

    in.close();
    //out.close();

    return 0;
}
