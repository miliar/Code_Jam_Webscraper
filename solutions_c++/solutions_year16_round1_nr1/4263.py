#include <cstdio>
#include <cstring>
char input[10001],output[100][10001];
int num;
struct node
{
	char data;
	struct node *next;
}*head,*tail,*temp;
int main()
{
	
	scanf("%d",&num);
	for(int i=0;i<num;i++)
	{
		scanf("%s",input);
		temp = new node;
		temp->data = input[0];
		head = temp;
		tail = temp;
		int length = strlen(input);
		for(int j=1;j<length;j++)
		{
			temp = new node;
			temp->data = input[j];
			if(input[j]>=head->data)
			{
				temp->next=head;
				head = temp;
			}
			else
			{
				tail->next =temp;
				tail = temp; 
			}
		}
		temp = head;
		int count = 0;
		while(temp->next != NULL)
		{
			output[i][count]=temp->data;
			temp = temp->next;
			count++;
		}
		output[i][count]=temp->data;
	}
	for(int i=0;i<num;i++)
	{
			printf("\nCase #%d: %s",i+1,output[i]);
		
	}
}
