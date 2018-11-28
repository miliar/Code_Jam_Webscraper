#include<iostream>
#include<map>
#include<set>
#include<stdio.h>
using namespace std;
int main() 
{
	freopen("A-large.in","r",stdin);  
	freopen("A-large.out","w",stdout); 
	int T;
	scanf("%d",&T);
	int n;
	int row=1;
	while(T--)
	{
		set<int> a;
		scanf("%d",&n);
		if(n==0)
		{
			printf("Case #%d: INSOMNIA\n",row++);
			//cout<<"Case #"<<row++<<": INSOMNIA"<<endl;
			continue;	
		}
		int i=1;
		int tem;
		int res;
		do
		{
			tem=n*(i++);
			res=tem;
			while(tem!=0)
			{
				a.insert(tem%10);
				tem=tem/10;
			}
		}while(a.size()!=10);
		printf("Case #%d: %d\n",row++,res);
		//cout<<"Case #"<<row++<<": "<<res<<endl;
			
	}
	return 0;
}
	

