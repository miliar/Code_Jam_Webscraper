#include<iostream>
#include<vector>
#include<fstream>
#include<string>
#include<sstream>
#include<cstdlib>
#include<cmath>

using namespace std;


int main()
{
    int total;
    int i = 1;
    int K,C,S;
	ifstream infile;
	ofstream ofile;
	ofile.open("output.txt");
	infile.open ("D-small-attempt1.in");
    infile>>total;

        while(i <=total)
        {
            infile>>K>>C>>S;
                int n = S;
        long long stride = pow(K,C-1);
        long long x = 1;
        ofile<<"Case #" << i << ": "<<"1";

        for(int j=1;j<n;j++)
        {
        x += stride;
        ofile<<" "<<x;
        }
        ofile<<endl;
            i ++;
        }

	infile.close();
	ofile.close();
	return 0;
}


