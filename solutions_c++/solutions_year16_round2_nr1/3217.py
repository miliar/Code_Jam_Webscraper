#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int buffer[257];

void cleanBuffer()
{
    for(int i='A';i<='Z';i++)
        buffer[i] = 0;
}

char* numberToString(int number)
{
    char* numbers[] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    return numbers[number];
}

void remove(int number)
{
    char* target = numberToString(number);
    for(int i=0;target[i]!=0;i++)
        buffer[target[i]]--;
}

void remove(char target, int number, vector<int> &results)
{
    int n = buffer[target];
    for(int i=0;i<n;i++)
    {
        results.push_back(number);
        remove(number);
    }
}

void solve(int position)
{
    string cad;
    vector<int> results;
    cin>>cad;
    cleanBuffer();
    for(int i=0;i<(int)cad.length();i++)
        buffer[cad[i]]++;
    remove('Z', 0, results);
    remove('W', 2, results);
    remove('X', 6, results);
    remove('G', 8, results);

    remove('T', 3, results);

    remove('R', 4, results);

    remove('F', 5, results);

    remove('S', 7, results);

    remove('O', 1, results);
    remove('I', 9, results);

    std::sort(results.begin(), results.end());

    cout<<"Case #"<<position<<": ";
    for(int i=0;i<(int)results.size();i++)
        cout<<results[i];
    cout<<endl;
}

int main()
{
    int n;
    cin>>n;
    for(int i=0;i<n;i++)
        solve(i+1);
    return 0;
}
