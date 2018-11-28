#include<iostream>
#include<vector>
#include<fstream>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
    ofstream fout;
    ifstream fin;
    fout.open("answers.txt");
    fin.open("a.txt");
	int i, t, k, z, p;
	string s, s1;
	fin>>t;
	fin.ignore();
	for(z=1;z<=t;z++)
	{
	    fout<<"Case #"<<z<<": ";
		getline( fin, s );
		int a[s.length()];
		for(i=0;i<s.length();i++)
            a[i]=0;
		k=0;
		for(i=1;i<s.length();i++) {
            if(s[i]>=s[k])
                k=i;
		}
		fout<<s[k];
		a[k]++;
		while(k!=0) {
		    p=0;
            for(i=1;i<k;i++) {
                if(s[i]>=s[p])
                    p=i;
            }
            if(p!=0) {
                fout<<s[p];
                a[p]++;
                k=p;
            }
            else
                break;
		}
        for(i=0;i<s.length();i++) {
            if(a[i]==0)
                fout<<s[i];
        }
        fout<<endl;
	}
    fin.close();
	fout.close();
	return 0;
}
