/*krypto.............................jagsxi...!! */
#include<bits/stdc++.h>
using namespace std;
int fastread(long long int* a) 
{ char c=0; 
while (c<33) 
c=getchar_unlocked(); 
*a=0; 
while (c>33) { 
*a=*a*10+c-'0'; 
c=getchar_unlocked(); 
} 
return 0; }

int main()
{
long long int cases;
fastread(&cases);
	for(int c1=1;c1<=cases;c1++){
	long long int a,b,k,ret=0;
fastread(&a);
fastread(&b);
fastread(&k);
	for(int i=0;i<a;i++)
		for(int j=0;j<b;j++)
			if((i&j)<k)
				ret++;
	printf("Case #%d: %d\n",c1,ret);
	}
}
