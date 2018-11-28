#include<fstream>
#include<string>
#include<cstdlib>
#include<sstream>
#include<cstdlib>
#include<iomanip>
#include<iostream>
using namespace std;
struct node
		{
			node *next;
			string str;
		};
node* insin(string s,node *a);
int mimno(node*a,node*b)
{
    int i=0;
    while(b!=NULL)
    {

        if(a->str<b->str)
        {
            i++;
            a = a->next;
            b=b->next;
        }
        else
            b=b->next;
    }
    cout<<i;
    return i;
}

node* insin (string s,node* a)
{
    node *c;
    if(a == NULL)
    {
        c = new node;
        c->str = s;
        c->next = NULL;
        a = c;
        return a;
    }
    else
    {
        node *d;
        d = a;
        if(a->str>s)
        {
          c = new node;
            c->str = s;
            c->next = a;
            a = c;
            return a;
        }
        else
        {
            while(a->next!=NULL&&a->next->str<s)
            {
                a = a->next;
            }
            if(a->next == NULL)
            {
                c = new node;
                c->str = s;
                c->next = NULL;
                a->next = c;
            }
            else
            {
                c = new node;
                c->str = s;
                c->next = a->next;
                a->next = c;
            }
            return d;
        }
    }
}
node* deletelast(node*a)
{
    if(a->next == NULL)
    {
        free(a);
        return NULL;
    }
    else
        {
            node *c;
            c = a;
        while(a->next->next!=NULL)
        {
            a = a->next;
        }
        node *b;
        b = a->next;
        a->next = NULL;
        free(b);
        return c;
        }
}
node* deletefirst(node*a)
{
    if(a!=NULL)
    {
        node *b1;
        b1 = a;
        a = b1->next;
        free(b1);
        return a;
    }
    else
        return a;
}
int maxno(node* a,node* b)
{
    int i=0;
    while(a!=NULL)
    {
        while(a!=NULL && a->str<b->str)
        {
            i++;
            a=deletefirst(a);
            b=deletelast(b);
        }

        while(a!=NULL&&(a->str)>(b->str))
        {
            a=deletefirst(a);
            b=deletefirst(b);
        }

    }
    return i;
}
int main ()
{
    fstream fin;
    fstream fohash;
    fohash.open("D-large.out",ios::out);
    fin.open("D-large.in",ios::in);
    char ch='0';
    int i=0,j=0,k,l=1,m,n;
    node *a, *b;
    string s1;
    cout<<fixed;
    fohash<<fixed;
    fin<<fixed;
    cout<<setprecision(6);
    fin<<setprecision(6);
    fohash<<setprecision(6);
     while(fin && ch!=' ' && ch!='\n' && ch!='\t')
        {
            j = 10*j + (int)ch - 48;
            fin.get(ch);
        }
        fin.get(ch);
        for(;j>0;j--)
        {
            a = NULL;
            b = NULL;
            while(fin && ch!=' ' && ch!='\n' && ch!='\t')
            {
                i = 10*i + (int)ch - 48;
                fin.get(ch);
            }
            fin.get(ch);
            for(k=0;k<i;k++)
                {
                    while(fin && ch!=' ' && ch!='\n' && ch!='\t')
                    {
                        s1+=ch;
                        fin.get(ch);
                    }
                    if(fin)
                        fin.get(ch);
                    a = insin(s1,a);

                    s1.clear();
                }
                for(k=0;k<i;k++)
                {
                    while(fin && ch!=' ' && ch!='\n' && ch!='\t')
                    {
                        s1+=ch;
                        fin.get(ch);
                    }
                    fin.get(ch);
                    b = insin(s1,b);

                    s1.clear();
                }
                n = mimno(a,b);
                m = maxno(a,b);
                m = i-m;

                n = i-n;
                i = 0;
                a = NULL;
                b = NULL;

                fohash<<"Case #"<<l<<": "<<m<<" "<<n<<"\n";
                l++;
        }
}
