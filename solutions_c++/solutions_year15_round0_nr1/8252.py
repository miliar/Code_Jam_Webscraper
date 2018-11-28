#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main()
{
	vector<vector <int> > x;
	string fn;
	ifstream in;
	ofstream out;
	cout<<"Filename: ";
	cin>>fn;
	in.open(fn.c_str());
	out.open("A-large.out", ios_base::app);
	int c;
	in>>c;
	x.resize(c);
	int max;
	char ch;
	int ci;
	for(int i=0;i<c;++i){
		in>>max;
		x[i].resize(max+2);
		x[i][0]=max;
		for(int j=1;j<max+2;++j){
			in>>ch;
			ci=ch-'0';
			x[i][j]=ci;
		}
	}

	for(int i=0;i<(int)x.size();++i){
		int add=0;
		int s=0;
		if(x[i][0]>0){
			for(int j=2;j<(int)x[i].size();++j){
				s=s+x[i][j-1];
				if(j-1>s){
					add=add+(j-1-s);
					s=j-1;
				}
			}
		}
		out<<"Case #"<<i+1<<": "<<add<<"\n";
	}
    return 0;
}
