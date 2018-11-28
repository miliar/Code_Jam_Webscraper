#include<fstream>
#include<algorithm>
using namespace std;
int T,n;
long long v[50],A,B;

inline bool Palindrom(long long x)
{
	long long aux,y,cif;
	aux=x;
	y=0;
	while(aux)
	{
		cif=aux%10LL;
		y=y*10LL+cif;
		aux/=10LL;
	}
	if(x==y)
		return true;
	return false;
}

inline void Precalculare()
{
	int i;
	for(i=1;i<=10000000;i++)
		if(Palindrom(1LL*i) && Palindrom(1LL*i*i))
			v[++n]=1LL*i*i;
}

int main()
{
	int t,st,dr;
	Precalculare();
	ifstream fin("C.in");
	ofstream fout("C.out");
	fin>>T;
	for(t=1;t<=T;t++)
	{
		fin>>A>>B;
		st=lower_bound(v+1,v+n+1,A)-v;
		dr=lower_bound(v+1,v+n+1,B)-v;
		while(v[dr]>B)
			dr--;
		fout<<"Case #"<<t<<": "<<(dr-st+1)<<"\n";
	}
	fin.close();
	fout.close();
	return 0;
}
