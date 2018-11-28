#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;

int main()
{
	fstream file1,file2;
	file1.open("k.in",ios::in);
	file2.open("k.txt",ios::out);
	bool use[15];
    int a,n,m,t,ans;
    file1>>a;//scanf("%d",&a);
    for(int b=1;b<=a;++b)
    {
    	file1>>n;//scanf("%d",&n);
    	memset(use,0,sizeof(use));
    	file2<<"Case #"<<b<<": ";//printf("Case #%d: ",b); 
    	if(n==0)
    	{
			file2<<"INSOMNIA"<<endl;//printf("INSOMNIA\n");
			continue;
		}
    	for(int q=1;q<=100;++q)
    	{
    		t=1;
    		m=n*q;
    		ans=m;
    		while(m)
    		{
    			use[m%10]=1;
    			m/=10;
    		}
    		for(int w=0;w<10;++w)
    			if(!use[w])
    				t=0;
    		if(t)
    			break;
    	}
    	file2<<ans<<endl;//printf("%d\n",ans);
    }
    return 0;
}

