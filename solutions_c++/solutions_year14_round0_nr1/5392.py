#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char *argv[]) {
	ifstream fin("A-small-attempt0.in");
	ofstream fout("A-small-attempt0.out");
	int T;
	fin>>T;
	for(int I=0;I<T;I++) {
		bool can_be[17]={false};
		int r,a;
		fin>>r;
		for(int i=0;i<4;i++) { 
			for(int k=0;k<4;k++) { 
				fin>>a;
				if (i+1==r) can_be[a]=true;
			}
		}
		fin>>r;
		for(int i=0;i<4;i++) { 
			for(int k=0;k<4;k++) { 
				fin>>a;
				if (i+1!=r) can_be[a]=false;
			}
		}
		int cr=0;
		for(int i=1;i<17;i++) { 
			if (can_be[i]) { r=i; cr++; }
		}
		if (cr>1) fout<<"Case #"<<I+1<<": Bad magician!"<<endl;
		if (cr==1) fout<<"Case #"<<I+1<<": "<<r<<endl;
		if (cr==0) fout<<"Case #"<<I+1<<": Volunteer cheated!"<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}

