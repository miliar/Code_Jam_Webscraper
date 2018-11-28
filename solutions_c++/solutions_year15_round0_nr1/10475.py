#include<iostream>
using namespace std;

int n;
int person;
int total;
string s;


int main()
	{
		int t;
		void ovation(int);
		cin>>t;
		for( int i = 0 ; i < t ; i++ )
			{
				total = person = 0;
				cin>>n;
				cin>>s;
				ovation(0);
				cout<<"Case #"<<i+1<<": "<<person<<endl;
			}
	}
void ovation(int i)
	{
		if( i > n )
			return;
		int p = s[i] - 48;
		if( total - i >= 0 )
			total += p;
		else
			{
				person += i - total;
				total = i + p; 
			}
		ovation(i + 1);
	}
