#include<iostream>
#include<cmath>
#include<cstdio>
#include<vector>

//Under Construction
using namespace std;
int main(){
	#ifndef ONLINE_JUDGE
	freopen("large.in","r",stdin);
	#endif
	freopen("output.txt","w",stdout);
	
	int i, j, n = 0, cases, pep, shy, stand=0;
	char pepc;
	scanf("%d", &cases);
	
	for(i=0;i<cases;i++)
	{
		scanf("%d", &shy);
		n = stand = 0;
		scanf("%c", &pepc);
		
		for(j=0;j<=shy;j++)
		{
			scanf("%c", &pepc);
			pep = pepc - '0';
//			cout<<pep<<" ";
			
//			cout<<pep<<stand<<j<<" ";
			if(j==0 && pep > 0)
			{
				stand = pep;
//				cout<<"First ";
//				cout<<pep<<stand<<j<<" ";

				continue;
			}	
			if(stand >= j)
			{
				stand += pep;
//				cout<<" S |";
			}
			else
			{
				n += abs(stand - j);
				stand += pep + abs(stand - j);
//				cout<<" P |";
			}	
			
		}
//		cout<<stand<<" ";
	
	printf("Case #%d: %d\n", i+1, n);	
	}	

return 0;
}

