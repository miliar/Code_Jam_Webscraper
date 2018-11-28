#include<bits/stdc++.h>
#include<fstream>
using namespace std;
int main()
{
	ifstream in("A-large.in");
	ofstream out("output_large.txt");
	int t;
	in>>t;
	int m=t;
	while(t--)
	{
		string s="";
		in>>s;
		int size=s.length();
		char key;
		 int l=0,k=1; // *always* initialize variables
        for (int i=1; i<size; ++i) // use pre-increment to avoid unneccessary temorary object
        {
                if(s[0]>s[i])
                {
                	s[k++]=s[i];
				}
				else
				{
					char z=s[i];
					for(int j=i;j>0;j--)
					{
						s[j]=s[j-1];
					}
					s[0]=z;
					k++;
				}
        }
		cout<<s<<"\n";
		out<<"Case #"<<m-t<<": "<<s<<"\n";
	}
}
