#include<bits/stdc++.h>
using namespace std;

int main()
{
	
	int test;
	int count=1;
	
	ifstream infile;
	ofstream outfile;
	
	infile.open("A.in");
	outfile.open("result.txt");
	
	infile >> test;
	
	while(test--)
		{
			deque <char> d;
			int i;
			
			char s[1001];
			
			infile >> s;
			
			char ch=s[0];
			d.push_front(ch);
			for(i=1;i<strlen(s);i++)
				{
					
					if(s[i]>=d[0])
						{
							d.push_front(s[i]);
							
						}
					else
						{
							d.push_back(s[i]);
						}
				}
			outfile<< "Case #"<<count++<<": ";
			
			for(i=0;i<strlen(s);i++)
				outfile <<d.at(i);
			
			outfile << endl;
	}
	return 0;
}
