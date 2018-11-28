#include<iostream>
#include<stack>
#include<fstream>
#include<string>

using namespace std;

void emptystack(stack<char> &s)
{
	while(s.size()!=0)
	{
		s.pop();
	}
}
bool checkstack(stack<char> s)
{
		char c;
		c=s.top();
		
	while(s.top()!='x')
	{
		if(s.top()==c)
		{
			s.pop();
		}
		else if(s.top()!=c)
			return true;

	}
	if(c=='+')
	return false;

	else return true;
}
int main()
{
	stack<char> s;
	string str;
	int i=0,counter=0,j_2=1;
	char* arr;
	int j=0;
	int k=0;
	ifstream fin("file.txt");
	ofstream fout("output.txt");

	int testcases=0;



	fin>>testcases;
	while(testcases!=0)
	{

		emptystack(s);
	fin>>str;
	int len=str.length();

	arr=new char [len];
	
	i=len-1;
	s.push('x');
	while(len!=0)
	{
		s.push(str[i]);


		i--;
		len--;
	}



	while(checkstack(s))
	{
		j=0;
		
		

		arr[j]=s.top();
		s.pop();
		while(arr[j]==s.top() && s.top()!='x')
		{
				j++;
				arr[j]=s.top();
				s.pop();
		}
	
		k=j;
		
		while(k!=-1)
		{
				if(arr[k]=='+')
				{
				arr[k]='-';
				}
				else if(arr[k]=='-')
				{
					arr[k]='+';
				}

						k--;
		}
	
		k=j;
		
		while(k!=-1)
		{
			s.push(arr[k]);
			arr[k]='\0';
			k--;
		}
	
	counter++;
	}


		fout<<"Case #"<<j_2<<": "<<counter<<endl;
		counter=0;
		j_2++;
	testcases--;

		}
	arr=nullptr;
return 0;


}