/*Vladimir Ignatiev 2014*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

#define rep(A,B) for(int A=0;A<B;++A)
#define repi(A,I,B) for(int A=I;A<B;++A)
#define repd(A,B) for(int A=B-1;A>=0;--A)
#define repdi(A,I,B) for(int A=B-1;A>=I;--A)
#define repall(A,F) for_each(A.begin(),A.end(),F);

vector<double> An,Ak;
int N;
int Rw,Rdw;

void f()
{	
	sort(An.begin(),An.end());
	sort(Ak.begin(),Ak.end());

	vector<double> An_save(An);
	
	Rdw=N;

	repd(i,N)
	{
		if(Ak[i]>*An.rbegin())
		{
			Rdw--;
			An.erase(An.begin());
		}
		else
			for(auto pos=An.begin();pos!=An.end();pos++)
			{
				if(Ak[i]<*pos) {An.erase(pos);break;}
			}
	}

	An=An_save;

	Rw=0;

	rep(i,N)
	{
		if(An[i]>*Ak.rbegin())
		{
			Rw++;
			Ak.erase(Ak.begin());
		}
		else
			for(auto pos=Ak.begin();pos!=Ak.end();pos++)
			{
				if(An[i]<*pos) {Ak.erase(pos);break;}
			}
	}

}

int main()
{
	FILE* In=fopen("D.in","r");if(!In) return 1;
	FILE* Out=fopen("D.res","w");if(!Out) return 2;

	int nCount;
	fscanf(In,"%d",&nCount);
	rep(i,nCount)
	{
		fprintf(Out,"Case #%d: ",i+1);
		printf("%d\n",i);
		fscanf(In,"%d",&N);
		double d;
		An.clear();
		Ak.clear();

		rep(n,N)
		{
			fscanf(In,"%lf",&d);
			An.push_back(d);
		}

		rep(n,N)
		{
			fscanf(In,"%lf",&d);
			Ak.push_back(d);
		}

		f();
		fprintf(Out,"%d %d\n",Rdw,Rw);
	};
	fclose(In);
	fclose(Out);
	return 0;
}