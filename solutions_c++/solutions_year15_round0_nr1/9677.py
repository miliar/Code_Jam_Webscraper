#include <iostream>
using namespace std;
main()
{
	int T = 0 ;
	cin>>T;	
	for( int i = 0 ; i < T; i++)
	{
		int smax=0;
		char s[1001];
		cin>>smax;
		cin>>s; 
		int res = 0;
		int stand = 0;
		for(int j = 0 ; j <= smax; j++)
		{
			if( 0 != ( s[j] - '0') )
			{
				if(j <= stand)
					stand += (s[j]-'0');
				else
				{
					res += (j-stand);
					stand += (res+s[j]-'0');
				}
			}
		}	
		cout<<"Case #"<<i+1<<": "<<res<<endl;
	}
}
