#include<iostream>
#include<fstream>
#define MAX 101

using namespace std;

int isHappy(char stack[]){
	for (int i = 0; i < strlen(stack); i++){ if (stack[i] == '-') return 0;	}
	return 1;
}

void reduce(char stack[]){
	char temp[MAX] = { stack[0], 0, };
	int len = 0;
	for (int i = 1; i < strlen(stack); i++){
		if (stack[i] != stack[i - 1]) temp[++len] = stack[i];
	}
	strcpy(stack, temp);
}

void main(){
	ifstream in;
	ofstream out;
	in.open("B-large.in");
	out.open("out.out");

	int t;
	in >> t;
	for (int i = 1; i <= t; i++){
		int cnt = 0;
		char stack[MAX] = { 0, };
		in >> stack;
		for (cnt = 0; !isHappy(stack); cnt++){
			reduce(stack);
			stack[0] = (stack[0] == '+' ? '-' : '+');
		}
		out << "Case #" << i << ": " << cnt << endl;
	}

	in.close();
	out.close();
}