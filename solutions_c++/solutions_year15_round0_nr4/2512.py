#include <bits/stdc++.h>
using namespace std;

ifstream fin("D-small-attempt0.in");
ofstream fout("output4.txt");

bool funct(int x,int r, int c) 
{
	bool person = 0;
	if (x == 1)
		person = 1;
    else
	{
		if( ((r*c) % (x*x) == 0) || ((r*c) % (x*(x-1)) == 0))
			person = 1;
	}

	return person;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int t;
	fin>>t;
	int m = t;
	while(t--) 
	{
	    int x, r, c; 
        fin>>x>>r>>c; 
        fout<<"Case #"<<m-t<<": ";
        if(funct(x,r,c))
            fout<<"GABRIEL"<<endl;
        else
            fout<<"RICHARD"<<endl; 
	}
	return 0;
}