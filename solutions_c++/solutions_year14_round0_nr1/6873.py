#include <iostream>
#include <fstream>
using namespace std;
int main(){
	ifstream fin("A-small-attempt3.in");
	ofstream fout("A-small-attempt3.out");
	int T,a[17],i,j,n,x,s;
	bool flag;
	fin>>T;
	for (j=1;j<=T;j++){
		fin>>n;
		for (i=1;i<=16;i++) a[i]=0;
		for (i=0;i<=15;i++){
			fin>>x;
			if ((i/4)==n-1) a[x]++;
		}
		fin>>n;
		for (i=0;i<=15;i++){
			fin>>x;
			if ((i/4)==n-1) a[x]++;
		}
		s=-1;
		flag=true;
		for (i=1;i<=16;i++)
			if (a[i]==2) { if (s==-1) s=i; else flag=false;}
		fout<<"Case #"<<j<<": ";
		if (s==-1) fout<<"Volunteer cheated!";
		else if (flag==true) fout<<s;
		else fout<<"Bad magician!";
		fout<<endl;
	}
	fin.close();
	fout.close();
}