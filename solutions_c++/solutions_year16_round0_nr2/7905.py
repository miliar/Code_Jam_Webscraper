#include<iostream>
#include <string>
#include<fstream>
#include<ostream>
#include<vector>
#include<algorithm>
#include<set>
using namespace std;

#define InputOutputToFile
char str[100];

void flip(int i)
{
	int j=0;
	char tmp;
	if(i==0)
	{
		if(str[i]=='+')
			str[i]='-';
		else
			str[i]='+';
		return;
	}
	while(j!=i)
	{
		tmp=str[j];
		if(str[i]=='+')
			str[j]='-';
		else
			str[j]='+';

		if(tmp=='+')
			str[i]='-';
		else
			str[i]='+';
		++j;
		--i;
		if(j==i)
		{
			if(str[i]=='+')
				str[i]='-';
			else
				str[i]='+';
		}
		else if(j>i)
			return;
	}
	return;
}

int main(void)
{
#ifdef InputOutputToFile
	
	//cin redirection
	std::ifstream fin("cin.txt");
	std::streambuf *inbuf = std::cin.rdbuf(fin.rdbuf());

	//cout redirection
	std::streambuf* cout_sbuf = std::cout.rdbuf(); // save original sbuf 
	std::ofstream   fout("cout.txt"); 
	std::cout.rdbuf(fout.rdbuf()); // redirect 'cout' to a 'fout' 
	//std::cout.rdbuf(cout_sbuf); // restore the original stream buffer 
#endif
	int run = 0;
	cin>>run;

	int i=0,count=0;
	
	bool flg=true;

	bool itrFlg = false;
	int tc=1;
	while(run--)
	{
		if(itrFlg)
		{
			cout<<endl;	
			flg=true;
			count=0;
		}
		itrFlg = true;
		//initialize str
		for(i=0;i<100;i++)
			str[i]=NULL;
		
		cin>>str;

		while(flg)
		{
			if(str[i]=='-')
			{
				if(str[0]=='-')
				{
					flip(i);
					count++;
				}
				else
				{
					while(str[--i]!='+');
					if(str[i]=='+')
					{
						flip(i);
						count++;
					}
				}
				i=99;
			}
			else
			{
				--i;
				if(i<0)
					flg=false;
			}
		}
		
		cout<<"Case #"<<tc++<<": "<<count;
	}
	
	return 0;
}