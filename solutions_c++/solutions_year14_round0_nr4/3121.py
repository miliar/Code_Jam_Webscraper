#include<iostream>
#include<fstream>

using namespace std;

struct node
{
    double data;
    node *next;
};

void del(node *&start, node *&end, double data);
void add(node *&start, node *&end, double ele);
int main()
{
    int t, case_no=0;
    FILE *in  = fopen("C:\\Users\\Rizaraf\\Desktop\\input.in", "r");
    FILE *out  = fopen("C:\\Users\\Rizaraf\\Desktop\\output.txt", "w");
    fscanf(in, "%d", &t);
    while(t--)
    {
        case_no++;
        int n, wd =0, wf=0,x;
        fscanf(in, "%d", &n);
        node *a,*ae, *b,*be, *ac, *aec, *bc, *bec;
        a = NULL;   ae = NULL;
        b = NULL;   be = NULL;
        ac = NULL; aec = NULL;
        bc = NULL; bec = NULL;
        float it;
        double item;
        for(x=0; x<n; x++)
        {
            fscanf(in, "%f", &it);
            item = (double)it;
            add(a, ae, item);
            add(ac, aec, item);
        }
        for(x=0; x<n; x++)
        {
            fscanf(in, "%f", &it);
            item = (double)it;
            add(b, be, item);
            add(bc, bec, item);
        }
        while(a!=NULL)
        {
            if(ae->data<be->data)
            {
                node *y = b;
                while(y->data<ae->data)
                {
                    y = y->next;
                }
                del(a, ae, a->data);
                del(b, be, y->data);
            }
            else if(ae->data>be->data)
            {
                wd++;
                node *x = a;
                while(x->data<b->data)
                {
                    x = x->next;
                }
                del(a, ae, x->data);
                del(b, be, b->data);
            }
        }
        node *l;
        while(ac!=NULL)
        {
            l = bc;
            while(l!=NULL&&l->data<ac->data)
            {
                l = l->next;
            }
            del(ac, aec, ac->data);
            if(l==NULL)
            {
                wf++;

            }
            else
             del(bc, bec, l->data);

        }
        fprintf(out, "Case #%d: %d %d\n", case_no, wd, wf);
    }

    return 0;
}

void add(node *&start, node *&end, double ele)
{
    node *p = new node;
    p->data = ele;
    p->next = NULL;
    if(start==NULL)
    {
        start = p;
        end = p;
    }
    else if(p->data < start->data)
    {
        p->next = start;
        start = p;
    }
    else
    {
        node *q = start;
        while(q->next!=NULL&&q->next->data<p->data)
        {
            q = q->next;
        }
        if(q->next==NULL)
        {
            q->next = p;
            end = p;
        }
        else
        {
            p->next = q->next;
            q->next = p;
        }
    }
}

void del(node *&start, node *&end, double ele)
{
    node *p = start;
    if(p->data == ele)
    {
        start = p->next;
        delete p;
    }
    else
    {
        while(p->next->data!=ele)
        {
            p = p->next;
        }
        node *q = p->next;
        p->next = q->next;
        if(p->next == NULL)
        {
            end = p;
        }
        delete q;

    }
}
