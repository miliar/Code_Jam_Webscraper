#include <iostream>
#include <vector>
#include <string>
#include <ostream>
#include <algorithm>
#include <iterator>
#include <array>
// #include <discreture/discreture.hpp>

using namespace std;
// using namespace dscr;

template <class T> 
std::ostream& operator<<(std::ostream& os, const vector<T>& rhs)
{
	for (const auto& x : rhs)
		os << x << "";
	return os;
}

vector<bool> A;
vector<int> Number;

string Name(int i)
{
    if (i == 0)
        return "ZERO";
    if (i == 1)
        return "ONE";
    if (i == 2)
        return "TWO";
    if (i == 3)
        return "THREE";
    if (i == 4)
        return "FOUR";
    if (i == 5)
        return "FIVE";
    if (i == 6)
        return "SIX";
    if (i == 7)
        return "SEVEN";
    if (i == 8)
        return "EIGTH";
    if (i == 9)
        return "NINE";
    return "";
}

void mark(int i, const string& S)
{
    auto name = Name(i);
    for (auto x : name)
    {
        for (int j = 0; j < S.size(); ++j)
        {
            if (S[j] != x)
                continue;
            if (A[j] == 0)
            {
                A[j] = 1;
                break;
            }
        }
    }
    Number.push_back(i);
}

void Solve(string& S)
{
    A = vector<bool>(S.size(),0);
    Number.clear();
	for (auto x : S)
    {
        if (x == 'Z')
            mark(0,S);
        if (x == 'W')
            mark(2,S);
        if (x == 'G')
            mark(8,S);
        if (x == 'X')
            mark(6,S);
        if (x == 'U')
            mark(4,S);
    }
    
    for (int i = 0; i < S.size(); ++i)
    {
        auto x = S[i];
        if (x == 'S' && !A[i])
            mark(7,S);
        
        if (x == 'T' && !A[i])
            mark(3,S);
    }
    
    for (int i = 0; i < S.size(); ++i)
    {
        auto x = S[i];
        if (x == 'V' && !A[i])
            mark(5,S);
    }
    
    
    
    for (int i = 0; i < S.size(); ++i)
    {
        auto x = S[i];
        
        if (x == 'O' && !A[i])
            mark(1,S);
        if (x == 'I' && !A[i])
            mark(9,S);
    }
    sort(Number.begin(), Number.end());
//     cout << A << endl;
    cout << Number << endl;
}


int main() 
{
	int Total;
	cin >> Total;
	for (int i = 0; i < Total; ++i)
	{
		string s;
		cin >> s;
		
		cout << "Case #" << i+1 << ": ";
		Solve(s);
// 		cout << endl; 
	}
	
	
	return 0;
}
