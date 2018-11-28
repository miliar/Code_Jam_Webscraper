#include<iostream>
#include<math.h>
#include<fstream>
using namespace std;
int main()
{
    ofstream fout;
    ifstream fin;
    fout.open("answers_d.txt");
    fin.open("d.txt");
	long long unsigned int t, k, c, s, z, i;
	fin>>t;
	for(z=1;z<=t;z++)
	{
	    fin>>k>>c>>s;
        if(s==k)
        {
            fout<<"Case #"<<z<<": ";
            for(i=1;i<=k;i++)
                fout<<i<<" ";
            fout<<endl;
        }
        else
        {
            if(s<(k-c+1)) {
                fout<<"Case #"<<z<<": "<<"IMPOSSIBLE"<<endl;
            }
            else if(c==1) {
                    fout<<"Case #"<<z<<": ";
                    for(i=1;i<=k;i++)
                        fout<<i<<" ";
                    fout<<endl;
                }
                else
                {
                    fout<<"Case #"<<z<<": ";
                    for(i=0;i<=k-c+1;i++) {
                        fout<<2+((k+1)*i)<<" ";
                    }
                    fout<<endl;
                }
            }
        }
    fin.close();
	fout.close();
	return 0;
}
