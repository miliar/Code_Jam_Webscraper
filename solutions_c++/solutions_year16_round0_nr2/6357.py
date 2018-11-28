#include <stdio.h>
#include <string.h>

#define change(a) ((a=='+')?'-':'+')

void reversePancake(char arr[],int from, int to)
{
	for (int i = from,j=to; i<j; i++,j--)
		{
			char tmp=arr[i];
		
			arr[i] = arr[j];
			arr[j]=tmp;
		}
}

void flip( char arr[], int from, int to, char value)
{
	//printf("here :from = %d, to = %d, value = %c\n",from,to,value);
	int i=from;
	int j=to;
	for (i = from,j=to; i<j; i++,j--)
	{
			arr[i] = value;
			arr[j] = value;
		
			char tmp=arr[i];
		
			arr[i] = arr[j];
			arr[j]=tmp;
	}
	
	if( arr[i]!=value)
		arr[i]=value;
		

}


int main()
{
	int t=0;
	scanf("%d ",&t);
	for(int i=1;i<=t;i++)
	{
		long int answer=0;
		char s [110]={0};
		int top=-1;
		
		fgets(s,110,stdin);
		s[strlen(s)-1]='\0';
		top = strlen(s) -1;
		
		//printf("Pancake: [%s], top=%d\n",s,top);
		reversePancake(s,0,top);
		//printf("Pancake: [%s], top=%d\n",s,top);
		
		
		//Calculate minimum flip
		bool flag = false;
		int ctr=0;
		while(!flag)
		{
			int startP = -1;
			int startN = -1;
			bool topP = false;
			bool topN = false;
			
						
			if (s[top]=='+')
			{
				int nIndex = top;
				topP=true;
				
				while( s[nIndex] == '+' && nIndex >=0)
				{
					nIndex--;
				}
				
				
				//printf("Top is positive:: Negative Index from top = %d\n",nIndex);
				if(nIndex == -1)
				{
				flag=true;
				break;
				}	
				
				{
					flip(s,nIndex+1,top,'-');
					++answer;
					//printf("FLIPPancake: [%s]\n",s);
				}
			
				
			}
			else if (s[top]=='-')
			{
				topN=true;
				int pIndex = top;
				topP=true;
				while( s[pIndex] == '-' && pIndex >=0)
				{
					pIndex--;
				}
				//printf("Top is negative:: Positive Index from top = %d\n",pIndex);
				
				{
					flip(s,pIndex+1,top,'+');
					++answer;
					//printf("FLIPPancake: [%s]\n",s);
				}
			
			}
			/*if( s[0]=='+' && s[top]=='+')
			{
				flag=true;
				break;
			}*/	
			
			
			
			
		}	
		
		
		printf("Case #%d: %ld\n",i,answer);
				
	
	}
	return 0;
}
