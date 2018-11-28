#include <iostream>
#include <fstream>

using namespace std;

bool isOK(int x,int y,int a[100][100], int n,int m,int hh)  {
	int h=a[x][y];
	bool ok=true;
	if (h==hh) return true;
	for (int i=0;i<m;++i)
		if (a[x][i]>h) {ok=false; break;}
	if (ok) return ok;
	for (int i=0;i<n;++i)
		if (a[i][y]>h) return false;
	return true;
}

int mysolve(ifstream &fi)  {
	int a[100][100]={0};
	int n(0),m(0),h(0);
	int i(0),j(0),k(0);
	fi>>n>>m;
	for (i=0;i<n;++i)
		for (j=0;j<m;++j) {
			fi>>a[i][j];
			if (a[i][j]>h) h=a[i][j];
		}
	for (i=0;i<n;++i)
		for (j=0;j<m;++j)
			if (!isOK(i,j,a,n,m,h)) return 0;
	return 1;
}

int main()  {
	int n(0);
	int res(0);
	//ifstream fi("B-small-attempt0.in");
	ifstream fi("B-large.in");
	ofstream fo("output.txt");
	fi>>n;
	for (int i(0);i<n;++i)  {
		res=mysolve(fi);
		cout<<"Case #"<<i+1<<": ";		fo<<"Case #"<<i+1<<": ";
		if (res==1) {cout<<"YES\n";		fo<<"YES\n";}
		else		{cout<<"NO\n";		fo<<"NO\n";}
	}
	//cin>>n;
	return 0;
}