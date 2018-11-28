#include <cstdio>
#include <time.h>
#include <cstdlib>
#include <random>
#include <iostream>
#include <vector>
#include <deque>
#include <algorithm>

using namespace std;

void subChar(int* numChars, char lett)
{
	numChars[lett-'A']--;
}

int main(void)
{
	int T;
	cin >> T;
	
	for ( int tc = 0; tc < T; tc++ )
	{
		string inp;
		cin >> inp;
		
		int numNums[10];
		for ( int c = 0; c < 10; c++ ){ numNums[c] = 0; }
		int numChars[26];
		for ( int c = 0; c < 26; c++ ){ numChars[c] = 0; }
		
		for ( int c = 0; c < inp.length(); c++ )
		{
			numChars[((int)inp[c])-'A']++;
		}
		
		while ( numChars['Z'-'A'] > 0 ){ 
			subChar(numChars,'Z');subChar(numChars,'E');subChar(numChars,'R');subChar(numChars,'O');
			numNums[0]++;
		}
		while ( numChars['X'-'A'] > 0 ){ 
			subChar(numChars,'S');subChar(numChars,'I');subChar(numChars,'X');
			numNums[6]++;
		}
		while ( numChars['S'-'A'] > 0 ){ 
			subChar(numChars,'S');subChar(numChars,'E');subChar(numChars,'V');subChar(numChars,'E');subChar(numChars,'N');
			numNums[7]++;
		}
		while ( numChars['W'-'A'] > 0 ){ 
			subChar(numChars,'T');subChar(numChars,'W');subChar(numChars,'O');
			numNums[2]++;
		}
		while ( numChars['G'-'A'] > 0 ){ 
			subChar(numChars,'E');subChar(numChars,'I');subChar(numChars,'G');subChar(numChars,'H');subChar(numChars,'T');
			numNums[8]++;
		}
		while ( numChars['H'-'A'] > 0 ){ 
			subChar(numChars,'T');subChar(numChars,'H');subChar(numChars,'R');subChar(numChars,'E');subChar(numChars,'E');
			numNums[3]++;
		}
		while ( numChars['U'-'A'] > 0 ){ 
			subChar(numChars,'F');subChar(numChars,'O');subChar(numChars,'U');subChar(numChars,'R');
			numNums[4]++;
		}
		while ( numChars['F'-'A'] > 0 ){ 
			subChar(numChars,'F');subChar(numChars,'I');subChar(numChars,'V');subChar(numChars,'E');
			numNums[5]++;
		}
		while ( numChars['O'-'A'] > 0 ){ 
			subChar(numChars,'O');subChar(numChars,'N');subChar(numChars,'E');
			numNums[1]++;
		}
		while ( numChars['I'-'A'] > 0 ){ 
			subChar(numChars,'N');subChar(numChars,'I');subChar(numChars,'N');subChar(numChars,'E');
			numNums[9]++;
		}
		
		
		
		for ( int c = 0; c < 26;c++)
		{
			if ( numChars[c] != 0 ){ cerr << "not zero!" << endl; }
		}
		
		cout << "Case #" << tc+1 << ": ";
		for ( int c = 0; c < 10; c++ )
		{
			while (numNums[c] > 0){
				numNums[c]--;
				cout << c;
			}
		}
		cout << endl;
		
	}

	return 0;
}