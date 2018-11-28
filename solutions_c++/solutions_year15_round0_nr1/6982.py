#include<iostream>
#include<string>
using namespace std;
int main()
{   /*freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);*/

	int test_case , count = 0 , max_shy , total = 0 , add = 0 ;
	string s ;
	cin>>test_case;
	

	for(int i  = 0 ; i < test_case ; i++)
	{
		count = 0 ;
		add = 0 ;
		cin>>max_shy;
	    cin>>s;

		for(int j =  1 ; j < s.size() ; j++)
		{
			if(s[j] != '0')
			{
				count = 0 ;
				for(int k = 0 ; k < j ; k++)
				{
					if(s[k] != '0')
					{
					  count = count + (int)s[k]-48 ;
					}
				}
				if(count >= j)
				{
				   count = 0 ;
				}
				else
				{
				     count = j - count ;
					 if(count > add)
					 {
					 add = count ;
					 }
				}

			}
		}
	
		cout<<"Case #"<<i+1<<": "<<add<<endl;
	
	}
return 0;
}