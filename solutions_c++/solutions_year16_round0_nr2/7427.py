#include <iostream>
#include <string>
using namespace std;
int main()
{

	int T;
	unsigned long long iter,pos,lastpos;
	string str;
	char c;

	cin>>T;
	for(int tcounter=1;tcounter<=T;tcounter++)
	{
		str.clear();
		iter = 0;
		lastpos = 1;
		cin>>str;


		while(lastpos != str.length())
		{
			c = str[0];
			for(pos=lastpos;pos < str.length();pos++)
			{
				if(str[pos] != c)
					break;	
			}
			
			lastpos = pos;
			if(lastpos == str.length())
				break;

			for(unsigned int k = 0;k < pos;k++)
			{
				str[k] = str[pos];	
			}
		
			iter++;
		}

		if(str[0] == '-')
			iter++;

		cout<<"Case #"<<tcounter<<": "<<iter<<endl;

	}

	return 0;

}
