#include<iostream>
int main()
{
    int a[4][4],b[4][4],T;
    int result[4];
    
    std::cin>>T;
    for(int i=0;i<T;++i)
    {
	for(int j=0;j<4;++j)
	    result[j]=0;
	int x;
	std::cin>>x;
	for(int j=0;j<4;++j)
	    for(int k=0;k<4;++k)
		std::cin>>a[j][k];
	int y;
	std::cin>>y;
	for(int j=0;j<4;++j)
	    for(int k=0;k<4;++k)
		std::cin>>b[j][k];
	
	for(int j=0;j<4;++j)
	{
	    for(int k=0;k<4;++k)
	    {
		if(a[x-1][j]==b[y-1][k])
		{
		    result[j]++;
		    break;
		}
	    }
	}
	
	int c=0,id;
	for(int j=0;j<4;++j)
	    if(result[j]>0)
	    {
		c++;
		id=j;
	    }
	std::cout<<"Case #"<<i+1<<": ";
	if(c==1)
	    std::cout<<a[x-1][id]<<'\n';
	if(c==0)
	    std::cout<<"Volunteer Cheated!"<<'\n';
	if(c>1)
	    std::cout<<"Bad Magician!"<<'\n';
    }
}