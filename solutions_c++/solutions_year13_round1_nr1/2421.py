#include <iostream >
#include <fstream >
#include <sstream >
#include <math.h>
using namespace std;
ifstream fin("msp_in.txt");
ofstream fout("msp_out.txt");


int main()
{
	//double PI = 3.1415926535;
	long long N,r,t;
	fin>>N;
	int ans[N];
	int n = 0;
	long long area1,area2,area;
	while(n < N)
	{
	area = 0; int ct;
	
	for(int i = 0; i < N; i++)
	{
		fin>>r>>t;
		ct = 0;
		repeat:
		area1 = r * r;
		r++;
		area2 = r * r;
		area += area2 - area1;
		//area = area;
		
		if(area <= t){ r++; ct++; goto repeat; }
		else{ans[n] = ct; break;}
	}
	n++;
}
for(int j = 0; j < N; j++)fout<<"Case #"<<j+1<<": "<<ans[j]<<"\n";
}
	
