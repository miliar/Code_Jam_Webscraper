#include <iostream>
#include <string>
using namespace std;

int main() {
    freopen("out.txt", "w", stdout);
	int i,t_case=10;
	string inp;
	cin>>t_case;
	for(i=0;i<t_case;i++)
	{
		cin>>inp;
		int len=inp.length();
		int count=0;
		for(int j=0; j<len-1;j++)
			{
				if(inp[j]!= inp[j+1])
				{
					count++;
				}
			}
			if(inp[len-1]=='-')
				cout<<"Case #"<<i+1<<": "<<count+1<<"\n";
			else
				cout<<"Case #"<<i+1<<": "<<count<<"\n";
	}
	return 0;
}
