#include <iostream>
#include<string>
using namespace std;
int scanSMAX()
{
	int a;
	cin>> a;
	return a;
}
string scanString()
{
	string s;
	cin >> s;
	return s;
}
int question_solver(int a,string b)
{
	int res=0,total=0;
	for (int i=0;i< a+1;i++)
	{
		if (i>total)
			{res+=i-total;total=i;}
		total+=(b[i]-'0');
	}
	return res;
}
int main()
{
	int numberOfCases;
	cin >> numberOfCases;
	for (int i=0;i<numberOfCases;i++)
	{
		int a;
		string b;
		a=scanSMAX();
		b=scanString(); 
		cout<< "Case #" <<i+1 <<": "<<question_solver(a,b)<<endl;
	}
}

