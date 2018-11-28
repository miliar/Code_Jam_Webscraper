#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	int testcase;
	int cas=0;
	
	ifstream inp;
	ofstream out;
	inp.open("input.txt");
	out.open("output.txt");
	inp>>testcase;
	string s;
	int num [10];
	int i,j,k,t;
	string snam [10] = {"ZERO","ONE", "TWO" , "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
	for (i=0;i<10;i++)
		num[i] = 0;
	while (cas < testcase)
	{
		inp>>s;
		for (i=0;i<10;i++)
			num[i] = 0;
		int * ch = new int [s.length()];
		for (i=0;i<s.length();i++)
			ch[i] = 0;
		for (i=0;i<10;i++)
		{
			string st = snam[i];
		
			int fin = 0;
			for (j=0;j<st.length();j++)
			{
				char c = st[j];
				for (k=0;k<s.length();k++)
				{
				
					if (c ==  s[k] && ch[k]==0)
					{
						ch[k] = 1;
						
						fin++;
						break;
					}
				}
				
					
				if (fin == st.length() )
					break;
			}
			
			if (fin == st.length() )
			{
				num[i] = num[i] + 1;
				if (fin < st.length() - fin)
					i = -1;
			}
			else
			{
				for (t=0;t<10;t++)
					ch[t] = 0;
			}
				
			cout<<num[i]<<" ";
		}
		
		delete []ch;
		out<<"Case #"<<cas+1<<": ";
		for (i=0;i<10;i++)
			for (j=0;j<num[i];j++)
				out<<i;
		out<<endl;
		cas++;
		cout<<" end test "<<endl;
	}
	inp.close();
	out.close();
	
	return 0;
}
