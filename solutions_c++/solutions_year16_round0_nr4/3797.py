#include<iostream>
#include<cstdio>
#include<cmath>
#include<fstream>
using namespace std;

int main()
{
	fstream file1,file2;
	file1.open("l.in",ios::in);
	file2.open("g.txt",ios::out);
    long long a,k,c,s,d;
    file1>>a;//scanf("%lld",&a);
    for(int b=1;b<=a;++b)
    {
    	file1>>k>>c>>s;//scanf("%lld%lld%lld",&k,&c,&s);
		file2<<"Case #"<<b<<": ";//printf("Case #%d: ",b);
		if(s<k)
			file2<<"IMPOSSIBLE"<<endl;//printf("IMPOSSIBLE\n");
		else
		{
			d=pow(k,c);
			d=d/k;
			file2<<1;//printf("1");
			for(int q=1;q<k;++q)
			{
				file2<<" "<<1+d*q;//printf(" %lld",1+d*q);
			}
			file2<<endl;//printf("\n");
		}
    }
    return 0;
}

