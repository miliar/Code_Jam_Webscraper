#include<iostream>
#include<fstream>

using namespace std;
int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("B-large.in");
	fout.open("out.txt");
	int cases;
	fin>>cases;
	
	string s1;
	getline(fin,s1);
	
	for(int n=1;n<=cases;n++)
	{
	    string s2;
		getline(fin,s2);
 	
		int b=0,x=s2.length()-1;
		for(x=s2.length()-1;x>=0;x--)
		{
			if(s2[x]=='-')
			{
				int a=x;
				for(a=x;a>=0;a--)
				{
					if(s2[a]=='+')
					{
						s2[a]='-';
					}	
					else
					{
						s2[a]='+';
					}
					
				}
				b++;
			}
		}	
		fout<<"Case #"<<n<<": "<<b<<endl;
	}
}
