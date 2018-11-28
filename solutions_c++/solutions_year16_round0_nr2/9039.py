#include <iostream>
#include <string.h>
using namespace std;

int main() {
	int T;
	cin>>T;
	for(int i=0;i<T;i++)
	{
		int x=0,count=0;
		char S[100],c;
		cin>>S;
		while(x < strlen(S))
		{
			c=S[x];
			while(x < strlen(S) && S[x] == c) x++;
			if(x>=strlen(S) && c=='-')
			{	
				count++;
				x++;
			}
			else if(x<=strlen(S)-1)
				count++;
		}
		cout<<"Case #"<<i+1<<": "<<count<<"\n";
	}
	return 0;
}