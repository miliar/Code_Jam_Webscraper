#include <iostream>
#include <string>

using namespace std;

char shyLevel[1002];

int calculate(int f,int total,int start,int audience)
{
	int n=shyLevel[start]-'0';
	if(n!=0)
	{
		if(audience>=start-1)
			audience+=n;
		else
		{
			f+=start-1-audience;
			audience+=f+n;
		}
	}
	if(start<=total)
		return f+calculate(0,total,start+1,audience);
	else
		return f;
}

int main()
{
	int T,S;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cin>>S;
		cin.getline(shyLevel,1002);
		int numOfFriend=0;
		cout<<"Case #"<<i+1<<": "<<calculate(numOfFriend,S,1,0)<<endl;
	}
}