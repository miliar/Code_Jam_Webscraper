#include <iostream>
using namespace std;

int main(int argc, char **argv)
{
	int t,c=1;
	cin>>t;
	while(c<=t)
	{
		string word,answer="";
		cin>>word;
		int l=word.length();
		answer+=word[0];
		for(int i=1;i<l;i++)
		{
			if(word[i]>=answer[0])
				answer=word[i]+answer;
			else
				answer=answer+word[i];
		}
		cout<<"Case #"<<c<<": "<<answer<<endl;
		c++;
	}
	
}
