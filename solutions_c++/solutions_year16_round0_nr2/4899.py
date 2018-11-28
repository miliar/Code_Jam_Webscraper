#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;

int main()
{
	fstream fil;
	fil.open("C:\\Users\\vaibhav\\Desktop\\JAM2out.txt");
	int T;
	cin>>T;
	int j=1;
	while(T)
	{
		char input[101];
		cin>>input;
		int len=strlen(input);
		char curr=input[0];
		int flips=0;
		for(int i=0;i<len-1;i++)
		{
			if(input[i]!=input[i+1])
			{
				curr=input[i+1];
				flips++;
			}
		}
		if(curr=='-')
		{
			flips++;
		}
		cout<<"Case #"<<j<<": "<<flips<<endl;
		fil<<"Case #"<<j<<": "<<flips<<"\n";
		j++;
		T--;
	}
	fil.close();
}
