#include<iostream>

using namespace std;

int main()
{
	int i=1,j,test,len,com,size,answer;
	cin>>test;
	while(test >= i)
	{
		cin>>len;
		cin>>com;
		cin>>size;
		cout<<"Case #"<<i<<":";
		if(com==1 || len==1)
			answer=len;
		else
			answer=len-1;
		if(answer<=size)
		{
				for(j=len;answer>0;--j,--answer)
					cout<<" "<<j;
		}
		else
			cout<<" IMPOSSIBLE";
		cout<<endl;
		++i;
	}
	return 0;
}