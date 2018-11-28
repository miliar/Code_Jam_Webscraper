#include<stdio.h>
#include<string.h>
#include<stdlib.h>
void addAtLast(struct ankit**,char);
char a[2016];
struct ankit
{
    char data;
    struct ankit *next;
};
void addAtLast(struct ankit** p,char x)
{
    struct ankit* acp =(struct ankit*)malloc(sizeof(struct ankit));
    if(*p==NULL)
    {

        acp->next=NULL;
        acp->data=x;
        *p=acp;
        return ;
    }
    struct ankit *last=*p;
    while(last->next!=NULL)
    {
        last=last->next;
    }
    last->next=acp;
    acp->data=x;
    acp->next=NULL;

}
void addAtBegin(struct ankit** p,char x)
{
    struct ankit* acp =(struct ankit*)malloc(sizeof(struct ankit));
    if(*p==NULL)
    {

        acp->next=NULL;
        acp->data=x;
        *p=acp;
        return ;
    }
    acp->next=*p;
    *p=acp;
    acp->data=x;
}
int main()
{
    int T,x=1;
    scanf("%d",&T);
    while(T--)
    {
        scanf("%s",&a);
        int l,i,j;
        struct ankit* p=NULL;
        char left=a[0];
        l=strlen(a);
        for(i=0;i<l;i++)
        {
            if(a[i]<left)
                addAtLast(&p,a[i]);
            else
            {
                left=a[i];
                addAtBegin(&p,a[i]);
            }
        }
        addAtLast(&p,NULL);
        printf("Case #%d: ",x);
        while(p!=NULL)
        {
            printf("%c",p->data);
            p=p->next;
        }
        printf("\n");
        x++;
    }
}
