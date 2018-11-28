#include <iostream>
#include <string>
using namespace std;

void lastWord(string &S)
{
	string last;
	for(int i = 0; i<S.size(); i++)
	{
		if(S[i]>=last[0])
		{
			last = S[i] + last;
		}
		else
		{
			last += S[i];
		}
	}
	cout<<last<<endl;
}

int main()
{
	int T;
	string S;
	cin>>T;
	for(int i = 1; i<= T; i++)
	{
		cin>>S;
		cout<<"Case #"<<i<<": ";
		lastWord(S);
	}
}