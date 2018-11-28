#include <iostream>
#include <fstream>
#include <sstream>
#include <math.h>

using namespace std;

bool isPalin(int num)
{
    ostringstream ss;
    ss << num;
    
    string numString = ss.str();
    int len = numString.length();
    for(int i = 0; i < len; ++i)
        if(numString[i] != numString[len - i - 1])
           return false;
    return true;
}

int main()
{
	ifstream in("in.in");
	ofstream out("out.out");

	int T;
	in >> T;
	
	for(int i = 0; i < T; ++i) 
	{
	    int A, B, rootA, rootB;
	    in >> A >> B;
	    
	    int count = 0;
	    
	    rootA = sqrt(A);
	    if(rootA * rootA < A)
	        rootA += 1; //first integer larger than rootA
	    rootB = sqrt(B);
	    
	    for(int j = rootA; j <= rootB; ++j)
	        if(isPalin(j) && isPalin(j*j))
    	        count += 1;
        
    	out << "Case #" << i+1 << ": " << count << endl;
	}
	
	
	out.close();
}
