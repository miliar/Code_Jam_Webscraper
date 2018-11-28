#include<iostream>

using namespace std;

int main()
{
	int a,b,c,i,j,k,t,n,m;
	cin >> t;
	string str1;
	for(i=0;i<t;i++)
	{
		cin >> n >> str1;
		int start=0;
		int count=0;
		int counter=0;
		while(start<n && counter<str1.length())
		{
			if(counter<=start)
				start+=str1[counter]-'0';
			else
			{
				count+=counter-start;
				start+=counter-start;
				start+=str1[counter]-'0';
			}
			counter++;
		}
		if(start<n)
			count+=n-start;
		cout << "Case #" << i+1 << ": " << count << endl;
	}
	return 0;
}
