#include <cstdio>
#include <string>
#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

bool isPalindrome(unsigned long long num)
{
    string numStr = to_string(num);
    for(unsigned long i = 0; i < numStr.length() / 2; i++)
        if(numStr[i] != numStr[numStr.length() - i - 1])
            return false;
    return true;
}

int main()
{
    const unsigned long long maxSize = 100000000000001l;
    
    vector<unsigned long long> solutions;
    
    //Set bits to on for valid solutions
    for(unsigned long long i = 1; i*i < maxSize; i++)
    {
         if(isPalindrome(i) && isPalindrome(i*i))
            solutions.push_back(i*i);
    }

	string filename;
	cin >> filename;

	fstream input(filename, fstream::in);
	fstream output("output.txt", fstream::out);

    int cases;
    input >> cases;
    for(int i = 0; i < cases; i++)
    {
        unsigned long long A, B;
        input >> A >> B;
        
        int j, k;
		for(j = 0; j < solutions.size(); j++)
			if(solutions[j] >= A) break;
		
		for(k = j; k < solutions.size(); k++)
			if(solutions[k] > B) break;
			
		int count = k - j;
            
		output << "Case #" << i + 1 << ": " << count << endl;
    }
    
    return 0;
}
