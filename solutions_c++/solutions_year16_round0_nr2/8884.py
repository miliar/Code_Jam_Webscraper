#include<stdio.h>
#include<stdlib.h>
#include<string.h>
struct node
{
	char data;
	struct node *prev;
}*newnode,*temp,*top=NULL;

void push(char element)
{
	newnode=(struct node*)malloc(sizeof(struct node));
	newnode->data=element;
	newnode->prev=NULL;
	if(top==NULL)
	{
		top=newnode;
	}
	else
	{
		newnode->prev=top;
		top=newnode;
	}
	
}


int compare(int sount)
{
	char f1,f2,f3;
	int flag=0;
	struct node* t3;
	struct node* t4=top;
	f1=top->data;
	for(t3=t4;t3!=NULL;t3=t3->prev)
	{
		
		
		if(t3->data!=f1)
		{
			flag=1;
			break;
		}
	}
	
	if(flag==0)
	{
		f2=f1;
	    if(f2=='-')
		{
		for(t3=t4;t3!=NULL ;t3=t3->prev)
			{
				t3->data='+';	
			}
			sount++;
	    }
	    
	    return sount;
	
	   
	}
	
	else
	{
	

		for(t3=t4;t3->data==f1 && t3!=NULL ;t3=t3->prev)
		{
		
			if(t3->data=='-')
			{
				t3->data='+';
		
			}
			else
			{
				t3->data='-';
			}
			
		}
		sount++;
	
		compare(sount);
	}
	
	
}
int main()
{
	FILE *fp1,*fp2;
	fp1=fopen("input.in","r");
	fp2=fopen("output.out","w");
	int N,t,l,f,g,count,j;	
	fscanf(fp1,"%d",&t);
	for(int i=1;i<=t;i++)
	{
		char s[100];
		struct node* t1;
		fscanf(fp1,"%s",s);
		l=strlen(s);
		count=0;
		for(j=0,f=l-1;j<l,f>=0;j++,f--)
		{
			push(s[f]);
		}
		g=compare(count);
		fprintf(fp2,"case #%d: %d\n",i,g);
	}	
	return 1;
}
