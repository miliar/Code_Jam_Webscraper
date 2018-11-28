#include <iostream>
#include <string>
#include <algorithm>

int main()
{
	std::string str="a";
    int t=0,left=0,right=0,a0=0,k=0;
    bool flag=true;
    char temp='a';
    std::cin>>t;
    for(int i=1;i<=t;++i)
    {
    	std::cin>>str;
    	a0=str.length();
    	char * a=new char [(2*a0)+2];
    	for(int j=0;j<(2*a0)+2;++j)
        {
        	a[j]='0';
        }
    	a[((2*a0)+2)/2]=str[0];
    	left=((2*a0)+2)/2;
    	right=((2*a0)+2)/2;
    	for(int j=1;j<a0;++j)
    	{
    		if(str[j]>=a[left])
    		{
    			a[left-1]=str[j];
    			--left;
    		}
    		else
    		{
    			a[right+1]=str[j];
    			++right;
    		}
    	}
    	std::cout<<"Case #"<<i<<":  ";
    	for(int j=left;j<=right;++j)
    	{
    		std::cout<<a[j];
    	}
    	std::cout<<"\n";
    }
    return 0;
}