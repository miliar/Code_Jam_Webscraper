#include <iostream>
#include <fstream>
using namespace std;

int main()
{
ifstream fin("2013_square.txt");
ofstream fout("2013_square_out.txt");
int noCase;
fin >> noCase;
for (int i = 1; i <= noCase; i++)
	{
	int a,b;
	fin >> a >> b;
	int ans = 0;
	//1
	if (a<=1 && b>=1) ans++;
	//4
	if (a<=4 && b>=4) ans++;
	//9
	if (a<=9 && b>=9) ans++;
	//121
	if (a<=121 && b>=121) ans++;
	//242
	if (a<=484 && b>=484) ans++;
	fout << "Case #" << i << ": " << ans << endl;
	}
}
