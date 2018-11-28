#include <iostream>
#include <fstream>
#include <sstream>
#include <algorithm>
#include <string>
#include <cmath>
using namespace std;

int PalindromsInRange (int A, int B)
{
    string strNum, strNum2;
    int Count(0);
    int curNum;    
        
    for (int i = A; i <= B; i++)
    {
        curNum = i;
        
        strNum = to_string(curNum);
        strNum2 = to_string(static_cast<int>(sqrt(curNum)));
        
        if (equal(strNum.begin(), strNum.end(), strNum.rbegin()) &&
            equal(strNum2.begin(), strNum2.end(), strNum2.rbegin()) &&
            (stoi(strNum2) * stoi(strNum2)  == stoi(strNum))) 
        {
            Count++;
        }
        else
            continue;
    }
    
    return Count;
}

int main()
{
    ifstream infile("input.txt");
    ofstream outfile("output.txt");
    int N(0), A(0), B(0);
        
    infile >> N;
    
    
    for (int i = 0; i < N; i++)
    {
        infile >> A >> B;
        outfile << "Case #" << i + 1 << ": ";
        outfile << PalindromsInRange (A, B) << endl;
    }
	
	cout << "It's ok." << endl;
    infile.close();
    outfile.close();
    return 0;
}
