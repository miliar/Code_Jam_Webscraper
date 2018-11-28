#include<iostream>
#include<vector>
#include<fstream>
#include<string>

using namespace std;

int numMinusStrings(string & str);

int main()
{
    ifstream fin("B-large.in");
    int numTests = 0;
    fin >> numTests;
    cout << "There are " << numTests << " test cases." << endl;
    ofstream fout("output.txt");
    string str;
    getline(fin, str);
    int k = 0;
    for(int i = 0; i < numTests; i++)
    {
        fout << "Case #" << i + 1 << ": ";
        getline(fin, str);
        k = numMinusStrings(str);
        if(str[0] == '+')
        {
            fout << 2*k << endl;
        }
        else
        {
            fout << 2*k - 1 << endl;
        }
    }

    return 0;
}

int numMinusStrings(string & str)
{
    int k = 0;
    int i = 0;
    if(str[0] == '-') //get the initial segment
    {
        k = 1;
    }
    for(int j =0; j < str.length() - 1; j++)
    {
        if(str[j] == '+' && str[j+1] == '-')
        {
            k++;
        }
    }
    return k;
}
