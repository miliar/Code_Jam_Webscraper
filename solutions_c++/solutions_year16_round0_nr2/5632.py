#include<cstring>
#include<iostream>

using namespace std;

int T;
char str[10000];
int cont = 0;
int sPos, sNeg;
int it;
int countPos;
int strLength;
bool again;

int main( )
{
	cin >> T;
	
	for(int i=0 ; i<T ; i++)
	{
		cin >> str;
		
		strLength = strlen(str);
		countPos = 0;
		cont =0;
		
		for(int j=0 ; j<strLength ; j++)
		{
			if(str[j] == '+')
			{
				countPos ++;
			}
		}
		
		again = true;
		if(countPos == strLength)
		{
			again = false;
		}
		
		while(again)
		{
			it = 0;
			sPos = sNeg = 0;
			
			while( str[it] == str[it+1] && it<strLength-1)
			{	
				if(str[it] == '+')
				{
					sPos ++;
				}
				else
				{
					sNeg ++;
				}
				
				it++;
			}
			
			if(sPos < strLength)
			{
				for(int k=it ; k>=0 ; k--)
				{
					if(str[k] == '+')
					{
						countPos --;
					}
					
					str[k] = (str[k] == '+'? '-' : '+');
					
					if(str[k] == '+')
					{
						countPos ++;
					}
				}
			}
			
			if(countPos == strLength)
			{
				again = false;
			}
			cont ++;
		}
		
		cout << "Case #" << i+1<< ": " << cont << endl;
	}

return 0;
}