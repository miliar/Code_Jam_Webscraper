#include <stdio.h>
#include <stdlib.h>



struct book{

	char p;

	struct book* next;

};



struct book* head = NULL;

struct book* curr = NULL;



void insertend(char n)

{

	if(head==NULL)

	{

		struct book* ptrh=(struct book*)malloc(sizeof(struct book));

		ptrh->p=n;

		ptrh->next=NULL;

		head=curr=ptrh;

	}

	else

	{

		struct book* ptr=(struct book*)malloc(sizeof(struct book));

		ptr->p=n;

		ptr->next=NULL;

		curr->next=ptr;

		curr=ptr;

	}

}



void insertbegin(char n)

{

	if(head==NULL)

	{

	struct book* ptrh=(struct book*)malloc(sizeof(struct book));

	ptrh->p=n;

	ptrh->next=NULL;

	head=curr=ptrh;

	}

	else
	{

	struct book* ptr=(struct book*)malloc(sizeof(struct book));

	ptr->p=n;

	ptr->next=head;

	head=ptr;
	}

}

void print (struct book * head)

{

	struct book* temp;

	temp=head;

	

	while(temp != NULL)

	{

		printf("%c",temp->p);

		temp=temp->next;

	}

	while (head != NULL)
	{
		temp = head;
		head = head->next;
		free (temp);
	}

	printf ("\n");	
}

int main ()
{

	freopen("A-large.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int t;
	scanf ("%d",&t);
	int b = 1;
	while (b <= t)
	{
		char s[1002];
		scanf ("%s",s);
//		char ans[1002];
		int i = 1;
		char c = s[0];
		insertend (c);
		while (s[i] != '\0')
		{
			if (s[i] >= c)
			{
				insertbegin (s[i]);
				c = s[i];
			}
			else
				insertend (s[i]);
			i++;
		}
		printf ("Case #%d: ",b);
		print (head);
		b++;
		head = NULL;
		curr = NULL;
	}
}
