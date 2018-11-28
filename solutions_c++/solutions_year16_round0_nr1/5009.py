#include<iostream>

#define lim 800

FILE *inp, *out;

bool seen[10];

bool ok()
{
	int i;
	//printf("..seen:\n");	
	for(i=0;i<10;++i)
	{
		//printf("..seen[%d]=",i);
		//printf(seen[i]?"true\n":"false\n");
		if(!seen[i])			
		return false;
	}
	return true;
}

int main(){
	int i,j,T,N,temp;
	inp = fopen("inp.in","r");
	out = fopen("out.txt","w");
	fscanf(inp,"%d",&T);
	for(i=1;i<=T;++i)
	{
		fscanf(inp,"%d",&N);
		if(N==0)
		{	
			//printf("Case #%d: INSOMNIA\n",i);
			fprintf(out,"Case #%d: INSOMNIA\n",i);			
		}
		else
		{		
			for(j=0;j<10;++j)
			seen[j]=false;
			for(j=1;true;++j)
			{
				temp=N*j;
				while(temp>0)
				{
					seen[temp%10]=true;
					temp=temp/10;
				}
				if(ok())
				{
					//printf("Case #%d: %d\n",i,N*j);
					fprintf(out,"Case #%d: %d\n",i,N*j);					
					break;
				}
			}
		}
	}
	return 0;
}
