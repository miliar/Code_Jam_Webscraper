
#include <bits/stdc++.h>
struct node
{
	char x;
	struct node * left;
	struct node * right;
};
void leftInsert(struct node * res, char x)
{
	//printf("left %d\n",res);
	if(res->left==NULL)
	{
		res->left=new struct node;
		res->left->x=x;
		res->left->left=res->left->right=NULL;
	}
	else
		leftInsert(res->left,x);
}
void rightInsert(struct node * res, char x)
{
	//printf("right %d\n",res);
	if(res->right==NULL)
	{
		res->right=new struct node;
		res->right->x=x;
		res->right->left=res->right->right=NULL;
	}
	else
	{
		rightInsert(res->right,x);
	}
}
void display(struct node * res)
{
	if(res==NULL)
		return;
	display(res->left);
	printf("%c",res->x );
	display(res->right);
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A.out","w",stdout);
	long long t,n,i,T,flag[10],v;
	char s[1111],lo,hi;
	struct node * res=NULL;
	scanf("%lld",&T);
	for(t=1;t<=T;t++)
	{
		getchar();
		scanf("%s",s);
		lo=hi='\0';
		for(i=0;s[i]!='\0';i++)
		{
			//printf("%c %c %c\n",s[i],lo,hi);
			//printf("##########\n");
			//display(res);
			//printf("\n");
			if(lo=='\0')
			{
				res=new struct node;
				res->x=s[i];
				res->left=res->right=NULL;
				lo=s[i];
				hi=s[i];
			}
			else
			{
				if(s[i]>=lo)
				{
					leftInsert(res,s[i]);
					lo=s[i];
				}
				else
				{
					rightInsert(res,s[i]);
					hi=s[i];
				}
			}
			//printf("%lld\n",i);
		}

		printf("Case #%lld: ",t);
		display(res);
		printf("\n");
	}
	return 0;
}