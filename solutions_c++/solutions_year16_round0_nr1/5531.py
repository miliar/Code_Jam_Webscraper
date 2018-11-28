#include<iostream>
#include<vector>
#include<fstream>
using namespace std;
int main()
{
    ofstream fout;
    ifstream fin;
    fout.open("answers.txt");
    fin.open("a.txt");
	long long unsigned int j;
	int i, t, n, x, q, z;
	vector <int> a;
	fin>>t;
	for(z=1;z<=t;z++)
	{
		for(i=0;i<10;i++)
			a.push_back(0);
		fin>>n;
		i=1;
		fout<<"Case #"<<z<<": ";
		if(n==0)
			fout<<"INSOMNIA"<<endl;
		else
		{
			while(1)
			{
				j=n*i;
				while(j!=0)
				{
					x=j%10;
					a[x]++;
					j=j/10;
				}
				for(q=0;q<10;q++)
				{
					if(a[q]==0)
						break;
				}
				if(q==10) {
				    j=n*i;
					break;
				}
                i++;
			}
			fout<<j<<endl;
			a.clear();
		}
	}
    fin.close();
	fout.close();
	return 0;
}
