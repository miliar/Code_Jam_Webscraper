#include <iostream>
#include <cmath>
#include <string>
#include <sstream>

using namespace std;

bool isPal(int num)
{
	stringstream ss;
	ss << num;
	string theWord = ss.str();
	string original = theWord;
	
	int i;
	char temp;
	
	for (i=0; i<theWord.length()/2; i++)
	{
		temp = theWord[i];
		theWord[i] = theWord[theWord.length()-i-1];
		theWord[theWord.length()-i-1] = temp;
	}
	
	if (original==theWord) return true;
	else return false;
}

int main (void)
{
	int num;
	cin >> num;
	
	int x,y,z,b,e;
	for (x=0;x<num;x++){
		cin >> b;
		cin >> e;
		
		z=0;
		for (y=b;y<=e;y++){
			if ((int)sqrt((double)y)*(int)sqrt((double)y)==y){
				if (isPal(sqrt(y)) && isPal(y))
					z++;
			}
		}
		
		cout << "Case #" << x+1 << ": " << z << endl;
	}
	
	return 0;
}
