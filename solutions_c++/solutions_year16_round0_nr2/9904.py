#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
	int t,i=1,count=0;
	char top,cur;
	scanf("%d",&t);
	scanf("%c",&cur);
	while(t--)
	{
		
		count=0;
		scanf("%c",&cur);
		//std::cout<<cur;
		//std::cin>>cur;
		top=cur;
		while(cur!='\n')
		{
			
			if(top!=cur)
			{
				count++;
				top=cur;
			}
			scanf("%c",&cur);
			//std::cout<<cur;
		}
		if(top=='-')
		count++;
		std::cout<<"Case #"<<i<<": "<<count<<"\n";
		i++;
	}
	
	return 0;
}