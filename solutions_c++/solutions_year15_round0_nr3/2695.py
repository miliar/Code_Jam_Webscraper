#include<stdio.h>
int main()
{
	int t;
	scanf("%d",&t);
        int q=t;
	while(t>0)
	{
		int n,r;
		scanf("%d %d",&n,&r);
		getchar();
 		char s[100000];
                scanf("%s",s);           
 		int a[5][5];
                a[1][1]=1;a[1][2]=2;
                a[1][3]=3;a[1][4]=4;
                a[2][1]=2;
		a[2][2]=-1;
		a[2][3]=4;
		a[2][4]=-3;
                a[3][1]=3;
		a[3][2]=-4;
		a[3][3]=-1;
		a[3][4]=2;
                 a[4][1]=4;
		a[4][2]=3;
		a[4][3]=-2;
		a[4][4]=-1;
		/*  for(int i=2;i<=4;i++)
		    {
		    for(int j=2;j<=4;j++)
		    printf("%d ",a[i][j]);
		    printf("\n");
		    }*/
                int p,c=0,o=0,l=1;
               for(int j=1;j<=r;j++)
              {
		for(int i=0;i<n;i++)
		{
			int k;
			if(s[i]=='i')
				k=2;
			else if(s[i]=='j')
				k=3;
			else if(s[i]=='k')
				k=4;
			else
				k=9;

			p=k;
//			printf("p%d\n",p);
		//	if( j!=0)
                        {
//                              printf("p%d l%d\n",p,l);
				p=a[l][p];
 
                        }
//                        printf("%d\n",p);
			if(p<0)
			{
    //                        printf("sadfs\n");
				c++;
				p*=-1;
                        }
			if(p==2 && ((c%2)==0) && o==0)
                            {
  //                             printf("i done\n");
                               p=1;
                               o=2;
                               c=0;
                           }
                       else if(p==3 && o==2 && ((c%2)==0))
                          {
    //                           printf("j done\n");
                               p=1;
                               o=3;
                               c=0;
                          }
                      else if(p==4 && o==3 && ((c%2)==0))
                          {
      //                          printf("k done\n");
                             p=1;
                             o=4;
                             c=0;
                          }
                     else if(o==4 && ((c%2)==0) && p==1)
                        {
                            c=0;
                            o=5;
                        }			
			l=p;
		}
              }
      //        printf("c%d\n",c);
                for(int i=0;i<c;i++)
                  p*=-1;
  //             printf("%d\n",p);
          t--;
               if((o==4 && p==1) || (o==5 && p==1))
                  printf("Case #%d: YES\n",q-t);
               else
                  printf("Case #%d: NO\n",q-t);
               // for(int i=0;i<r;i++)
                  
	//	printf("%d\n",p);
	//	t--;
	}
	return 0;
}
