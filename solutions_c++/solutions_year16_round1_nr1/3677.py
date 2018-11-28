#include <iostream>
#include <string>
using namespace std;

int main()
{
	int T;cin>>T;
	int t=1;
	while(t<=T)
	{
		string myStr;
		cin>>myStr;
		int N = myStr.length();
		string resStr;
		resStr+=myStr[0];
		for(int i =1;i<N;i++)
		{
			char ch = myStr[i];
			if(resStr[0]>ch)
				resStr+=ch;
			else
			{
				string str2;
				str2+=ch;
				str2+=resStr;
				resStr=str2;
			}
		}
		cout<<"Case #"<<t<<": "<<resStr<<"\n";
		t++;
	}
	
}