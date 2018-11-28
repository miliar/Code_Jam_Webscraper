
#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>

using namespace std;


int main(){
	int t =0;
	freopen( "A-large.in", "r", stdin );
	freopen( "A-large.out", "w", stdout );	
	cin >> t;
	

	for(int k =0; k< t; k++)
	{
		int result[10]={0,0,0,0,0,0,0,0,0,0};
		int alpha[26];
		string input;
		string res="";
		cin >> input;
		for(int m=0; m<26; m++)
		{
			alpha[m] = 0;
		}
		
		for(int i=0; i< input.length();i++)
		{

			(alpha[input[i]-'A'])++;
		}

		for(int i=0; i<alpha['Z'-'A']; i++)
		{
			(result[0])++;
			string s = "ZERO";
			for(int j=0; j< s.length(); j++)
			{
				if(s[j] != 'Z')
				{
				(alpha[s[j]-'A'])--;
				}
			}
		}
		for(int i=0; i<alpha['W'-'A']; i++)
		{
			(result[2])++;
			string s = "TWO";
			for(int j=0; j< s.length(); j++)
			{
				if(s[j] != 'W')
				{
				(alpha[s[j]-'A'])--;
				}
			}
		}

		for(int i=0; i <alpha['X'-'A']; i++)
		{
			(result[6])++;
			string s = "SIX";
			for(int j=0; j< s.length(); j++)
			{
				if(s[j] != 'X')
				{
				(alpha[s[j]-'A'])--;
				}
			}
		}

		for(int i=0; i <alpha['U'-'A']; i++)
		{
			(result[4])++;
			string s = "FOUR";
			for(int j=0; j< s.length(); j++)
			{
				if(s[j] != 'U')
				{
				(alpha[s[j]-'A'])--;
				}
			}
			
		}
		for(int i=0; i <alpha['G'-'A']; i++)
		{
			(result[8])++;
			string s = "EIGHT";
			for(int j=0; j< s.length(); j++)
			{
				if(s[j] != 'G')
				{
				(alpha[s[j]-'A'])--;
				}
			}
		}
		for(int i=0; i <alpha['H'-'A']; i++)
		{
			(result[3])++;
			string s = "THREE";
			for(int j=0; j< s.length(); j++)
			{
				if(s[j] != 'H')
				{
				(alpha[s[j]-'A'])--;
				}
			}
		}
		for(int i=0; i <alpha['F'-'A']; i++)
		{
			(result[5])++;
			string s = "FIVE";
			for(int j=0; j< s.length(); j++)
			{
				if(s[j] != 'F')
				{
				(alpha[s[j]-'A'])--;
				}
			}
		}
		for(int i=0; i <alpha['V'-'A']; i++)
		{
			(result[7])++;
			string s = "SEVEN";
			for(int j=0; j< s.length(); j++)
			{
				if(s[j] != 'V')
				{
				(alpha[s[j]-'A'])--;
				}
			}
		}
		for(int i=0; i <alpha['I'-'A']; i++)
		{
			(result[9])++;
			string s = "NINE";
			for(int j=0; j< s.length(); j++)
			{
				if(s[j] != 'I')
				{
				(alpha[s[j]-'A'])--;
				}
			}
		}
		for(int i=0; i <alpha['N'-'A']; i++)
		{
			(result[1])++;
			string s = "ONE";
			for(int j=0; j< s.length(); j++)
			{
				if(s[j] != 'N')
				{
					(alpha[s[j]-'A'])--;
				}				
			}
		}

		for(int i = 0; i< 10;i++)
		{
			for(int j= 0; j< result[i]; j++)
			{
				int a = i;
				stringstream ss;
				ss << a;
				string str = ss.str();
				res.append(str);
			}
		}

		
		cout << "Case #" << k+1 <<": " << res << "\n";		
	}

}

