#include<iostream>
#include<string>
#include<fstream>
using namespace std;
class list
{
	struct node
	{
		int x;
		node *next;
	};
	node *current; 
	node *head;
public:
	list()
	{
		current = head = NULL;
	}
	void insert(int x)
	{
		if (head == NULL)
		{
			head = new node;
			head->x = x;
			head->next = NULL;
			current = head;
		}
		else
		{
			node *ptr = new node;
			ptr->x = x;
			ptr->next = NULL;
			current->next = ptr;
			current = ptr;
		}
	}
	void insert_A(int x)
	{
		
			node *ptr = new node;
			ptr->next = head;
			ptr->x = x;
			head = ptr;
	}
	string display()
	{
		string q = "";
		cout << endl;
		int x=0;
		node *temp = head;
		while (temp != NULL)
		{
			x = temp->x;
			//cout <<(char)x;
			q = q + (char)x;
			temp = temp->next;
		}
		return q;
	}
	
};
void main()
{
	ifstream infile("input1.in");
	ofstream outfile("output.out");
	int Cases = 0;
	infile >> Cases;
	for (int i = 0; i < Cases; i++)
	{


		list a;
		string x;
		infile >> x;
		int *y = new int[x.size()];

		for (int i = 0; i < x.size(); i++)
		{
			y[i] = (int)x[i];
		}

		int c;
		for (int i = 0; i < x.size(); i++)
		{

			if (i == 0)
			{
				a.insert(y[i]);
				c = y[i];
			}
			else
			{
				if (c <= (y[i]))
				{
					a.insert_A(y[i]);
					c = y[i];
				}
				else
				{

					a.insert(y[i]);
				}
			}
		}
		outfile << "Case #" << i+1 << ": " << a.display()<<endl;
	}

	system("pause");
}