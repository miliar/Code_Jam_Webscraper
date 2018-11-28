#include <iostream>
#include <vector>
#include <cstring>
using namespace std;

struct node{
	int val;
	string color;
};

int main(){

	vector<node> myVector;

	int n;
	cin >> n;

	for(int i=0;i<n;i++){
		int val;
		string color;
		node* newnode = new node();
		cin >> newnode->val;
		cin >> newnode->color;
		myVector.push_back(*newnode);
	}

	vector<node>::iterator it;

	for(it=myVector.begin();it!=myVector.end();it++){
		cout << (*it).val << "	" << (*it).color << endl;
	}

	return 0;

}