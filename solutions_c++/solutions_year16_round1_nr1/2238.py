#include<stdio.h>
#include<iostream>
#include<string.h>

using namespace std;

struct node
{
    int val;
    node *next;
    node *prev;
};

class linkedlist
{
    node *head;
public:
    linkedlist()
    {
        head=new node;
        head->next=NULL;
        head->prev=NULL;
    }
    void insert_at_first(int x)
    {
        node *q;
        q=new node;
        q->val=x;
        q->next=head->next;
        q->prev=head;
        head->next=q;
    }
    void insert_at_last(int x)
    {
        node *p=head;
        while(p->next!=NULL)
        {
            p=p->next;
        }
        node *q=new node;
        q->val=x;
        q->next=NULL;
        q->prev=p;
        p->next=q;
    }
    void insert_at_any(int x,int index)
    {
        int c=-1;
        node *p=head;
        while(p->next!=NULL)
        {
            c++;
            if(c==index)
                break;
            p=p->next;
        }
        node *q=new node;
        q->val=x;
        q->next=p->next;
        q->prev=p;
        p->next=q;

    }
    void delete_at_first()
    {
        if(head->next==NULL)
        {
            printf("The list is empty\n");
        }
        else
        {
            head->next=head->next->next;
            head->next->prev=head;
        }
    }
    void delete_at_last()
    {
        if(head->next==NULL)
        {
            printf("The list is empty\n");
        }
        else
        {
            node *p=head;
            while(p->next->next!=NULL)
            {
                p=p->next;
            }
            p->next=NULL;
        }
    }
    void delete_at_any(int index)
    {
        if(head->next==NULL)
        {
            printf("The list is empty\n");
        }
        else
        {
            int c=-1;
            node *p=head;
            while(p->next!=NULL)
            {
                c++;
                if(c==index)
                    break;
                p=p->next;
            }
            p->next=p->next->next;
            p->next->prev=p;
        }
    }
    void displayforward()
    {
        node *p=head;
        while(p->next!=NULL)
        {
            printf("%c",(p->next->val)+'A');
            p=p->next;
        }
        printf("\n");
    }
    void displaybackward()
    {
        node *p=head;
        while(p->next!=NULL)
        {
            p=p->next;
        }
        while(p->prev!=NULL)
        {
            printf("%d\n",p->val);
            p=p->prev;
        }
    }
};

int main()
{
    freopen("outtt.txt","w",stdout);
    int test;
    int tt=1;
    scanf("%d",&test);
    while(test--)
    {
        linkedlist *p;
        p=new linkedlist;
        string s;
        cin>>s;
        int l=s.length();
        int ma=s[0]-'A';
        for(int i=0;i<l;i++)
        {
            int temp=s[i]-'A';
            if(temp>=ma)
            {
                p->insert_at_first(temp);
                ma=temp;
            }
            else
            {
                p->insert_at_last(temp);
            }
        }
        printf("Case #%d: ",tt++);
        p->displayforward();
    }
    return 0;
}

