#include<iostream>

#define lim 800

FILE *inp, *out;

char str[101],temp[101];
int ans;

void invert(int l, int r)
{
	//printf("..inverting l=%d r=%d\n",l,r);
	int i,j,k;
	for(i=r,k=0;i>=l;--i,++k)
	{
		temp[k]=str[i];
		temp[k]=(temp[k]=='+'?'-':'+');
	}
	for(i=l,j=0;j<k;++i,++j)
	{
		str[i]==temp[j];
	}
}

int compute(int l, int r)
{
	//printf("..computing l=%d r=%d\n",l,r);	
	if(l>r)
	return 0;
	else
	{
		int i,newL=l;
		/*printf("str[%d,%d]= ",l,r);
		for(i=l;i<=r;++i)
		printf("%c",str[i]);
		printf("\n");*/
		while(newL<=r && str[newL]=='-')
		++newL;
		--newL;
		if(newL<l)
		{
			i=l;
			while(i<=r && str[i]=='+')
			{
				str[i]='-';
				++i;
			}
			return 1 + compute(l,r);
		}
		else
		{
			++newL;
			invert(newL,r);
			return 1 + compute(newL,r);
		}
	}
}

int main(){
	int i,j,T,size,l,r;
	inp = fopen("inp.in","r");
	out = fopen("out.txt","w");
	fscanf(inp,"%d",&T);
	for(i=1;i<=T;++i)
	{
		fscanf(inp,"%s",str);
		for(j=0;str[j]!='\0';++j);
		size=j;
		l=0;
		r=size-1;
		while(r>=0 && str[r]=='+')
		--r;
		ans=compute(l,r);
		printf("Case #%d: %d\n",i,ans);
		fprintf(out,"Case #%d: %d\n",i,ans);		
	}
	return 0;
}
