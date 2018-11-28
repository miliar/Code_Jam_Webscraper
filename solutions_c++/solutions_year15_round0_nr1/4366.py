#include<iostream>
#include<stdio.h>
#include<cstring>
#include<stdlib.h>
#include <queue>
#include<string>
#include <sstream>
#include<list>
#include<map>
#include<cmath>
#include<algorithm>

using namespace std;

int main()
{
	int flag = 0,n,i=0,j,index = 0,x,y,m,input,sum,ans;

	
	freopen ("d:/Codejam/A-large.in","r",stdin);
	freopen ("d:/Codejam/A-large.out","w",stdout);
	scanf("%d",&input);
	 string A;
	int smax;
	while(input--)
	{
		A="";
		scanf("%d",&smax);
		
		cin>>A;//string
		sum=0;
		ans=0;
		for(i=0;i<=smax;i++){
			x = A[i]-'0';
			if(x!=0){
				if(sum>=i)
					sum = sum + x;
				else{
					y=i-sum;
					ans = ans+y;
					sum = sum+y+x;
				}
			}
		}

		printf("Case #%d: ",++index);		

		cout<<ans<<"\n";
	}
	return 0;
}

