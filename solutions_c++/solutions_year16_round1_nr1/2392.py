#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<string.h>


using namespace std;
struct node
{
    char data;
    struct node *next;
};

void append(struct node **h, int data)
{
    struct node *t, *temp;
    temp = (struct node*)malloc(sizeof(struct node));
    temp->data=data;
    temp->next=NULL;
    t = *h;
    if(t==NULL)
    {
        *h = temp;
        return;
    }
    while(t->next)
        t=t->next;
    t->next=temp;

}


int main()
{
    int K = 0;
    int t;
    cin>>t;
    while(t--)
    {
        K++;
        struct node *h,*t;
         h= NULL;
        char s[1001];
        cin>>s;
        int size = strlen(s);
        int i;
        append(&h,s[0]);
        for(i=1;i<size;i++)
        {
            if(h->data>s[i])
                append(&h,s[i]);
            else
            {
                struct node  *temp;
                temp = (struct node*)malloc(sizeof(struct node));
                temp->data=s[i];
                temp->next=h;
                h=temp;
            }


        }
            cout<<"Case #"<<K<<": ";
          while(h)
            {
            cout<<h->data<<"";
            h=h->next;
            }
            cout<<"\n";


    }





}
