#include <iostream>
#include<set>
using namespace std;

int main() {
	int t;
	long long int ca=0,n,a,a_new,k,f,i;
	cin>>t;
	while(t--)
	{
		ca=ca+1;
		set <int > S;
		S.clear();
		scanf("%lld",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",ca);
			continue;
		}
		for(i=1;;i++)
		{
			a_new=i*n;
			a=a_new;
			f=0;
			while(a!=0)
			{
				k=a%10;
				S.insert(k);
				if(S.size()==10)
				{
					f++;
					printf("Case #%d: ",ca);
					cout<<a_new<<endl;
					break;
				}
				a=a/10;
			}
			//cout<<S.size(); 
			if(f>0)
			{
				break;
			}
		}
	}
	return 0;
}