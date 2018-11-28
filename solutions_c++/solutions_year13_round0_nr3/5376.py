
#include <iostream>
#include <fstream>
#include <string>
#include <map>
#include <queue>
#include <stdio.h>

using namespace std;

int isp(string s) {
    int i = -1, j = s.length();
    while (i < j && s[++i] == s[--j]);
    return i >= j;
}


string convert (int val, int base)
{
	string x;
	do
	{
		x += "0123456789ABCDEFGHIJKLMNOPQRSTVWXYXZ"[val % base];
		val /=base;
	}
	while(val);
	return string(x.rbegin(),x.rend());
}

int main() 
{
	ifstream fin("C-small-attempt1.in");
	ofstream fout ("output.out");
	int n,a,b;
	fin >> n;
	for (int j  = 1; j  <= n; j ++)
	{
		
		fin >> a >> b;
		int c = 0;
		for (int i = a; i <= b; i++)
		{
			if(isp(convert(i,10)))
			{
				
				double raiz = sqrt(i);
				if(raiz - (int )raiz == 0.0)
				{
					
					if(isp(convert(raiz,10)))
					{
						c++;
					}
				}

			}
		}
		fout<<"Case #" <<j<<": "<<c <<endl;
		//printf("Case #%d: %d\n",j,c);


	}
	
   
    
    return 0;
}