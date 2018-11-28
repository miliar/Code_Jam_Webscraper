#include <iostream>
#include <cstdio>
#include <map>
using namespace std ;
int M[5][5] ;
int ans[5] ;
int main()
{
	freopen("D:\\A-small-attempt0.in","r",stdin) ;
	freopen("D:\\A-small-attempt0.out","w",stdout) ;
	int t,cas=1 ;
	scanf("%d",&t) ;
	while(t--)
	{
		int row1,row2 ;
		scanf("%d",&row1) ;
		for(int i=0 ;i<4 ;i++)
			for(int j=0 ;j<4 ;j++)
				scanf("%d",&M[i][j]) ;
		map <int,int> q ;
		for(int i=0 ;i<4 ;i++)
			q[M[row1-1][i]]=1 ;
		scanf("%d",&row2) ;
		for(int i=0 ;i<4 ;i++)
			for(int j=0 ;j<4 ;j++)
				scanf("%d",&M[i][j]) ;
		int cnt=0,ans ;
		for(int i=0 ;i<4 ;i++)
		{
			if(q[M[row2-1][i]]){ans=M[row2-1][i] ;cnt++ ;} 
		}
		printf("Case #%d: ",cas++) ;
		if(cnt>=2)
			puts("Bad magician!") ;
		else if(!cnt)
			puts("Volunteer cheated!") ;
		else 
			printf("%d\n",ans) ;
	}
	return 0 ;
} 