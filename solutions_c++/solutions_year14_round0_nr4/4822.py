#include<stdio.h>
#include<stdlib.h>
typedef struct node node;
struct node
{
	double data;
	node *prev;
	node *next;
};
void add(node *head,node **tail,double d)
{
	node *ptr;
	node *hook;
	ptr=(node*)malloc(16);
	ptr->data=d;
	hook=head;
	while(hook)
	{
		if(hook->data<d)
		{
			if(hook->next)
			{
				hook=hook->next;
			}
			else
			{
				ptr->prev=hook;
				ptr->next=0;
				hook->next=ptr;
				*tail=ptr;
				break;
			}
		}
		else
		{
			ptr->prev=hook->prev;
			ptr->next=hook;
			hook->prev=ptr;
			ptr->prev->next=ptr;
			break;
		}
	}
}
void release(node *head)
{
	node *ptr;
	node *hook;
	ptr=head->next;
	while(ptr)
	{
		hook=ptr->next;
		free(ptr);
		ptr=hook;
	}
	head->next=0;
}
int main()
{
	int T;
	int N;
	int n;
	node *Nhead,*Ntail,*Npivot;
	node *Khead,*Ktail,*Kpivot;
	double d;
	int dw,w;
	int i;
	Nhead=(node*)malloc(16);
	Nhead->data=-1;
	Nhead->prev=0;
	Nhead->next=0;
	Khead=(node*)malloc(16);
	Khead->data=-1;
	Khead->prev=0;
	Khead->next=0;
	scanf("%d",&T);
	for(n=0;n<T;n++)
	{
		w=0;
		dw=0;
		scanf("%d",&N);
		for(i=0;i<N;i++)
		{
			scanf("%lf",&d);
			add(Nhead,&Ntail,d);
		}
		for(i=0;i<N;i++)
		{
			scanf("%lf",&d);
			add(Khead,&Ktail,d);
		}
		Npivot=Nhead->next;
		Kpivot=Khead->next;
		while(1)
		{
			if(Npivot->data>Kpivot->data)
			{
				dw++;
				Kpivot=Kpivot->next;
			}
			if(Npivot->next)
			{
				Npivot=Npivot->next;
			}
			else
			{
				break;
			}
		}
		Npivot=Nhead->next;
		Kpivot=Khead->next;
		while(1)
		{
			if(Ntail->data>Ktail->data)
			{
				w++;
				Kpivot=Kpivot->next;
			}
			else
			{
				Ktail=Ktail->prev;
			}
			if(Ntail!=Npivot)
			{
				Ntail=Ntail->prev;
			}
			else
			{
				break;
			}
		}
		release(Nhead);
		release(Khead);
		printf("Case #%d: %d %d\n",n+1,dw,w);
	}
	free(Nhead);
	free(Khead);
	return 0;
}