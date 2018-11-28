/*Revenge of the Pancakes*/
#include<bits/stdc++.h>
using namespace std;
int main()
{
	int t;
	string s;
	int parity=0;
	long long int countt=0;
	scanf("%d",&t);
	for(int test=1;test<=t;++test)
	{
		cin>>s;
		int found1 = s.find_last_not_of('+');
		if(found1==-1)
			s.erase();
  		else
  		if (found1!=(int)string::npos)
    		s.erase(found1+1);
		countt=0;
		parity=0;
		while(s.length()!=0)
		{
			if(parity==0)
			{
				parity=1;
				if(s[s.length()-1]=='-')
				{
					countt++;
					int found = s.find_last_not_of('-');
					if(found==-1)
						s.erase();
					else
  					if (found!=(int)string::npos)
    					s.erase(found+1);
    			}
			}
			else
			{
				parity=0;
				if(s[s.length()-1]=='+')
				{
					countt++;
					int found = s.find_last_not_of('+');
					if(found==-1)
						s.erase();
					else
  					if (found!=(int)string::npos)
    					s.erase(found+1);
				}
			}
		}
		printf("Case #%d: %lld\n",test,countt);
	}
	return 0;
}
