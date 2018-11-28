#include<iostream>
#include<cstdio>
#include<cstring>
#include<fstream>
using namespace std;

int main()
{
	fstream file1,file2;
	file1.open("k.in",ios::in);
	file2.open("h.txt",ios::out);
    int a,b,t,ans;
    char s[110];
    file1>>a;//scanf("%d",&a);
    for(b=1;b<=a;++b)
    {
    	file1>>s;//scanf("%s",s);
    	file2<<"Case #"<<b<<": ";//printf("Case #%d: ",b);
    	ans=0;
    	t=strlen(s)-1;
    	while(1)
    	{
    		while(s[t]=='+')
    			t--;
    		if(t<0)
    			break;
    		if(s[0]=='+')
    		{
    			ans++;
    			for(int q=0;s[q]=='+';++q)
    				s[q]='-';
    		}
    		ans++;
    		for(int q=0;q<=t;++q)
    		{
    			if(s[q]=='+')
    				s[q]='-';
    			else
    				s[q]='+';
    		}
    	}
    	file2<<ans<<endl;//printf("%d\n",ans);
    }
    return 0;
}

