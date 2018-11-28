#include <cstdio>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;
const int MAXN=1000005;
vector <int> X;
int T[MAXN];
int n,t,siz,c,mno;
int main()
{
	fstream plik;
    plik.open( "C:/a.txt", ios::out);
    for(int i=1; i<MAXN; ++i)
    	T[i]=1000000000;
    T[1]=1;
    for(int i=1; i<1000001; ++i)
    {
    	T[i+1]=min(T[i+1],T[i]+1);
    	X.clear();
    	c=i;
    	while(c>0)
    	{
    		X.push_back(c%10);
    		c/=10;
    	}
    	siz=X.size();
    	mno=1;
    	for(int j=siz-1; j>=0; --j)
    	{
    		c+=mno*X[j];
    		mno*=10;
    	}
    	T[c]=min(T[c],T[i]+1);
    }
	scanf("%d", &t);
	for(int i=1; i<=t; ++i)
	{
		scanf("%d", &n);
		plik<<"Case #"<<i<<": "<<T[n]<<endl;
	}
	plik.close();
}
