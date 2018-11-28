#include <iostream>
#include <fstream>
#include <string>

using namespace std;

bool checkallpos(string s)
{
	bool check=true;
	for(int i=0;i<s.length();i++)
	{
		if(s[i]!='+')
		{
			check=false;
			break;
		}
	}

	return check;
}

string trimlastpos(string s)
{
	int i=s.length()-1;
	while(s[i]=='+')
	{
		s[i]='-';
		i--;
	}

	return s;
}

main()
{
	ifstream in;
    in.open("Revenge_Pancakes_input_L.txt");
    ofstream out;
    out.open("Revenge_Pancakes_ouput_L.txt");
	int t;
	in>>t;

	for(int i=0;i<t;i++)
	{

		string s;
		in>>s;
		int count=1;

		if(checkallpos(s))
        {
            cout<<"Case #"<<i+1<<": "<<0<<endl;
            out<<"Case #"<<i+1<<": "<<0<<endl;

        }
		else
		{

			char current=s[0];
			s=trimlastpos(s);
			for(int j=1;j<s.length();j++)
			{
				if(s[j]!=current)
				{
					current=s[j];
					count++;
				}
			}

			cout<<"Case #"<<i+1<<": "<<count<<endl;
			out<<"Case #"<<i+1<<": "<<count<<endl;


		}

	}
}
