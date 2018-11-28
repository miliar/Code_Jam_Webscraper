#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<cmath>
#include<iostream>
#include<fstream>
#include<algorithm>
#include<string>
#include<vector>
#include<map>
#include<set>
using namespace std;
ifstream fin ("A-small-attempt0.in");
ofstream fout ("A-small-attempt0.out");
struct PAS{
	long long o,e,p;
}pa[2003];
long long sum,now,n;
long long f[2003][2];
int la[2003];
bool cmp (PAS u,PAS v){
	return u.e<v.e || u.e==v.e && u.o<v.o;
}
int main(){
	int i,j,k,m,T,TI;
	fin >> T;
	for (TI=1;TI<=T;++TI){
		fin >> n >> m;
		sum=now=0;
		for (i=0;i<m;++i)
			fin >> pa[i].o >> pa[i].e >> pa[i].p;
		for (i=0;i<m;++i){
			sum+=((pa[i].e-pa[i].o)*n-(((pa[i].e-pa[i].o-1LL)*(pa[i].e-pa[i].o))>>1))*pa[i].p;
//			fout << sum << endl;
		}
//		fout << endl;
		while (1){
			sort(pa,pa+m,cmp);
//			for (i=0;i<m;++i)
//				fout << pa[i].o << ' ' << pa[i].e << ' ' << pa[i].p << endl;
//			fout << endl;
			for (i=0;i<m;++i){
				f[i][0]=pa[i].p;
				f[i][1]=pa[i].e-pa[i].o;
				la[i]=-1;
				for (j=0;j<i;++j)
					if (pa[j].o<pa[i].o && pa[i].o<=pa[j].e && pa[j].e<pa[i].e)
						if (f[i][1]<f[j][1]+pa[i].e-pa[j].e){
							f[i][1]=f[j][1]+pa[i].e-pa[j].e;
							f[i][0]=min(f[j][0],pa[i].p);
							la[i]=j;
						}
			}
//			for (i=0;i<m;++i)
//				fout << f[i][0] << ' ' << f[i][1] << endl;
//			fout << endl;
			for (k=-1,j=0,i=0;i<m;++i)
				if (f[i][1]>pa[i].e-pa[i].o)
					if (j<f[i][1]){
						j=f[i][1];
						k=i;
					}
//			fout << k << endl;
			if (k==-1) break;
			pa[m].o=pa[k].e-f[k][1];
			pa[m].e=pa[k].e;
			pa[m].p=f[k][0];
			++m;
			for (j=f[k][0],i=k;la[i]>=0;i=la[i]){
				pa[i].p-=j;
				pa[m].o=pa[i].o;
				pa[m].e=pa[la[i]].e;
				pa[m].p=j;
				++m;
				if (pa[i].p==0) pa[i]=pa[--m];
			}
//			fout << m << endl;
			pa[i].p-=j;
			if (pa[i].p==0) pa[i]=pa[--m];
//			fout << m << endl;
		}
		for (i=0;i<m;++i)
			now+=((pa[i].e-pa[i].o)*n-(((pa[i].e-pa[i].o-1LL)*(pa[i].e-pa[i].o))>>1))*pa[i].p;
//		fout << sum << ' ' << now << endl;
		fout << "Case #" << TI << ": " << (sum-now) << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
