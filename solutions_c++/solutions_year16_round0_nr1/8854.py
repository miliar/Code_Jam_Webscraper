#include <stdio.h>
#include <string.h>
using namespace std;
class my_numbers {
	private:
		int N;
		int current;
		short A[10];
	public:
		my_numbers(int n)
		{
			current=n;
			N=n;
			for(int i=0;i<10;i++)
				A[i]=0;
			while(n)
			{
				A[n%10]=1;
				n/=10;
			}
		}
		bool next()
		{
			current+=N;
			int tmp=current;
			bool change = false;
			while(tmp)
			{
				if(A[tmp%10]==0)
					change=true;
				A[tmp%10]=1;
				tmp/=10;

			}
			int i=0;
			if(change)
			{while(i<10)
					if(A[i++]!=1)
						return false;
			return true;}
			else
				return false;
		}
		int getN()
		{
			return current;
		}

};
int main()
{
	int n;
	scanf("%d",&n);
	for(int i=1;i<=n;i++)
	{
		int number;
		scanf("%d",&number);
		printf("Case #%d: ",i);
		if(number ==0)
			printf("INSOMNIA\n");
		else
		{
			my_numbers tmp(number);
			while(!tmp.next());
			printf("%d\n",tmp.getN());
		}
	}
	return 0;
}
