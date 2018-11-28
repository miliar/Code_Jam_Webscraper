#include<iostream>
#include<fstream>
using namespace std;


template<class T>
class Node
{
public:
	T value;
	Node<T>* prev;
	Node<T>* next;
	Node(T v,Node* p=NULL,Node* n=NULL):value(v),prev(p),next(n){}
};

template<class T>
class LinkedList
{
public:
	Node<T>* head;
	Node<T>* tail;
	int length;
	LinkedList()
	{
		length=0;
		head=tail=NULL;
	}
	void Insert(T v)
	{
		Node<T>*cur=head;
		if(length==0)
			head=tail=new Node<T>(v);
		else if(v<=head->value)
		{
			head->prev=new Node<T>(v,NULL,head);
			head=head->prev;
		}
		else if(v>=tail->value)
		{
			tail->next=new Node<T>(v,tail);
			tail=tail->next;
		}
		else
		{
			for(int i=0;i<=length-1;i++)
			{
				if(cur->value>v)
				{
					cur->prev->next=new Node<T>(v,cur->prev,cur);
					cur->prev=cur->prev->next;
					break;
				}
				cur=cur->next;
			}
		}
		length++;
	}
				
	void Remove(Node<T>* n)
	{
		if(length==0)
			return;
		else if(length==1)
		{
			delete n;
			head=tail=NULL;
			length--;
		}
		else
		{
			Node<T>* temp=n;
			if(n==head)
				head=n->next;
			else if(n==tail)
				tail=n->prev;
			else
			{
				n->prev->next=n->next;
				n->next->prev=n->prev;
			}
			delete n;
			length--;
		}
	}
	void Show()
	{
		Node<T>* cur=head;
		for(int i=1;i<=length;i++)
		{
			os<<cur->value<<" ";
			cur=cur->next;
		}
	}
};


int main()
{
	ifstream is;
	ofstream os;
	is.open("H:\\D-large.in");
	os.open("H:\\D-large.out");

	int t,n;
	is>>t;
	int score;
	double min1,min2;
	int minindex1,minindex2;
	for(int c=1;c<=t;c++)
	{
		is>>n;
		double* a=new double[n];
		double* b=new double[n];

		//Deceitful War
		score=0;
		LinkedList<double> la;
		LinkedList<double> lb;
		for(int i=0;i<n;i++)
		{
			is>>a[i];
			la.Insert(a[i]);
		}
		for(int i=0;i<n;i++)
		{
			is>>b[i];
			lb.Insert(b[i]);
		}
		for(int i=0;i<n;i++)
		{
			if(la.head->value<lb.head->value)
			{
				la.Remove(la.head);
				lb.Remove(lb.tail);
			}
			else
			{
				la.Remove(la.head);
				lb.Remove(lb.head);
				score++;
			}
		}
		os<<"Case #"<<c<<": "<<score<<" ";

		//War
		score=0;
		int* existb=new int[n];
		memset(existb,true,n);
		//min1: the minimum among b[..] not chosen
		//min2: the minimum among b[..] larger than a[i] not chosen
		for(int i=0;i<n;i++)
		{
			min1=10;
			minindex1=-1;
			min2=-1;
			minindex2=-1;
			for(int j=0;j<n;j++)
			{
				if(!existb[j])
					continue;
				if(b[j]<min2)
				{
					min2=b[j];
					minindex2=j;
				}
				if(b[j]>a[i])
				{
					if(b[j]<min1)
					{
						min1=b[j];
						minindex1=j;
					}
				}
			}
			if(minindex1==-1)
			{
				score++;
				existb[minindex2]=false;
			}
			else
				existb[minindex1]=false;
		}
		os<<score<<endl;
	}
	return 0;
}
