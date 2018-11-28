#include<bits/stdc++.h>
using namespace std;
int main(void)
{
    ifstream fin;
	ofstream fout;
	fin.open("A-large (1).in");
fout.open("round1lf.txt");
	int t,c,i,l;
	string old,updated;
	fin>>t;
	c=1;
	while(t--)
    {
        fin>>old;
        l=old.length();
        updated=old[0];
        for(i=1;i<l;i++)
        {

            if(old[i]>=updated[0]) updated=old[i]+updated;
            else updated=updated+old[i];
        }
        fout<<"Case #"<<c<<": "<<updated<<endl;
        c++;
    }
	return 0;

}
