#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<vector>
using namespace std;

int main()
{
	
 	freopen("C-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int arr[]={0, 1, 4, 9, 121, 484};
	int len = 6;
	int T,A,B,*ptr,start,end;
	scanf("%d",&T);
	for(int t=0;t<T;t++)
	{	
		scanf("%d%d",&A,&B);
		ptr = lower_bound(arr,arr+len,A);
		start = ptr-arr;
//		cout<<start<<endl;
		if(start == len){
			printf("Case #%d: 0\n",t+1);
			continue;
		}

		ptr  = lower_bound(arr,arr+len,B);
		if(ptr-arr == len  || *ptr != B)	ptr--;
		end = ptr-arr;
//		cout<<end<<endl;

		printf("Case #%d: %d\n",t+1,end-start+1);
	}
}
