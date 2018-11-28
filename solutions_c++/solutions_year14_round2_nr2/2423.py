#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
	fstream plik;
	fstream out;
	out.open("out.txt");
	plik.open("plik.txt");
	int n;
	plik>>n;
	for(int i=0;i<n;i++)
	{
        int a,b,k;
        plik>>a>>b>>k;
        long long s=0;
        for(long j=0;j<a;j++)
        {
            for(int z=0;z<b;z++)
            {
                if((j&z)<k)
                    s++;
            }
        }
	    out<<"Case #"<<i+1<<": "<<s<<endl;
	}
}
