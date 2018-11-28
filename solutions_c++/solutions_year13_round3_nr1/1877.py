#include <iostream>
#include <string.h>
#include <fstream.h>
#include <algorithm>
#include <stdio.h>

using namespace std;

int main ()
{
ifstream file1;
ofstream file2;
file1.open("inp.txt",ios::in);
file2.open("out.txt");
int t;
file1>>t;

int cnt=1;
while (t--)
{
string str;
int n;
	file1>>str;
	file1>>n;
	int count=0;
	for (int i=0;i<str.length()-n+1;++i)
	{
		for (int j=i+n-1;j<str.length();++j)
		{
            int precount=0;
			for (int k=i;k<=j;++k)
			{
				if (str[k]!='a' && str[k]!='e' && str[k]!='i' && str[k]!='o' && str[k]!='u')
				{
					precount++;
				}
				else if (precount<n)
				{
               precount=0;
            }
			}
			if (precount>=n)
			   {
             count++;
           }
		}
	}
file2<<"Case #"<<cnt++<<": "<<count<<endl;

}



	
file2.close();
file1.close();
	return 0;
} 
