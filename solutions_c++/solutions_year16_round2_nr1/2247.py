
#define _CRT_SECURE_NO_WARNINGS

#include <iostream> // standard input & output cout cin
#include <cstdio> // scanf printf
#include <vector> // std::vector
#include <algorithm>
#include <string> // std::string
#include <queue> // std::queue
#include <cstring> // memset
#include <set> // std::set
#include <utility> // std::pair, std::make_pair
#include <map>

using namespace std;

typedef long long LL;
typedef vector<int> VI;

#define REP(i,n) for(int i=0, i##_len=(n); i<i##_len; ++i)
#define EACH(i,c) for(__typeof((c).begin()) i=(c).begin(),i##_end=(c).end();i!=i##_end;++i)


// -------------------------- global variable



// ; 빼먹지 않았는지 확인 ;;;;;;;;;;;;;;;;;
// -------------------------- declare function

vector<string> spell= {"ZERO","ONE","TWO","THREE","FOUR","FIVE","SIX","SEVEN","EIGHT","NINE"};
char buf[2001];
int digit[26];
// -------------------------- main

int main(int argc, char **argv)
{
	int t;
	scanf("%d",&t);
	string s;
	string answer;
	
	for(int tcase = 1; tcase <=t ;tcase++)
	{
		memset(digit, 0, sizeof(digit));
		answer.clear();
		scanf("%s",buf);
		s = buf;
		
		for(int i = 0 ; i < s.size();i++)
		{
			digit[s[i]-'A']++;
		}	
		
		while(digit['G'-'A']) // eight
		{
			answer = answer + '8';
			for(int j = 0 ; j < spell[8].size();j++)
			{
				digit[spell[8][j]- 'A']--;
			}
		}
		
		while(digit['X'-'A']) // six
		{
			answer = answer + '6';
			for(int j = 0 ; j < spell[6].size();j++)
			{
				digit[spell[6][j]- 'A']--;
			}
		}
		
		while(digit['Z'-'A']) //zero
		{
			answer = answer + '0';
			for(int j = 0 ; j < spell[0].size();j++)
			{
				digit[spell[0][j]- 'A']--;
			}
		}
		
		while(digit['U'-'A']) // four
		{
			answer = answer + '4';
			for(int j = 0 ; j < spell[4].size();j++)
			{
				digit[spell[4][j]- 'A']--;
			}
		}
	
		while(digit['R'-'A']) // three
		{
			answer = answer + '3';
			for(int j = 0 ; j < spell[3].size();j++)
			{
				digit[spell[3][j]- 'A']--;
			}
		}
		while(digit['F'-'A']) // five
		{
			answer = answer + '5';
			for(int j = 0 ; j < spell[5].size();j++)
			{
				digit[spell[5][j]- 'A']--;
			}
		}
		
		while(digit['V'-'A']) // seven
		{
			answer = answer + '7';
			for(int j = 0 ; j < spell[7].size();j++)
			{
				digit[spell[7][j]- 'A']--;
			}
		}
		
		while(digit['W'-'A']) // two
		{
			answer = answer + '2';
			for(int j = 0 ; j < spell[2].size();j++)
			{
				digit[spell[2][j]- 'A']--;
			}
		}
		
		while(digit['O'-'A']) // one
		{
			answer = answer + '1';
			for(int j = 0 ; j < spell[1].size();j++)
			{
				digit[spell[1][j]- 'A']--;
			}
		}
		
		
		while(digit['E'-'A']) // nine
		{
			answer = answer + '9';
			for(int j = 0 ; j < spell[9].size();j++)
			{
				digit[spell[9][j]- 'A']--;
			}
		}
		
		sort(answer.begin(), answer.end());
		printf("Case");
		printf(" #%d: %s\n",tcase, answer.c_str());
	}
	return 0;
}

/* memo
*
*
*
*
*
*/
