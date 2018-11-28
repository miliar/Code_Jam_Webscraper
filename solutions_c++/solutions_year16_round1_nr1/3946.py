// leetcode.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
// Example program
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <string>
#include <math.h>

using namespace std;

struct Node
{
   char c;
   struct Node* next;
};

int main()
{
    ifstream infile("A-large.in");
	ofstream outfile;//("OUTPUT.txt");
	outfile.open("OUTPUT2.txt");
	long t,n,j,k,c;
	
    long count = 0;
	infile>>t;
	long long arr[101];
	
	for (long i=0; i<t; i++)
	{   
		string s;
		infile >> s;
		Node* root = new Node();
		root->next = NULL;
		Node* realroot = root->next;
		Node* last = root->next;
		for (int j=0; j<s.length(); j++)
		{
			if (root->next == NULL)
			{
				root->next = new Node();
				root->next->next = NULL;
				root->next->c = s[j];
				realroot = root->next;
				last = realroot;
				//cout<<"new root: "<<realroot->c<<"; ";
			}
			else
			{
				if (realroot->c > s[j])
				{
					Node* node = new Node();
					node->next = NULL;
					node->c = s[j];
					last->next = node;
					last = node;
					//cout<<"smaller: "<<last->c<<"; ";
				}
				else
				{
					Node* node = new Node();					
					node->c = s[j];
					node->next = realroot;
					realroot = node;
					//cout<<"bigger: "<<realroot->c<<"; ";
				}
			}
		}
		//cout<<endl;
		outfile <<"Case #"<<i+1<<": ";
		while (realroot!=NULL)
		{
			outfile << realroot->c;
			Node* tmp = realroot;
			realroot = realroot->next;
			delete tmp;
		}
		outfile <<endl;
	}


	infile.close();
	outfile.close();
	return 0;
}


