#include<iostream>
#include<fstream>
#include<string>

using namespace std;

int tol[1111];
bool is[1111];
int m, n;

bool ok(int p)
{
	if (p<10) return true;
	if (p<100) {
		return (p%10 == p/10);
	}
	else {
		return (p%10 == p/100);
	}
	return false;
}

int main(){
	int i, j, k, a, b, c, t, tt, res;
	bool fd;
	ifstream fin("C-small-attempt0.in");
	ofstream fout("out.txt");
	tol[0] = 0;
	for (i=0; i<=1000; i++) is[i] = false;

	for (i=1; i<=40; i++) if ((ok(i)) && (i*i<=1000) && (ok(i*i))) is[i*i]=true;
	for (i=1; i<=1000; i++) if (is[i]) tol[i] = tol[i-1]+1;
	else tol[i]=tol[i-1];
	fin >> tt;
	for (t=1; t<=tt; t++){
		fin >> n >> m;		
		fout << "Case #" << t << ": " << tol[m] - tol[n-1] << endl;
	}
}