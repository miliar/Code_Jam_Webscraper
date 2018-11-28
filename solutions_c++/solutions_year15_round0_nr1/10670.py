#include <iostream>
using namespace std;

int main() {
	// your code goes here
int i,n,nop,req,z,p=0;
char a[1001];

scanf("%d",&z);

while(z--)
{
p++;
scanf("%d %s",&n,a);

for(i=0;i<=n;i++)
a[i]=a[i]-48;

nop=a[0];
req=0;

for(i=1;i<=n;i++)
{
	
	if(a[i]!=0)
	{
		if(i<=nop)
		{
        nop=nop+a[i];
		}
		
		else
		{
			req=req+(i-nop);
			nop=i+a[i];
		}
		
	}


}

printf("Case #%d: %d\n",p,req);

}

	return 0;
}
