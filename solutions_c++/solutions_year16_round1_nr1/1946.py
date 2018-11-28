#include<iostream>
#include<cstdio>
#include<fstream>
using namespace std;

int main()
{
	fstream file1,file2;
	file1.open("kl.in",ios::in);
	file2.open("b.txt",ios::out);
    int a,x,y;
    char s[1100],ans[3000];
    file1>>a;//scanf("%d",&a);
    for(int b=1;b<=a;++b)
    {
    	file1>>s;//scanf("%s",s);
    	file2<<"Case #"<<b<<": ";//printf("Case #%d: ",b);
    	x=y=1500;
    	y++;
    	ans[x]=s[0];
    	for(int q=1;s[q];++q)
    	{
    		if(s[q]>=ans[x])
    			ans[--x]=s[q];
    		else
    			ans[y++]=s[q];
    	}
    	for(int q=x;q<y;++q)
    		file2<<ans[q];//printf("%c",ans[q]);
    	file2<<endl;//printf("\n");
    }
    return 0;
}

