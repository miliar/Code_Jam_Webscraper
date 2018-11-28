#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;
int main()
{
	//FILE *pfile;
	//pfile= fopen("p2ans.txt","w");
	//ifstream fin("B-large.in.txt");
	double f,x,c,pr,count;
	int t,k;
	cin>>t;
	for(k=0;k<t;k++)
	{
		count=0.0;
		cin>>c>>f>>x;
		pr=2.0;
		while(((x-c)/pr)>(x/(pr+f)))
		{
			count+=(c/pr);
			pr+=f;
		}
		count+=(x/pr);
		printf("Case #");
		printf("%i: ",k+1);
		printf("%.7lf\n",count);
	}
	return 0;
} 

