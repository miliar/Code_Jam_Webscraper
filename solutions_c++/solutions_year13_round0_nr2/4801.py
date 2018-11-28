#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int rslt=-1;
struct wrd
{
	char c[5];
	//int nc;
	
};
struct line
{
	wrd w[200];
	//int nw;
	
};

struct page
{
	line l[1000];

	//int nl;
	
};

FILE* f, *fw;
void read(int nol,page* pg)
{
	//printf("\n");
	int x,n=0,i=0,j=0,k=0;
	 while  (  i<nol )
            if(( x = fgetc( f ) ) != EOF){
				//printf("%c",x);
				n++;
				if(x==10)
				{
					
					pg->l[i].w[j].c[k]=NULL;
					
					i++;
		

					j=0;k=0;
				}
				else if(x==32)
				{
					
					pg->l[i].w[j].c[k]=NULL;
					//printf("val=%d ,(%d,%d) ",atoi(pg->l[i].w[j].c),i,j);
					
					j++;k=0;
				
		
				}
				else
				{
				
					
					pg->l[i].w[j].c[k]=x;
//		
					k++;
				}
				
            }
	
}

void cnst()
{
		
f=fopen("B-large.in","r");
fw=fopen("B-large.out","w");
if(fw==NULL) printf("could not open");
if(f==NULL) printf("unable to open file");

}

void dest()
{
			fclose( f);/**/
			fclose(fw);

}
/**/
int main()
{
	page pg;
	int x,n=0,i=0,j=0,k=0;

	cnst();
	

			
			//printf("%s",c);
			//printf("%d\n\n-----\n",atoi(pg.l[0].w[0].c));
			int t;		
			
			read(1,&pg);
			t=atoi(pg.l[0].w[0].c);
			
			int N=0,M=0,tcnt=0;
			int rmax[105],cmax[105];
			for (tcnt=0;tcnt<t;tcnt++)
			{
				read(1,&pg);
				N=atoi(pg.l[0].w[0].c);
				M=atoi(pg.l[0].w[1].c);
				rslt=1;

				read(N,&pg);

			for(i=0;i<100;i++)
			{
				rmax[i]=-1;
				cmax[i]=-1;
			}

				for(i=0;i<N;i++)
					for(j=0;j<M;j++)
					{
						rmax[i]=(rmax[i]>atoi(pg.l[i].w[j].c)?rmax[i]:atoi(pg.l[i].w[j].c));
						cmax[j]=(cmax[j]>atoi(pg.l[i].w[j].c)?cmax[j]:atoi(pg.l[i].w[j].c));
		//				if(rmax[i]>2) printf("--%d,%d\n",i,j);			
						
					}
//					printf("case#%d: %d  %d,%d\n",tcnt+1,atoi(pg.l[i].w[j].c),rmax[1],cmax[0]);
					for(i=0;i<N;i++)
					{
						
						for(j=0;j<M;j++)
						{
							//printf("%d ",atoi(pg.l[csp+i].w[j].c));

							
						if(!(atoi(pg.l[i].w[j].c)==rmax[i]||atoi(pg.l[i].w[j].c)==cmax[j])) 
						{
							rslt=0;		
	//						printf("(%d,%d),%d!=%d,%d\n",i,j,atoi(pg.l[i].w[j].c),rmax[i],cmax[j]);

						}


						}

					}
			

			if(rslt==0)
			{
				fprintf(fw,"Case #%d: NO\n",tcnt+1);
			}
			else
			{
				fprintf(fw,"Case #%d: YES\n",tcnt+1);
			}
			//printf("rslt=%d\n",rslt);
			}
			
			dest();
			//printf("\nlines=%d\n",pg.nl);
			//scanf("%d",&x);
}