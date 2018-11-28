#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <utility>

using namespace std;

int main()
{
	ifstream fin("C.in");
	ofstream fout("C.out");

	map<pair<string, string> , string> mul;
	mul[make_pair("1","1")] = "1";
	mul[make_pair("1","i")] = "i";
	mul[make_pair("1","j")] = "j";
	mul[make_pair("1","k")] = "k";
	mul[make_pair("i","1")] = "i";
	mul[make_pair("i","i")] = "-1";
	mul[make_pair("i","j")] = "k";
	mul[make_pair("i","k")] = "-j";
	mul[make_pair("j","1")] = "j";
	mul[make_pair("j","i")] = "-k";
	mul[make_pair("j","j")] = "-1";
	mul[make_pair("j","k")] = "i";
	mul[make_pair("k","1")] = "k";
	mul[make_pair("k","i")] = "j";
	mul[make_pair("k","j")] = "-i";
	mul[make_pair("k","k")] = "-1";

	int t;
	fin >> t;
	for(int tnum = 1; tnum <= t; ++tnum)
		{
			int l, x;
			string str;
			fin >> l >> x >> str;
			
			string newstr;			
			for(int i = 1; i <= x; ++i)
				newstr += str;
				
			string prod = "1";
			bool minus = false;
			int i,j,k;
			bool ifound = false, jfound = false, kfound = false;
			
			string s;
			for(i = 0; i < l*x; ++i)
				{			
					if(prod[0] == '-')
						{
							minus = true;
							prod.erase(0,1);							
						}	
					s = newstr[i];		
					prod = mul[make_pair(prod,s)];					
					if(prod[0] == '-')
						{
							if(minus)
								{
									prod.erase(0,1);
									minus = false;
								}	
						}
					if(prod.compare("i") == 0 && !minus)
						{ ifound = true; break;	}						
				}
			prod = "1";
			minus = false;	
			for(j = i + 1; j < l*x; ++j)
				{			
					if(prod[0] == '-')
						{
							minus = true;
							prod.erase(0,1);							
						}		
					s = newstr[j];			
					prod = mul[make_pair(prod,s)];					
					if(prod[0] == '-')
						{
							if(minus)
								{
									prod.erase(0,1);
									minus = false;
								}	
						}
					if(prod.compare("j") == 0 && !minus)
						{ jfound = true; break;	}						
				}	
			prod = "1";
			minus = false;	
			for(k = j + 1; k < l*x; ++k)
				{			
					if(prod[0] == '-')
						{
							minus = true;
							prod.erase(0,1);							
						}		
					s = newstr[k];			
					prod = mul[make_pair(prod,s)];					
					if(prod[0] == '-')
						{
							if(minus)
								{
									prod.erase(0,1);
									minus = false;
								}	
						}					
				}
			if(prod.compare("k") == 0 && !minus)
				kfound = true;	
			string ans;
			if(ifound && jfound && kfound)
				ans = "YES";
			else
				ans = "NO";				
			fout << "Case #" << tnum << ": " << ans << endl;
		}
	return 0;
}
