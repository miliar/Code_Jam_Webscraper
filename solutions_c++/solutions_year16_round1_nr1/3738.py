#include<stdio.h>
#include<vector>
#include<iostream>
#include<queue>
#include<algorithm>
#include<stack>
#include<stdlib.h>
#include<string.h>
#include<map>

#include <fstream>
#define ll long long
using namespace std;
int N;
char A[1004];
char B[1004];
stack<char> st;
int main(){
	ofstream coutf;
	coutf.open("output.txt");
	int t, T;
	int len = 0;
	int token = 0;
	scanf("%d", &T);
	for (t = 0; t < T; t++){
		memset(A, 0, sizeof(A));
		memset(B, 0, sizeof(B));
		len = 0;
		token = 0;
		scanf("%s", A);
		for (int i = 0; A[i]; i++){
			len++;
		}
		st.push(A[0]);
		for (int i = 1; i < len; i++){
			if (st.top() > A[i]){
				B[token++] = A[i];
			}
			else st.push(A[i]);
		}
		//printf("Case #%d: \n", t + 1);
		coutf << "Case #" << t + 1 << ": "; 
		while (!st.empty()){
			coutf << st.top();
			//printf("%c", st.top());
			st.pop();
		}
		for (int i = 0; i < token; i++){
		//	printf("%c", B[i]);
			coutf << B[i];
		}
		coutf << '\n';
	//	printf("\n");
	
	}

	return 0;
}
