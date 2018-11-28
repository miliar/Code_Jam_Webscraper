#include<iostream>
#include<vector>
#include<fstream>

using namespace std;

int sheep(int n);
int updates(int n, vector<int> & numFound);

int main()
{
    ifstream fin("A-large.in");
    int n = 0;
    fin >> n;
    cout << "There are " << n << " test cases" << endl;
    ofstream fout("output.txt");
    int number = 0;
    for(int i = 0; i < n; i++)
    {
        fout << "Case #" << i + 1 << ": ";
        fin >> number;
        if(number == 0)
        {
            fout << "INSOMNIA" << endl;
        }
        else
        {
            fout << sheep(number) << endl;
        }
    }
    return 0;
}

int sheep(int n) // returns the answer
{
    vector<int> numFound = {0,0,0,0,0,0,0,0,0,0};
    int num = 0;
    int numUpdates = 0;
    while(numUpdates < 10)
    {
        num = num + n;
        numUpdates = numUpdates + updates(num, numFound);
    }
    return num;
}

int updates(int n, vector<int> & numFound) // updates numFound, and returns the number of additional digits found in n
{
    int updates = 0;
    while(n > 0)
    {
        int digit = n % 10;
        if(numFound[digit] == 0)
        {
            updates = updates + 1;
            numFound[digit] = 1;
        }
        n = (n - digit)/10;
    }
    return updates;
}
