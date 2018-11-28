
#include <iostream>
#include<string>
#include <fstream>


using namespace std;
ifstream in;
ofstream out;
//int input[1001];

int inviteGuest()
{
	char a;
	int temp=0;
	int total=0;
	int guest=0;
	int S=0;
	in>>S;
	for(int k=0;k<=S;k++)
	{
		int needed=0;
		in>>a;
		temp=a-'0';
		//input[k]=temp;
		if(total<S)
		{if(total<k)
			{
				needed=k-total;
				guest=guest+needed;
			}
			total=total+temp+needed;
		}
	}
	return guest;

}

void printResult(int test, int guest)
{
	out<<"Case #"<<test<<": "<<guest;
}

int main()
{
	in.open("A-large.in");
	out.open("A-large.out");
	if(!in)
	{
		cout<<"no file"<<endl;
	}
	int testCase=0;
	in>>testCase;
	for(int i=0;i<testCase;i++)
	{
		int result;

		result=inviteGuest();
		printResult(i+1, result);
		if(i!=testCase-1)
		{out<<endl;}
	}
	
	out.close();
	in.close();
	return 0;
}