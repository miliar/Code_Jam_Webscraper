#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<stdio.h>
using namespace std;
int  main()
{
	int a[4][4],b[4][4],n,n1,t,i,j,k,f,ans;
	FILE *stream,*stream1;
	stream=fopen("input1.txt","r");
	fscanf(stream,"%d",&t);
	stream1=fopen("output.txt","w");
	
	
	for(k=0;k<t;k++)
	{
		fscanf(stream,"%d",&n);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
			fscanf(stream,"%d",&a[i][j]);
		}
		}
		fscanf(stream,"%d",&n1);
		for(i=0;i<4;i++)
		{
			for(j=0;j<4;j++)
			{
			fscanf(stream,"%d",&b[i][j]);
		}
	}
		 if((a[n-1][0]==b[n1-1][0]||a[n-1][0]==b[n1-1][1]||a[n-1][0]==b[n1-1][2]||a[n-1][0]==b[n1-1][3])&&(a[n-1][1]==b[n1-1][1]||a[n-1][1]==b[n1-1][0]||a[n-1][1]==b[n1-1][2]||a[n-1][1]==b[n1-1][3])&&(a[n-1][2]==b[n1-1][2]||a[n-1][2]==b[n1-1][0]||a[n-1][2]==b[n1-1][1]||a[n-1][2]==b[n1-1][3])&&(a[n-1][3]==b[n1-1][3]||a[n-1][3]==b[n1-1][0]||a[n-1][3]==b[n1-1][1]||a[n-1][3]==b[n1-1][2])) 
			{
			f=5;
		}
		else if((a[n-1][0]==b[n1-1][0]||a[n-1][0]==b[n1-1][1]||a[n-1][0]==b[n1-1][2]||a[n-1][0]==b[n1-1][3])&&(a[n-1][1]==b[n1-1][1]||a[n-1][1]==b[n1-1][0]||a[n-1][1]==b[n1-1][2]||a[n-1][1]==b[n1-1][3]))
		f=5;
		else if((a[n-1][0]==b[n1-1][0]||a[n-1][0]==b[n1-1][1]||a[n-1][0]==b[n1-1][2]||a[n-1][0]==b[n1-1][3])&&(a[n-1][2]==b[n1-1][2]||a[n-1][2]==b[n1-1][0]||a[n-1][2]==b[n1-1][1]||a[n-1][2]==b[n1-1][3]))
		f=5;
		else if((a[n-1][0]==b[n1-1][0]||a[n-1][0]==b[n1-1][1]||a[n-1][0]==b[n1-1][2]||a[n-1][0]==b[n1-1][3])&&(a[n-1][3]==b[n1-1][3]||a[n-1][3]==b[n1-1][0]||a[n-1][3]==b[n1-1][1]||a[n-1][3]==b[n1-1][2])) 
		f=5;
		else if((a[n-1][1]==b[n1-1][1]||a[n-1][1]==b[n1-1][0]||a[n-1][1]==b[n1-1][2]||a[n-1][1]==b[n1-1][3])&&(a[n-1][2]==b[n1-1][2]||a[n-1][2]==b[n1-1][0]||a[n-1][2]==b[n1-1][1]||a[n-1][2]==b[n1-1][3]))
		f=5;
		else if((a[n-1][1]==b[n1-1][1]||a[n-1][1]==b[n1-1][0]||a[n-1][1]==b[n1-1][2]||a[n-1][1]==b[n1-1][3])&&(a[n-1][3]==b[n1-1][3]||a[n-1][3]==b[n1-1][0]||a[n-1][3]==b[n1-1][1]||a[n-1][3]==b[n1-1][2]))
		f=5;
		else if((a[n-1][2]==b[n1-1][2]||a[n-1][2]==b[n1-1][0]||a[n-1][2]==b[n1-1][1]||a[n-1][2]==b[n1-1][3])&&(a[n-1][3]==b[n1-1][3]||a[n-1][3]==b[n1-1][0]||a[n-1][3]==b[n1-1][1]||a[n-1][3]==b[n1-1][2]))
		f=5;		
				
				else if(a[n-1][0]==b[n1-1][0]||a[n-1][0]==b[n1-1][1]||a[n-1][0]==b[n1-1][2]||a[n-1][0]==b[n1-1][3])
				{
				ans=a[n-1][0];	
				f=1;
			}
				else if(a[n-1][1]==b[n1-1][1]||a[n-1][1]==b[n1-1][0]||a[n-1][1]==b[n1-1][2]||a[n-1][1]==b[n1-1][3])
				{
					ans=a[n-1][1];
				f=2;
			}
				else if(a[n-1][2]==b[n1-1][2]||a[n-1][2]==b[n1-1][0]||a[n-1][2]==b[n1-1][1]||a[n-1][2]==b[n1-1][3])
			{
				ans=a[n-1][2];
			
				f=3;
			}
				else if(a[n-1][3]==b[n1-1][3]||a[n-1][3]==b[n1-1][0]||a[n-1][3]==b[n1-1][1]||a[n-1][3]==b[n1-1][2])
				{
					ans=a[n-1][3];
				f=4;
			}
			
			
			
			else
			{
			
	f=6;
}
			
		
	
	switch(f)
	{
		case 1:
			fprintf(stream1,"Case #%d: %d\n",k+1,ans);
			break;
			case 2:
				fprintf(stream1,"Case #%d: %d\n",k+1,ans);
				break;
				case 3:
					fprintf(stream1,"Case #%d: %d\n",k+1,ans);
					break;
					case 4:
						fprintf(stream1,"Case #%d: %d\n",k+1,ans);
						break;
						case 5:
							fprintf(stream1,"Case #%d: Bad magician!\n",k+1);
							break;
							case 6:
								fprintf(stream1,"Case #%d: Volunteer cheated!\n",k+1);
								break;
				}

			

	
	}
	
	
	return 0;
}
