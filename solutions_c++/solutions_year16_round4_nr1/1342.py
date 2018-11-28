#include<cstdio>
#include<string>
int count (std::string& s, char a)
{
	int res=0;
	for(auto e:s)
	{
		if(e==a)
			res++;
	}
	return res;
}
bool ok(std::string& S,int p,int r,int s)
{
	return count(S,'P')==p and count(S,'R')==r and count(S,'S')==s;
}
std::string test()
{
	int n,r,p,s;
	scanf("%d%d%d%d",&n,&r,&p,&s);
	std::string P="P",R="R",S="S";
	for(int i=0;i<n;i++)
	{
		std::string P1,R1,S1;
		if(P<R)P1=P+R;
		else P1=R+P;
		if(R<S)R1=R+S;
		else R1=S+R;
		if(S<P)S1=S+P;
		else S1=P+S;
		P=P1;
		S=S1;
		R=R1;
	}
	std::string res="ZZ";
	if(ok(P,p,r,s) and P<res)res=P;
	if(ok(R,p,r,s) and R<res)res=R;
	if(ok(S,p,r,s) and S<res)res=S;
	return res;
}
int main()
{
	int t;
	scanf("%d",&t);
	for (int i=1;i<=t;i++)
	{
		std::string a=test();
		if(a==std::string("ZZ"))a="IMPOSSIBLE";
		printf("Case #%d: %s \n",i,a.c_str());
	}
}
