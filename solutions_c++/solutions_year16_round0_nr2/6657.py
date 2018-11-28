#include<bits/stdc++.h>
using namespace std;

int main()
{  ifstream in;
    ofstream out;
    in.open("input.txt");
    out.open("output.txt");
int t;
in>>t;
for(int i=0;i<t;i++)
{	
	string s;
	int swapped = 0;
	in>>s;
	int visited,length2;
	int length = s.length();

	char *frnt, *endd;
	start : frnt = &(s[0]);
	endd = &(s[length-1]);
	length2 = length-1;
	visited = 0;
	while((*frnt)=='-')
	{
		*frnt = '+';
		visited = 1;
		frnt++;

	}
	frnt = &(s[0]);
	if(visited == 1)
	{
		swapped++;
	}
	while((*endd)=='+')
	{
		endd--;
		length2--;
	}
	if(length2>=1)
	{
		int x = 0;
		int rear = length2 ;
		char temp;
		while(x<(length2+1)/2)
		{
			temp = s[x];
			s[x] = s[rear];
			s[rear] = temp;
            rear--;
			x++;
		}
	swapped++;
	goto start;
	}
	out<<"Case #"<<i+1<<": "<<swapped<<endl;
}

	in.close();
	out.close();
	return 0;
}
