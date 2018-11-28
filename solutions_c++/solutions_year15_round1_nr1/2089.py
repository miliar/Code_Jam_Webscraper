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
int half1,half2;
void divide(int maximum){
	{
		if(maximum%2 == 0){
			half1= maximum/2;half2 = half1;
		}
		else{
			half1= maximum/2;half2 = half1+1;
		}
	}

}
int main()
{
	int	flag = 0,n,i=0,j,index = 0,x,y,m,input,ans;

	freopen ("d:/Codejam/A-large(1).in","r",stdin);
	freopen ("d:/Codejam/A-large(1).out","w",stdout);
	scanf("%d",&input);
	string Ans;
	
	long long A[1005];
	while(input--)
	{
		scanf("%d",&n);
		long long sum=0,max=-1,X,result=0;

		for(i=0;i<n;i++)
		{
			cin>>A[i];
		}
		
		for(i=0;i<n-1;i++){
			if(A[i+1]<A[i]){
				X= A[i]-A[i+1];
			sum += X;
			if(X>max)
				max=X;
			}
		}
		if(max>-1)
		for(i=0;i<n-1;i++){
			if(A[i+1]<=A[i]){
				//X= A[i]-A[i+1];
				if(A[i]<=max)
					result+=A[i];
				else
					result+=max;
			}
			else{
				if(A[i]<=max)
					result+=A[i];
				else
					result+=max;
			
			}
		}
		
		
		printf("Case #%d: ",++index);

		cout<<sum<<" "<<result<<"\n";
	}
	return 0;
}
