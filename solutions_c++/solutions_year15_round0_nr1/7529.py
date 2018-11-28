#include<iostream>
#include<math.h>
#include<vector>
#include<deque>
#include<stack>
#include<fstream>
#include<string>
using namespace std;
int main()
{	
	int n=0,j=1;
	fstream fileo,filei;
	fileo.open("C:\\Users\\Anoos\\Desktop\\anas.txt",ios::out);
	filei.open("C:\\Users\\Anoos\\Desktop\\A-large.in",ios::in);
	filei>>n;
	while(n--)
	{
		int max;filei>>max;
		string s;filei>>s;
		int acco=s[0]-'0',ans=0;
		for(int i=1;i<s.length();i++)
		{
			if(acco<i)
			{
				if(i>max)
				{
				   while(acco!=i)
				   {
					   int temp=max-acco;
				       acco+=temp;
				       ans+=temp;
				   }
				}
				else
				{
					int temp=i-acco;
					  acco+=temp;
				      ans+=temp;
				}
			}
			acco+=s[i]-'0';
		}
		fileo<<"Case #"<<j<<": "<<ans<<endl;
		j++;
	}
	system("pause");
	return 0;
}