#include <fstream>
#include <cmath>
#include <algorithm>
#include <map>
#include <string>
#include <vector>
#include <string.h>
using namespace std; vector <char> array; vector <char> array2;
int main()
{
	ofstream fout("yayz.out");
	ifstream fin("A-small-attempt0 (6).in");
	int a; fin >> a;
	for (int g=0; g<a; g++)
	{
		int l; fin >> l; string c,d; fin >> c >> d; 
		int ll=g;
		for (int g=0; g<c.length(); g++)
		{
			if (g==0)
			{
				array.push_back(c[g]);
			}
			else
			{
				if (c[g]!=c[g-1])
				{
					array.push_back(c[g]);
				}
				
			}
		}
		for (int g=0; g<d.length(); g++)
		{
			if (g==0)
			{
				array2.push_back(d[g]);
			}
			else
			{
				if (d[g]!=d[g-1])
				{
					array2.push_back(d[g]);
				}
			}
		}int t=0;
		if (array.size()==array2.size())
		{
			for (int g=0; g<array.size(); g++)
			{
				if (array[g]!=array2[g])
				{
					t=1;
					fout << "Case #" << ll+1 << ": " << "Fegla Won" << '\n';break;
				}
			}
			if (t==0)
			{
				int pointer1=0; int pointer2=0; int ans=0; 
				for (int g=0; g<array.size(); g++)
				{
					char tt=array[g];int counter=0; int counter1=0;
					while (tt==c[pointer1] && pointer1<c.length())
					{
						pointer1+=1;
						counter++; 
					}
					while (tt==d[pointer2] && pointer2<d.length())
					{
						pointer2+=1;counter1++;
					}
					ans+=abs(counter1-counter);
					
				}
				fout << "Case #" << ll+1 << ": " << ans << '\n';
			}
			
		}
		else
		{
			fout << "Case #" << ll+1 << ": " << "Fegla Won" << '\n';array.clear(); array2.clear();continue;
		}
		array.clear(); array2.clear();
	}
	
	
	
	
	
	
	
	
	
	
	
	
}
