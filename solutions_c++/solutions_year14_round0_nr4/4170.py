#include<stdio.h>
int main()
{
	int T,b,z=0,i,j,n,v=0,k=0,l,p=0,u=0,q=0,r,x=0,X;
	float N[10000],K[10000],c,d,m[10000],h[10000],S[10000],I[10000],L[10000],P[10000],R[10000],U[10000],A[10000];
	freopen("D-large.in","rt",stdin);
	freopen("D-large.out","wt",stdout);
	scanf("%d",&T);
	for(b=0;b<T;b++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%f",&N[i]);
			L[i]=N[i];
		}
		
		for(i=0;i<n;i++)
		{
			scanf("%f",&K[i]);
			P[i]=K[i];
		}
		//war starts
		r=n;
		for(i=0;i<n;i++)
		{
			for(j=0;j<n;j++)
			{  // printf("hiii1\n");
				if(N[i]<K[j])
				{
					//printf("hiii2\n");
					v++;
					m[k]=K[j];                             //checking how much block masses are greater than naomi's mases
					k++;
				}	
			}
		//	printf("%d\n",v);
		//	for(k=0;k<v;k++)
		//	printf("%f ",m[k]);
		//	printf("/**********************/\n");
			//printf("value of m[0] is %f\n",m[0]);
			for(k=0;k<v;k++)
			{
				//printf("hiii3\n");
			   	j=0;
				d=m[0];
				c=m[k];                                   //sorting of m[k]
				m[0]=c;
				m[k]=d;
				for(l=0;l<v-1;l++)
				{
				if(m[0]>m[l+1])
			    j++;
				}
				//printf("value of j is %d\n",j);
				h[j]=m[0];
			}
		//	for(k=0;k<v;k++)
		//	printf("%f ",h[k]);
		//	printf("/**********************/\n");

            for(k=0;k<n;k++)
            {
            	S[k]=K[k];
          //      printf("%f ",S[k]);
            }
		//	printf("/**********************/\n");
			for(k=0;k<n;k++)
			{
				//printf("hiii3\n");
			   	j=0;
				d=S[0];
				c=S[k];                                   //sorting of m[k]
				S[0]=c;
				S[k]=d;
				for(l=0;l<n-1;l++)
				{
				if(S[0]>S[l+1])
			    j++;
				}
		//		printf("value of j is %d\n",j);
				I[j]=S[0];
			}
		//	for(k=0;k<n;k++)
		//	printf("%f ",I[k]);
		//	printf("/**********************/\n");
			//printf("value of h[0] is %f\n",h[0]);
			while(p!=1&& v>0)
			{
				//printf("hiii4\n");
				if(K[u]==h[0])
				{
					for(j=u;j<n-1;j++)
					{
						K[j]=K[j+1];
					}
					K[n]='\0';
					p=1;
				}
				u++;
			}
			while(p!=1&& v==0)
			{
				//printf("hiii4\n");
				if(K[u]==I[0])
				{
					for(j=u;j<n-1;j++)
					{
						K[j]=K[j+1];
					}
					K[n]='\0';
					p=1;
				}
				u++;
			}
			u=i;
			while(q!=1 )
			{    if(q==0)
			     {
				    // printf("hiii4.1\n");
					for(j=u;j<n;j++)
					{
						N[j]=N[j+1];
					}
					N[n]='\0';
					q=1;
				 }
			}
	        //for(k=0;k<n;k++)
	        //printf("%f",N[k]);
			if(v>0)
			{
				z++;
			}
			n=n-1;
				v=0;k=0;p=0;u=0;q=0;i=-1;
		}
		//Deceitful War
		n=r;
		for(k=0;k<n;k++)
			{
				//printf("hiii3\n");
			   	j=0;
				d=L[0];
				c=L[k];                                   //sorting of m[k]
				L[0]=c;
				L[k]=d;
				for(l=0;l<n-1;l++)
				{
				   if(L[0]>L[l+1])
			       j++;
				}
		//		printf("value of j is %d\n",j);
				R[j]=L[0];
			}
			for(k=0;k<n;k++)
			{
				//printf("hiii3\n");
			   	j=0;
				d=P[0];
				c=P[k];                                   //sorting of m[k]
				P[0]=c;
				P[k]=d;
				for(l=0;l<n-1;l++)
				{
				if(P[0]>P[l+1])
			    j++;
				}
		//		printf("value of j is %d\n",j);
				U[j]=P[0];
			}
			for(i=0;i<r;i++)
			{
				if(R[0]<U[0])
				{
					for(j=0;j<n-1;j++)
					{
						R[j]=R[j+1];
					}
					R[n]='\0';
					U[n]='\0';
				}
				else
				{
					for(j=0;j<n-1;j++)
					{
						R[j]=R[j+1];
					}
					R[n]='\0';
					for(j=0;j<n-1;j++)
					{
						U[j]=U[j+1];
					}
					U[n]='\0';
					x++;
				}
			}
			    printf("Case #%d: %d %d\n",b+1,x,r-z);
		    z=0;v=0;k=0;p=0;u=0;q=0;x=0;
	}
}
