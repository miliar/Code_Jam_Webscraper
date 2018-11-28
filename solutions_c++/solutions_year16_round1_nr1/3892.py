/*int maintest(int argc,char **argv);*/
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>

#define FILEIO

struct element
{
	char c;
	struct element *next;
};

int main(int argc,char **argv) 
{ 

#ifdef FILEIO
	freopen("in.txt","r",stdin); 
	freopen("out.txt","w",stdout); 
#endif

	int N;
	char c;
	scanf("%d\n",&N);
	//scanf("%s",&c); //enter
	char array[2000];

	for(int i=0;i<N;i++)
	{
		memset(array,0,sizeof(char)*2000);

		scanf("%s\n",array);

		
		struct element *tail;
		struct element *head = (struct element *)malloc(sizeof(struct element));
		memset(head,0,sizeof(struct element));
		head->c = array[0];
		head->next = NULL;
		tail = head;

		for(int j=1;array[j]!='\0';j++)
		{
			if(array[j]>=head->c)
			{
				struct element *e = (struct element *)malloc(sizeof(struct element));
				e->c = array[j];
				e->next = head;
				head = e;
			}
			else
			{
				struct element *e = (struct element *)malloc(sizeof(struct element));
				e->c = array[j];
				e->next = NULL;
				tail->next = e;
				tail = e;
			}
		}
		printf("Case #%d: ",i+1);
		struct element *p = head;
		for(;;)
		{
			if(p!=NULL){
				printf("%c",p->c);
				p=p->next;
			}
			else
				break;
		}
		printf("\n");

		//printf("%s\n",array);
	}

#ifdef FILEIO
	fclose(stdin);
	fclose(stdout);
#endif  
	return 0; 
}
