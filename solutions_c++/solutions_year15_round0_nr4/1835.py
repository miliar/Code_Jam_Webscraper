#include<iostream>
#include<fstream>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

void find(long long int tc){

	long long int X=0,R=0,C=0;
	fin>>X>>R>>C;
	if(X==1)
		fout<<"Case #"<<tc<<": "<<"GABRIEL"<<endl;
	else{
		if(((R*C)%X)!=0)
			fout<<"Case #"<<tc<<": "<<"RICHARD"<<endl;
		else{
			if(X==2)
				fout<<"Case #"<<tc<<": "<<"GABRIEL"<<endl;
			else{
				if((R==1)||(C==1))
					fout<<"Case #"<<tc<<": "<<"RICHARD"<<endl;
				else{
					if((R*C)==X)
						fout<<"Case #"<<tc<<": "<<"RICHARD"<<endl;
					else{
						if((R<(X-1))||(C<(X-1)))
							fout<<"Case #"<<tc<<": "<<"RICHARD"<<endl;
						else
							fout<<"Case #"<<tc<<": "<<"GABRIEL"<<endl;
					}
				}
			}
		}
	}
}

int main()
{
	int tc;
	fin>>tc;
	for(int i=1;i<=tc;i++){
		find(i);
	}
	return 0;
}