// Olimp _2.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;

struct node {
	char data;
	node *next;
};

void push(node *&top,int x) {
	node *p = new node;
	p->data = x;
	p->next = top;
	top = p;
}

node* find(node *top) {
	while (top) {
		if (top->data == '-') return top;
		top = top->next;
	}
	return NULL;
}

void f(node* top) {
	while (top) {
		if (top->data == '+') top->data = '-';
		else top->data = '+';
		top = top->next;
	}
}
bool pr(node *top) {
	while (top) {
		if (top->data == '-') return true;
		top = top->next;
	}
	return false;
}
int main()
{
	ifstream in("B-large.in");
	ofstream out("B-large.out");
	int t; int q;
	string c;
	getline(in, c);
	istringstream(c) >> t;

	for (int j = 0; j < t; j++) {
		q = 0;
		node *top = NULL;
		string s;
		getline(in, s);
		int i = 0;
		while (i < s.length()) {
			if (s[i] == '+' || s[i] == '-') push(top, s[i]);
			i++;
		}
		while (pr(top)) {
			node *p = find(top);
			f(p);
			q++;
		}
		out << "Case #" << j + 1 << ": " << q << endl;
		cout << "Case #" << j + 1 << ": " << q << endl;
	}
	return 0;
}

