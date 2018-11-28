#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <fstream>
using namespace std;

class del
{
	public:
	    del(const char* charsToRemove) : chars(charsToRemove) {};

	    bool operator()(char c)
	    {
	        for(const char* testChar = chars; *testChar != 0; ++testChar)
	        {
	            if(*testChar == c) { return true; }
	        }
	        return false;
	    }
	private:
	    const char* chars;
};

int main() 

{
	int z=1;
	cin >> z;
	cin.ignore();
	int standing, friends, i, j, k;
	for (i=1; i<=z; i++)
	{
		string a;
		getline(cin, a);
		a[0]=' ';
		a.erase(remove_if(a.begin(), a.end(), del(" ")), a.end());
		int b[1000];
		for (int p=0; a[p]!='\0'; p++)
		{
			b[p]=a[p]-'0';
		}
	    standing=b[0], friends=0;
	    for (k=1; a[k]!='\0'; k++)
	    {
        	if (standing>=k)
    		{
    			standing+=b[k];
    			continue;
    		}
    		else
    		{
    			while (standing<k)
    			{
    				standing++; friends++;
    			}
    			standing+=b[k];
    		}
	    }
		cout << "Case #" << i << ": " << friends << endl;
	}	
	return 0;
}