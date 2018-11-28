#include<iostream>
#include<cstdio>
#include<cstring>
#include<vector>
#include<fstream>
using namespace std;
vector<int> vec;
int main()
{
	fstream file1,file2;
	file1.open("jl.in",ios::in);
	file2.open("c.txt",ios::out);
    int a,n,x,t[3000];
    file1>>a;//scanf("%d",&a);
    for(int b=1;b<=a;++b)
    {
    	vec.clear();
    	memset(t,0,sizeof(t));
    	file1>>n;//scanf("%d",&n);
    	for(int q=0;q<2*n-1;++q)
    	{
    		for(int w=0;w<n;++w)
    		{
    			file1>>x;//scanf("%d",&x);
    			t[x]++;
    		}
    	}
    	for(int q=0;q<2510;++q)
    	{
    		if(t[q]%2)
    			vec.push_back(q);
    	}
    	file2<<"Case #"<<b<<":";//printf("Case #%d:",b); 
    	for(int q=0;q<vec.size();++q)
    		file2<<" "<<vec[q];//printf(" %d",vec[q]);
    	file2<<endl;//printf("\n");
    }
    return 0;
}

