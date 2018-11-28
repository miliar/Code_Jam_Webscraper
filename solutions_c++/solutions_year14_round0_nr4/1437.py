#include <cstdlib>
#include <fstream>
#include <iomanip>
#include <algorithm>

using namespace std;

ifstream fin("D-large.in");
ofstream fout("out.txt");

int main() {
	int t,n,ptsWar,ptsDec,kenPos;
	fin>>t;
	double ken[1000],naomi[1000];
	bool used[1000];
	for (int test=0;test<t;test++) {
		fin>>n;
		ptsWar=ptsDec=kenPos=0;
		memset(used,0,sizeof(used));
		for(int i=0;i<n;i++) {
			fin>>naomi[i];
		}
		for(int i=0;i<n;i++)
			fin>>ken[i];
		sort(naomi,naomi+n);
		sort(ken,ken+n);
		for(int i=0;i<n;i++)
			if(naomi[i]>ken[kenPos]) ptsDec++,kenPos++;
		bool flag=false;
		kenPos=0;
		for(int i=0;i<n && !flag;i++) {
			flag=true;
			for(int j=kenPos;j<n && flag;j++)
				if(ken[j]>naomi[i] && !used[j]) flag=false,used[j]=true,kenPos=j;
			if(flag) ptsWar=n-i;
		}
		fout<<"Case #"<<test+1<<": "<<ptsDec<<" "<<ptsWar<<endl;
	}
	return 0;
}