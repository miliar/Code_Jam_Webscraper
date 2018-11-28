#include <fstream>
#include <iostream>
#include <algorithm>
#include <cstring>
#include <map>
#include <vector>
using namespace std;

vector<long long> SomeNr;

ifstream fin("test.in");
ofstream fout("test.out");

bool IsPalindrome(long long X)
{
    vector<int> V;
    while(X) V.push_back(X % 10), X /= 10;
    for(int i = 0; i < V.size(); ++ i)
        if(V[i] != V[V.size() - 1 - i])
            return 0;
    return 1;
}

void Brute()
{
    long long i, Cnt = 0;
    for(i = 1; i <= 10000000; ++ i)
        if(IsPalindrome(i) && IsPalindrome(i * i))
            SomeNr.push_back(i * i);
}


int main()
{
    int i, T, TestCase;
    fin >> T;
    Brute();
    for(TestCase = 1; TestCase <= T; ++ TestCase)
    {
        fout << "Case #" << TestCase << ": ";
        long long A, B;
        fin >> A >> B;
        int Ans = 0;
        for(int i = 0; i < SomeNr.size(); ++ i)
            if(A <= SomeNr[i] && SomeNr[i] <= B)
                Ans ++;
        fout << Ans << "\n";
    }
    return 0;
}
