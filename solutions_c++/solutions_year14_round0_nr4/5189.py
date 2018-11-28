#include<iostream>
#include<stdio.h>
#include<string.h>
#include<fstream>
using namespace std;

class linklist
{
	private :

		// structure containing a data part and link part
		struct node
		{
			float data;
			node *link ;
		} *p ;

	public :

		linklist( ) ;
		void add (float item) ;
		int display( ) ;//returns total entries
		float get_special(float item);
		float get_special_d(float item);
		float get_special_e();
		int cnt();
		~linklist( ) ;
} ;

// initializes data member
linklist :: linklist( )
{
	p = NULL ;
}

// adds node to an ascending order linked list
void linklist :: add (float item)
{
    node *r, *temp, *old;
    if(p==NULL)
    {
        p=new node;
        p->link=NULL;
        p->data=item;
    }
    else if(item <= p->data)
    {
        r=new node;
        r->link=p;
        r->data=item;
        p=r;
    }
    else
    {
        temp=p;
        r=new node;
        r->data=item;
        while(temp->link!=NULL)
        {
            if(temp->data < item && temp->link->data >= item)
            {
                r->link=temp->link;
                temp->link=r;
                return;
            }
            else
                temp=temp->link;
        }
        r->link=NULL;
        temp->link=r;
    }
}

float linklist :: get_special(float item)
{
    float val=0;
	node *temp = p ,*q, *saved=NULL;
	// traverse the entire linked list
	if(p==NULL)
        return -1;
	while ( temp != NULL )
	{
	    if(temp->data > item)
	    {
	        val=temp->data;
	        if(p==temp)
	        {
                q = p -> link ;
                delete p ;
                p = q ;
	        }
	        else
	        {
                q = temp -> link ;
                delete temp ;
                saved->link = q ;
	        }
	        return val;
	    }
	    saved=temp;
	    temp=temp->link;
	}
	val=p->data;
    q = p -> link ;
    delete p ;
    p = q ;
    return val;
}

float linklist :: get_special_d(float item)
{
    float val=-1;
	node *temp = p ,*q;
	// traverse the entire linked list
	while ( temp != NULL )
	{
	    if(temp->data < item)
	        val=temp->data;
	    temp=temp->link;
	}
	if(val==-1)
        val=p->data;
    q = p -> link ;
    delete p ;
    p = q ;
    return val;
}

float linklist :: get_special_e()
{
    float val=-1;
	node *temp = p;
	while ( temp != NULL )
	{
	    val=temp->data;
	    temp=temp->link;
	}
    return val;
}

int linklist :: cnt( )
{
	node *q=p;
	int c=0;

	while ( q != NULL )
	{
		q = q -> link ;
		c++;
	}
	return c;
}

// deallocate memory
linklist :: ~linklist( )
{
	node *q ;

	while ( p != NULL )
	{
		q = p -> link ;
		delete p ;
		p = q ;
	}
}

linklist list_N, list_N1, list_K, list_K1;
int solution_dec_war()
{
    int ans=0;
    float w1, w2;
    while(1)
    {
        w1=list_K1.get_special(0);
        w2=list_N1.get_special(w1);
        if(w1!=-1)
        {
            if(w2>w1)
                ans++;
        }
        else
            break;
    }
    return ans;
}

int solution_war()
{
    int ans=0;
    float w1, w2;
    while(1)
    {
        w1=list_N.get_special(0);
        w2=list_K.get_special(w1);
        if(w1!=-1)
        {
            if(w1>w2)
                ans++;
        }
        else
            break;
    }
    return ans;
}


int main()
{
    int n, m=1, j, i;
    ifstream f2("D-large.in");
    f2>>n;
    ofstream f3("D-large.out", ios::app);
    int no;
    float w;
    while(m<=n)
    {
        f2>>no;
        for(i=0; i<no; i++)
        {
            f2>>w;
            list_N.add(w);
            list_N1.add(w);
        }
        for(i=0; i<no; i++)
        {
            f2>>w;
            list_K.add(w);
            list_K1.add(w);
        }
        f3<<"Case #"<<m<<": "<<solution_dec_war()<<" "<<solution_war()<<endl;
        list_N.~linklist();
        list_N1.~linklist();
        list_K.~linklist();
        list_K1.~linklist();
        m++;
    }
    return 0;
}

