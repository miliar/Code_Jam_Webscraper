#include<iostream>
int main()
{
    int t,a,b,k,j,l,count=0;
    std::cin>>t;
    for(int i=0;i<t;++i)
    {
	std::cin>>a>>b>>k;
	count=0;
	for(j=0;j<a;++j)
	{
	    for(l=0;l<b;++l)
	    {
		//std::cout<<(j&l)<<j<<l;
		if((j&l)<k)
		{
		    
		    count++;
		}
	    }
	}
	std::cout<<"Case #"<<i+1<<": "<<count<<'\n';
    }
}