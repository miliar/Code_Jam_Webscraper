#include<cstdio>
#include<cstring>
int main()
{
	int t,a,b,c,d,e,f=0;
	char A[101];
	scanf("%d",&t);
	int p,q,r,s;
	while(t--)
	{
        scanf("%s",A);
        e=strlen(A);
        p=0;q=0
        for(b=0;b<e;b++)
        {
        	if(A[b]=='-')
        	{
        		p++;
        	}
            if(A[b]=='+')
            {
            	q++;
            }
        }
        if(q==e)
        {
          printf("Case #%d: 0\n",++f);
        }
        else if(p==e)
        {
          printf("Case #%d: 1\n",++f);	
        }
        else
        {
        	char h;
        	b=1;
        	p=1;
        	r=1;
        	while(1)
        	{
               while(A[b]==A[b-1] && b<e) 
               {
                  p++;
                  b++;
               }
               if(b==e)
               {
               	if(A[b-1]=='+')
               		break;
               }
               if(A[b-1]=='-')
               {
               	h='+';
               }
               else
               {
               	h='-';
               }
               for(q=0;q<p;q++)
               {
                 A[q]=h;
               }
               b=1;
               p=1;
               r++;
        	}
        	printf("Case #%d: %d\n",++f,r-1);
        }
	}
	return 0;
}