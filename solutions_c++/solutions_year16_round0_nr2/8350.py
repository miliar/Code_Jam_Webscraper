#include <iostream>
#include <string>
using namespace std;
long long int times; 

char flip_char(char a) {return (a=='-')?'+':'-';}

void reverse_str(string &a)
{
	int s=0, e=a.length()-1;
	while (s < e)
	{
		char t = a[s];
		a[s] = a[e];
		a[e] = t;
		s++; e--;
	}
}

void flip_stack(string &a, int i)
{
	// get the substring from a
	string sub = a.substr(0, i+1);
	//reverse that string
	reverse_str(sub);
	// then reverse ever char in shit
	for(int j=0; j<sub.length(); j++)
		a[j] = flip_char(sub[j]);
}

int first_slot_same_as_first(string a)
{
	char f=a[0];
	for (int i=1; i<a.length(); i++)
		if (a[i] != f) return i;
	return a.length();
}

bool stack_ready(string a)
{
	for(int i=0; i<a.length(); i++) 
		if(a[i] == '-') return false;
	return true; 
}

int main()
{
	cin>>times;
	for (int i=0; i<times; i++)
	{
		string pancake;
		long long int count=0;
		cin>>pancake;
		while(!stack_ready(pancake))
		{
			int fs = first_slot_same_as_first(pancake);
			//cout<<"fs:"<<fs<<endl;
			flip_stack(pancake, fs-1);
			//cout<<"after flip:"<<pancake<<endl;
			count++;
		}
		cout<<"Case #"<<i+1<<": "<<count<<endl;
	}
	
	return 0;
}