#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <map>
#include <cmath>
#include <algorithm>
#include<sstream>

using namespace std;

bool isPal(int x){

	stringstream ss;
	ss << x;
	string str = ss.str();
	for(int i=0;i<str.length()/2;i++)
	{
		if(str[i]!=str[str.length()-1-i])
		{
			return false;
		}
	}
	return true;
}
int main()
{
    ifstream fin("C-small-attempt0.in");
    ofstream fout("C-small-attempt0.out");
   
    int T;
    
    fin >> T;


	for(int p=0 ; p<T ;p++)
    {
		int sum=0;
	   	int a=0,b=0;
		fin>>a;fin>>b;
		for(int i=0;i<=b;i++)
		{
			if(isPal(i)&&isPal(i*i))
				if(i*i<=b&&(i*i>=a))
				sum++;
		}
		
		fout << "Case #" << p+1 << ": " << sum << endl;
    }
	return 0;
}