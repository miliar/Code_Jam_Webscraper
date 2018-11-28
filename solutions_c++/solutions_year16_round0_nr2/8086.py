#include <iostream>

using namespace std;

int main()
{
	int T;
	cin>>T;
	for(int ti = 1;ti<=T;ti++)
	{
		string w;
		cin>>w;
		int o = 0;
		for(int i = 1; i < w.length(); i++)
		{
			if(w[i-1]!=w[i])
			{
				
					o += 1;
				
			}
			
		}
		if(w[w.length()-1]=='-')
			o += 1;
		cout<<"Case #"<<ti<<": "<<o<<endl;
	}
	
}