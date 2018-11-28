#include<iostream>
using namespace std;
long long T,L,X;
char str[10010];
char three[4]="ijk";
int mycompute(int a,int b)
{
	if(a==1)return b;
	if(a==-1)return -b;
	if(abs(a)==abs(b))
	{
		return a==b?-1:1;
	}

	if((a-b+3)%3==2)
	{
		for(int i=0;i<3;i++)
			if(three[i]!=a&&three[i]!=b)return three[i];
	}
	else if((a-b+3)%3==1)
	{
		for(int i=0;i<3;i++)
			if(three[i]!=a&&three[i]!=b)return -three[i];
	}
	else
		return -1;
}

int calpiece(char s[])
{
	int sign=1;
	int res=1;
	for(int i=0;i<strlen(s);i++)
	{
		res=mycompute(res,s[i]);
		if(res<0)
		{
			sign=-sign;
			res=-res;
		}
	}
	return sign==1?res:-res;
}


int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int lastvalue;
	int sign;
	int loop=0;
	int loop2=0;
	int tres=1;
	int pos=0;
	int flag=0;
	int appearedvalue[8]={0},apppos=0;
	int onePiece;
	scanf("%d",&T);
	for(int k=1;k<=T;k++)
	{
		flag=0;
		loop=0;
		loop2=0;
		pos=0;
		sign=1;
		scanf("%lld%lld",&L,&X);
		scanf("%s",str);
		tres=1;
		lastvalue=1;
		apppos=0;
		onePiece=calpiece(str);
		//cout<<(char)abs(onePiece);
		while(loop<X)
		{
			while(loop2<L)
			{
				tres=mycompute(tres,str[loop2]);
				if(tres<0)
				{
					sign=-sign;
					tres=-tres;
				}
				loop2++;
				if(sign==1&&tres==three[pos])
				{
					pos++;
					tres=1;
					memset(appearedvalue,0,sizeof(appearedvalue));
					apppos=0;
				}
				if(pos==3)break;
			}
			
			loop++;
			if(pos==3)break;

			for(int i=0;i<8;i++)
			{
				if((sign==1&&tres==appearedvalue[i])||(sign==-1&&tres==-appearedvalue[i]))
				{
					flag=-1;
					break;
				}
			}

			if(flag==-1)break;
			appearedvalue[apppos++]=sign==1?tres:-tres;
			loop2=0;
			
		}
		
		if(flag==-1)
		{
			printf("Case #%d: NO\n",k);
		}
		else
		{
			tres=1;
			if(pos==3)
			{
				for(int i=loop2;i<L;i++)
				{
					tres=mycompute(tres,str[i]);
					if(tres<0)
					{
						sign=-sign;
						tres=-tres;
					}
				}
				int tmp=(X-loop)%4;
				for(int i=0;i<tmp;i++)
				{
					if(onePiece<0)sign=-sign;
					tres=mycompute(tres,abs(onePiece));
					if(tres<0)
					{
						sign=-sign;
						tres=-tres;
					}
				}
				if(sign==-1||tres!=1)
					printf("Case #%d: NO\n",k);
				else
					printf("Case #%d: YES\n",k);
			}
			else
				printf("Case #%d: NO\n",k);
		}
	}

	fclose(stdin);
	fclose(stdout);
	return 0;
}