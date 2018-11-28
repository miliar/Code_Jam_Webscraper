#include<stdio.h>
#include<iostream>
#include<string.h>
using namespace std;
class pan
{
	int co,ci;
	char d[1000];
	int cc;
	void invert(int v);
	public:
	pan(char [1000]);
	int invert();
	void counta();
};
void pan::invert(int v)
{
	for(int i=0;i<=v;i++)
	{

		//t hh=strcmp(d[i],-)
		if(d[i]=='-')
			d[i]='+';
		else
			d[i]='-';
	}
cc++;
	counta();
//	puts(d);
}
pan::pan(char s[100])
{
	cc=0;
	co=0;ci=0;

	strcpy(d,s);
//	puts(d);
	for(int i=0;i<strlen(d);i++)
	{
		if(d[i]=='+')
			ci++;
		else
			co++;
	}
}
void pan::counta()
{
	ci=0;
	co=0;
	for(int i=0;i<strlen(d);i++)
	{
		if(d[i]=='+')
			ci++;
		else
			co++;
	}

}
int pan::invert()
{int i;
	while(1)
	{//cc++;
//		if(co>ci)
//			invert(strlen(d)-1);
		if(ci==strlen(d))
			return cc;
		else
		{for(i=0;i<strlen(d);i++)
			{
				if(d[i]=='-')
					break;
			}
			if(i>0)
			invert(i-1);
	//		cc++;
for(i=i;i<strlen(d);i++)
                        {
                                if(d[i]=='+')
                                        break;
                        }
			if(i==strlen(d))
			{
return cc+1;
}
else if(i>0)
			invert(i-1);
			counta();
		}
	}
}
int main()
{
	int i,k,l;
	//pan F;
	scanf("%d ",&l);
	for(i=1;i<=l;i++)
	{char s[1000];
		scanf("%s",s);
		pan F(s);
		k=F.invert();
		printf("Case #%d: %d\n",i,k);
	}

}
