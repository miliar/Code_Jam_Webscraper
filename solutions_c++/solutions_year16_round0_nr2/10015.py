#include <iostream>
#include <string>

using namespace std;



bool allflipped(string s, int n)
{
	for(int i = 0; i< n ;i++)
	{
		if(s[i] == '-')
			return false;
	}
	return true;
}
string move(string s, int n)
{
	string temp;
	for(int i=n-1;i>=0;i--)
	{
		if(s[i] == '+')
			temp.push_back('-');
		else
			temp.push_back('+');
	}
	s.replace(0,n,temp);
	//cout << s << endl;
	return s;	
}

int last_Char(string s, char c)
{
	int i=0;
	while(s[i] == c){
		i++;
	}
	return i;
}

bool endswith(string s, int p, int n)
{
	for(int i=p; i<n; i++)
	{
		if(s[i] == '-')
			return false;
	}
	return true;
}
int calculateOptimalMoves(string s)
{
	int op = 0;
	int n = s.length();
	int i=0,p;
	i=n-1;
	while(s[i]=='+')
		i--;
	n = i + 1;
	
	while(!allflipped(s,n)){
		
		if(s[0]=='+')
		{
			//cout << "plus" << endl;
			p = last_Char(s,'+');
			
			s = move(s,p);
			op++;
			//cout << s << endl;
		}
		else{
			
			p = last_Char(s,'-');
			
			if(endswith(s,p,n))
			{
				/*
				* from p to n all are plus or no plus
				*/
				s = move(s,p);
				op++;
			}
			else{
				s = move(s,n);
				op++;
				i=n-1;
				while(s[i]=='+')
					i--;
				n = i + 1;
			}

			//cout << s << endl;
				
		}

		
	}

	return op; 

}
int main(void)
{
	int t,c,i;
	string s;
	int ans;
	cin >> t;
	for(c=1;c<=t;c++)
	{
		s.erase();
		cin >> s;
		ans = calculateOptimalMoves(s);
		cout << "Case #" << c << ": " << ans << endl;
	}
	return 0;
}