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
	int i, t, z, j;
	string a;
	//vector <char> a;
	fin>>t;
    fin.ignore();
	for(z=1;z<=t;z++)
	{
        getline( fin, a );
        cout<<a<<endl;
	    j=0;
        for(i=0;i<a.size()-1;i++) {
            if(a[i]!=a[i+1])
                j++;
        }
        if(a[a.size()-1]=='-')
            j++;
        fout<<"Case #"<<z<<": "<<j<<endl;
		a.clear();
    }
    fin.close();
	fout.close();
	return 0;
}
