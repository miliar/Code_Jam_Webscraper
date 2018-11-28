#include<stdio.h>
#include<iostream>
using namespace std;
typedef struct mapping
{
	char symbol1;
	char symbol2;
}m;
m a[8];
int main()
{
	int mul[8][8]={{3,2,6,7,0,1,5,4},{5,3,0,6,1,7,4,2},{1,7,3,5,2,4,0,6},{7,6,5,4,3,2,1,0},{0,1,2,3,4,5,6,7},{6,0,4,2,5,3,7,1},{2,4,7,1,6,0,3,5},{4,5,1,0,7,6,2,3}};
	a[0].symbol1='-';
	a[0].symbol2='k';
	a[1].symbol1='-';
	a[1].symbol2='j';
	a[2].symbol1='-';
	a[2].symbol2='i';
	a[3].symbol1='-';
	a[3].symbol2='1';
	a[4].symbol1='+';
	a[4].symbol2='1';
	a[5].symbol1='+';
	a[5].symbol2='i';
	a[6].symbol1='+';
	a[6].symbol2='j';
	a[7].symbol1='+';
	a[7].symbol2='k';
	int t;
	scanf("%d",&t);
	getchar();
	for(int z=1;z<=t;z++)
	{
		int n,m;
		scanf("%d",&n);
		getchar();
		scanf("%d",&m);
		getchar();
		int x[n*m];
		int r=0;
		while(n--)
		{
			switch(getchar())
			{
				case '1':
					x[r++]=4;
					break;
				case 'i':
					x[r++]=5;
					break;
                                case 'j':
                                        x[r++]=6;
                                        break;
                                case 'k':
                                        x[r++]=7;
                                        break;
				case '-':
					switch(getchar())
					{
	                                	case '1':
                                        		x[r++]=3;
                                        		break;
                                		case 'i':
                                        		x[r++]=2;
                                        		break;
                                		case 'j':
                                        		x[r++]=1;
                                        		break;
                                		case 'k':
                                 	       		x[r++]=0;
                                        		break;
					}
			}
		}
		getchar();
		for(int d=0;d<r;d++)
		{
			for(int y=1;y<m;y++)
			{
				x[d+r*y]=x[d];
			}
		}
		int ipresent=0,iat=-1,kpresent=0,kat=-1;
		int h,b;
		h=x[0];
		if(h==5)
		{
			ipresent=1;
			iat=0;
		}
		for(int w=1;w<r*m;w++)
		{
			b=x[w];
			h=mul[h][b];
			if(h==5)
			{
				ipresent=1;
				if(iat==-1)
				{
					iat=w;
				}
			}
		}
		if(h!=3)
		{
			printf("Case #%d: NO\n",z);
			continue;
		}
		h=x[r*m-1];
		if(h==7)
		{
			kpresent=1;
			kat=r*m-1;
		}
		for(int w=r*m-2;w>=0&&kpresent==0;w--)
		{
			b=x[w];
			h=mul[h][b];
			if(h==0)
			{
				kpresent=1;
				kat=w;
			}
		}
		/*int flag=0;
		for(int u=0;u<r*m;u++)
		{
			if(i[u]==1)
			{
	//			printf("i->%d\n",u);
				for(int e=r*m-1;e>u;e--)
				{	
					if(k[e]==1)
					{
	//					printf("k->%d\n",e);
						int a=x[u+1];
						int h;
						for(int w=u+2;w<e;w++)
                				{
                			        	h=x[w];
	//			                        printf("multiplying %d %d ",a,h);
                			        	a=mul[a][h];
        //              				printf("h->%d\n",a);
            			                }
	//					printf("mul->%d\n",a);
						if(a==6)
						{
							printf("Case #%d: YES\n",z);
							flag=1;
							break;
						}
        			        }
				}
			}
			if(flag==1)
				break;
		}
		if(flag==0)
		{
			printf("Case #%d: NO\n",z);
		}*/
		if(ipresent==1 && kpresent==1 && iat<kat)
		{
			printf("Case #%d: YES\n",z);
		}
		else
		{
			printf("Case #%d: NO\n",z);
		}
	}
	return 0;
}
