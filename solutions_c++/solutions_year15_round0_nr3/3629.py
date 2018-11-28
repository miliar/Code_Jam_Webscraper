#include <iostream>
#include <string>
#include <fstream>

using namespace std;


string multiply(string s1 , string s2)
{
	if(!s1.compare("i") && !s2.compare("j"))
	{
		return "k";
	}
	else if(!s1.compare("-i") && !s2.compare("i"))
	{
		return "1";
	}
	else if(!s1.compare("i") && !s2.compare("k"))
	{
		return "-j";
	}
	else if(!s1.compare("i") && !s2.compare("-1"))
	{
		return "-i";
	}
	else if(!s1.compare("i") && !s2.compare("1"))
	{
		return "i";
	}
	else if(!s1.compare("-i") && !s2.compare("j"))
	{
		return "-k";
	}
	else if(!s1.compare("-i") && !s2.compare("k"))
	{
		return "j";
	}
	else if(!s1.compare("-i") && !s2.compare("-1"))
	{
		return "i";
	}
	else if(!s1.compare("-i") && !s2.compare("1"))
	{
		return "-i";
	}
	else if(!s1.compare("j") && !s2.compare("i"))
	{
		return "-k";
	}
	else if(!s1.compare("-j") && !s2.compare("j"))
	{
		return "1";
	}
	else if(!s1.compare("j") && !s2.compare("k"))
	{
		return "i";
	}
	else if(!s1.compare("j") && !s2.compare("-1"))
	{
		return "-j";
	}
	else if(!s1.compare("j") && !s2.compare("1"))
	{
		return "j";
	}
	else if(!s1.compare("-j") && !s2.compare("i"))
	{
		return "k";
	}
	else if(!s1.compare("-j") && !s2.compare("k"))
	{
		return "-i";
	}
	else if(!s1.compare("-j") && !s2.compare("-1"))
	{
		return "j";
	}
	else if(!s1.compare("-j") && !s2.compare("1"))
	{
		return "-j";
	}
	else if(!s1.compare("k") && !s2.compare("i"))
	{
		return "j";
	}
	else if(!s1.compare("-k") && !s2.compare("k"))
	{
		return "1";
	}
	else if(!s1.compare("k") && !s2.compare("j"))
	{
		return "-i";
	}
	else if(!s1.compare("k") && !s2.compare("-1"))
	{
		return "-k";
	}
	else if(!s1.compare("k") && !s2.compare("1"))
	{
		return "k";
	}
	else if(!s1.compare("-k") && !s2.compare("j"))
	{
		return "i";
	}
	else if(!s1.compare("-k") && !s2.compare("i"))
	{
		return "-j";
	}
	else if(!s1.compare("-k") && !s2.compare("-1"))
	{
		return "k";
	}
	else if(!s1.compare("-k") && !s2.compare("1"))
	{
		return "-k";
	}
	else if(!s1.compare("1") && !s2.compare("j"))
	{
		return "j";
	}
	else if(!s1.compare("1") && !s2.compare("k"))
	{
		return "k";
	}
	else if(!s1.compare("1") && !s2.compare("-1"))
	{
		return "-1";
	}
	else if(!s1.compare("1") && !s2.compare("i"))
	{
		return "i";
	}
	else if(!s1.compare("-1") && !s2.compare("j"))
	{
		return "-j";
	}
	else if(!s1.compare("-1") && !s2.compare("k"))
	{
		return "-k";
	}
	else if(!s1.compare("-1") && !s2.compare("i"))
	{
		return "-i";
	}
	else if(!s1.compare("-1") && !s2.compare("1"))
	{
		return "-1";
	}
	else if(!s1.compare(s2))
		return "-1";
}

int main()
{
	int T , len , rep;
	string s;
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	string in1 , in2;

	fin>>T;
	int j=1 , check = 0;
	while(T!=0)
	{
		fin>>len;
		fin>>rep;
		fin >>s;

		if(s.compare("ijk"))
		{
			in1 = s[0];
		
			for(int i = 1 ; i<len*rep;i++)
			{
				in2 = s[i%len];
				in1 = multiply(in1,in2);

				if(check == 0)
				{
					if(!in1.compare("i"))
					{
						in1 = s[(i+1)%len];
						i++;
						check++;
					}
				}
				else if(check == 1)
				{
					if(!in1.compare("j"))
					{
						in1 = s[(i+1)%len];
						i++;
						check++;
					}
				}
				else
				{
					if(!in1.compare("k") && i == (len*rep)-1)
					{
						in1 = s[(i+1)%len];
						i++;
						check++;
					}
				}

			}
			if(check == 3)
			{
				fout<<"Case #"<<j<<": YES"<<endl;
			}
			else
			{
				fout<<"Case #"<<j<<": NO"<<endl;
			}
		}
		else
		{
			fout<<"Case #"<<j<<": YES"<<endl;
		}

		
		check = 0;
		T--;
		j++;
	}
	return 1;
}