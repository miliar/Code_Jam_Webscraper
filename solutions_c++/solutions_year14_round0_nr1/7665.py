#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

void solve(int testCase, vector<int> arr1, vector<int> arr2, int row1, int row2, ofstream & output)
{

    vector<int> numbers(16,0);
    for(int i = 0; i < 4; i++)
    {
        numbers[ arr1[ row1*4 + i ]-1 ]++;
        numbers[ arr2[ row2*4 + i ]-1 ]++;
    }
    int somme = 0;
    int res;
    for(int i = 0; i < 16; i++)
    {
        if(numbers[i] == 2)
        {
            somme++;
            res = i+1;
        }
    }

    if(somme == 0)
    {
        output << "Case #"<< testCase <<": " << "Volunteer cheated!" << endl;
    }
    else if(somme == 1)
    {
        output << "Case #"<< testCase <<": " << res << endl;
    }
    else if(somme >= 2)
    {
        output << "Case #"<< testCase <<": " << "Bad magician!" << endl;
    }
}

int main()
{
    ifstream file("A-small-attempt2.in");
    int testCases;
    file >> testCases;
    ofstream output("output2.txt");

    for(int i = 0; i < testCases; i++)
    {
        vector<int> arr1(16,0);
        vector<int> arr2(16,0);
        int row1, row2;
        file >> row1;
        for(int i = 0; i < 16; i++)
        {
            file >> arr1[i];
        }
        file >> row2;
        for(int i = 0; i < 16; i++)
        {
            file >> arr2[i];
        }
        solve(i+1, arr1, arr2, row1-1, row2-1, output);
    }
    return 0;
}
