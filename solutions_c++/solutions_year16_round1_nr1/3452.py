#include<iostream>
#include<vector>
#include<fstream>
#include<string>

using namespace std;

string last(string s);
int findMax(string s);

int main()
{
    ifstream fin("A-large.in");
    int n = 0;
    fin >> n;
    cout << "There are " << n << " test cases" << endl;
    ofstream fout("output.txt");
    string s = "";
    for(int i = 0; i < n; i++)
    {
        fout << "Case #" << i + 1 << ": ";
        fin >> s;
        cout << "Case #" << i + 1 << " " << s << endl;
        cout << "The position of the latest letter is " << findMax(s) << endl;
        fout << last(s) << endl;
    }
    return 0;
}

string last(string s)
{
    if(s.length() == 0 || s.length() == 1)
    {
        return s;
    }
    int n = findMax(s);
    if(n < s.length() - 1)
    {
        return s[n] + last(s.substr(0,n)) + s.substr(n + 1);
    }
    else
    {
        return s[n] + last(s.substr(0,n));
    }

}

int findMax(string s)
{
    int n = 0;
    for(int i = 0; i < s.length(); i++)
    {
        if(s[i] >= s[n])
        {
            n = i;
        }
    }
    return n;
}
