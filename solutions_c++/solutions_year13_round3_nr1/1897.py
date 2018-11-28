#include <iostream>
#include <vector>
#include <map>
#include <fstream>

using namespace std;

bool isVowel(char c)
{
	return c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u';
}

int main()
{
	int testCases;
	ifstream fin;
	ofstream fout;
	
	fin.open("input2.txt");
	fout.open("output.txt");
	
	fin >> testCases;
	
	for(int i=1; i<=testCases; i++)
	{
		int n, inrowcount, count, total=0, unique=0;
		string name;
		
		fin >> name;
		fin >> n;
	/*	
		count = 0;
		
		for(int j=0; j<name.size(); j++)
		{
			if(!isVowel(name[j]))
			{
				count++;
				
				if(count==n)
				{
							// itself, before, after
					total += 1 + (j-n+1) + (name.size()-j-1);
				}
				else if(count>n)
				{
					
					total += 1 + (j-n+1) + (name.size()-j-1) - 1;
				}
				
				if(count>=n && ((j+1<name.size() && isVowel(name[j+1])) || j+1==name.size()))
				{
					unique++;
				}
			}
			else
			{
				count = 0;
			}
		}
		
		total++;
		total -= unique;
		*/
		
		for(int j=0; j<name.size(); j++)
		{
			if(isVowel(name[j]))
			{
				name[j] = '0';
			}
			else
			{
				name[j] = '1';
			}
		}
		
		string query = "";
		for(int j=0; j<n; j++)
		{
			query = query + '1';
		}
		
		for(int j=0; j<name.size(); j++)
		{
			for(int k=1; k<name.size()-j+1; k++)
			{
				string str = name.substr(j,k);
				if(str.find(query)!=-1)
				{
					total++;
				}
			}
		}
		
		fout << "Case #" <<i<< ": " << total << endl;
	}
	
	fin.close();
	fout.close();
	
	return 0;
}