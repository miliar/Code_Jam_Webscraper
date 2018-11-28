#include<cstdio>
#include<iostream>
#include<string>
using namespace std;
int main(void)
{
    int cases;
    int count;
    string str;
    scanf("%d",&cases);
    getline(cin,str);
    for(int i=1;i<=cases;i++)
    {
        getline(cin,str);
	count=0;
        for(int j=str.size()-1;j>=0;j--)
	    if( (str[j]=='-' && count%2==0))
	    {
		count++;
	    }
	    else if(str[j]=='+' && count%2==1)
	    {    
		count++;
	    }
	printf("Case #%d: %d\n",i,count);
    }
    return 0;
}
