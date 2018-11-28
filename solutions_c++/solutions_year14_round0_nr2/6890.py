#include <iostream>
#include <fstream>

using namespace std;

ofstream fout ("file.out");

int t;

double a,b,c,ans,x,z;

int main()
{
	cin >> t;	
	
	for (int i = 1; i <= t; i++)
	{
		cin >> a >> b >> c;
		
		ans = c/2,x = a/2,z = 2;
		
		int y = c+1;
		for (int h = 1; h <= y; h++)
			z+=b,ans = min(ans,x+c/z),x += a/z;
		
		fout.precision(7);
		
		fout << fixed << "Case #" << i << ": " << ans << "\n";
	}
}
