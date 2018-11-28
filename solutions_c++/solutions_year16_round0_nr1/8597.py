#include <iostream>
#include <cstring>
#define For(i,a,b) for(int i=a;i<=b;i++)
using namespace std;
int f[11],test,n;
void process(int x)
{
	while (x)
	{
		f[x%10] = 1;
		x/=10;
	}
}
bool check()
{
	For(i,0,9) if (!f[i]) return 0;
	return 1;
}
int main() {
	// your code goes here
	scanf("%d",&test);
	For(Test,1,test)
	{
		memset(f,0,sizeof(f));
		printf("Case #%d: ",Test);
		scanf("%d", &n);
		if (n==0) puts("INSOMNIA");
		else 
		{
			For(i,1,1000)
			{
				process(i*n);
				if (check())
				{
					cout<<n*i<<endl;
					break;
				}
			}
		}
	}
	return 0;
}