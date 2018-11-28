#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

bool isFair(long long in)
{
	long long i, j;
	for(i = 1; i*10 <= in; i *= 10);
	for(j = 1; j < i; j *= 10, i /= 10)
		if(((in/i)%10) != ((in/j)%10))
			return false;
	return true;
}

vector<long long> all;

long long A, B;
long long solve()
{
	long long i, ret = 0;
	i = sqrt(A);
	while(i*i < A)
		i++;
	for(; i*i <= B; i++)
		if(isFair(i) && isFair(i*i))
		{
			all.push_back(i*i);
			cout<<i<<' '<<i*i<<endl;
			ret++;
		}
	return ret;
}

int main()
{
	FILE *in,*out;
//	char line[1000];
	int T, t;
	A=1;
	B=1000000000000000;
	solve();
	in = fopen("C.in","r");
	out = fopen("C.out","w+");
//	fgets(line,999,in);
//	sscanf(line,"%d",&T);
	fscanf(in,"%d",&T);
	for(t = 1; t <= T; t++)
	{
		fscanf(in, "%lld %lld", &A, &B);
//		fprintf(out, "Case #%d: %s\n",t,solve());
		vector<long long>::iterator it;
		long long res = 0;
		for(it = all.begin(); it != all.end(); it++)
			if((*it)>=A && (*it)<=B)
				res++;
		fprintf(out, "Case #%d: %lld\n",t,res);
	}
	fclose(in);
	fclose(out);
}
