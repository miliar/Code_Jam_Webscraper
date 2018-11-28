#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

ifstream fin("in.in");
ofstream fout("out.out");

int get(vector <int> v)
{
    long long add = 0;
    for(int i = 0; i < v.size()-1; i++)
    {
        if(v[i] > 1)
        {
            v[i + 1] += (v[i] - 1);
            v[i] = 1;
        }
    }

    for(int i = 0; i < v.size(); i++)
    {
        if(v[i] == 0) add++;
    }
    return add;
}

void doCase(int k)
{
    int s;
    fin >> s;
    char c;
    long long sum = 0;
    vector <int> v(0);
    for(int i = 0; i < s; i++)
    {
        fin >> c;
        v.push_back(c-'0');
    }
    fin >> c;
    v.push_back(c-'0');

    fout << "Case #" << k << ": ";
    fout << get(v);
    fout << endl;
}



int main()
{
    int t;
    fin >> t;
    for(int i = 1 ; i <= t; i++)
    {
        doCase(i);
    }
    return 0;
}
