#include<cstdio>
#include<iostream>
using namespace std;

int main()
{
	int t;
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("k.txt", "w", stdout);
	scanf("%d\n",&t);
//	printf("\n scanning ::  %d",t);
	for(int tc = 1; tc <= t; tc++){
		printf("Case #%d: ", tc);
		int a,b,temp,res=0,ans;
		scanf("%d", &a);
	    int aa[4],bb[4];
        for(int i=0; i<4;i++)
        {   for(int j=0; j<4;j++)
            {
                if(i==a-1)
                scanf("%d", &aa[j]);
                else
                scanf("%d", &temp);
                }
        } 
        scanf("%d", &b);
        for(int i=0; i<4;i++)
        {   for(int j=0; j<4;j++)
            {
                if(i==b-1)
                {scanf("%d", &bb[j]);
                  for(int k=0;k<4;k++)
                    if(bb[j]==aa[k])
                     {  if(res) res++; else { res=1; ans=aa[k];} }
                }
                else
                scanf("%d", &temp);
                }
        } 
        if(res==0)
        printf("Volunteer cheated!\n");
        else if(res==1)
        printf("%d\n",ans);
        else
        printf("Bad magician!\n");
}
                                
             
	
	return 0;
}
			
