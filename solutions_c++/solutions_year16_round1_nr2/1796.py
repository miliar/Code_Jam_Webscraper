#include<bits/stdc++.h>
using namespace std;

set<int>coll;
//int store[15][15];
int hashi[2600];

int main()
{
	
//		freopen("B-large.in", "r" , stdin);
//freopen ("output.out","w",stdout);

	int j,T,i,N,k,num;
	scanf("%d",&T);
	
//		int arr[] = {1, 2, 3, 4, 5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20};
	
	set<int>::iterator it;
	for(i=1;i<=T;i++)
	{
		scanf("%d",&N);
		
		
		for(j=0;j<=2505;j++)
			hashi[j]=0;
		
		
		for(j=1;j<=2*N-1;j++)
			{
				for(k=1;k<=N;k++)
					{
					//	scanf("%d",&store[j][k]);
						scanf("%d",&num);
						hashi[num]++;
							
					}
			}
		
		for(j=1;j<=2500;j++)
			if(hashi[j]>0&&hashi[j]%2!=0)
				coll.insert(j);
		
		
			printf("Case #%d: ",i);
		for(it=coll.begin();it!=coll.end();++it)
			printf("%d ",*it);
		
			
		printf("\n");
		//1
  /* 		 int r = N;
   		 int n = 2*N-1;	//sizeof(arr)/sizeof(arr[0]);
   		 printCombination(arr, n, r);
		
	*/	
		
		
		
		coll.clear();
	}
	
//	fclose(stdout);
	return(0);
}


