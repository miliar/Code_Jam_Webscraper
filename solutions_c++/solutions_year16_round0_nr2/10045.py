#include<stdio.h>
#include<stdlib.h>
#include<vector>
#include<iostream>
#include<string>
#include<algorithm>
using namespace std;

int stacksize;
//from is point from top
int flip(int st, int from){
	for(int i=stacksize-from; i<stacksize; i++){
		if(st&(1<<i-1)==0)
			st = st & 1<<(stacksize-1-i);
	}
	return st;
}

int main(void){
	int T;
//	freopen("input1.txt","r",stdin);
	scanf("%d",&T);

	for(int i=0; i<T; i++){
		string input;
		cin >> input;

		stacksize = (int)input.size();
		vector<char> st;
			
		int stack=0;
		int goal=(1<<stacksize)-1;
		int count = 0;
		for(int j=stacksize-1; j>=0; j--){
			if(input[j]=='+'){
				st.push_back('+');
				stack |= 1<<count;
			}
			else
				st.push_back('-');
			
			count++;
		}
	
	// 0 is bottom
		int sol=0;
		while(stack!=goal){
			int end = stacksize-1;
			stack=0;
			count=0;
			if(st[end]=='+'){//end is top
				int count = end-1;//minus index
				while(st[count]!='-') count--;
				for(int j=count+1; j<=end; j++){
					if(st[j]=='+'){ st[j]='-';}
					else st[j]='+';
				}
				reverse(st.begin()+count,st.end());
	
				for(int j=0; j<=end; j++){
					if(st[j]=='+'){
						stack |= 1<<j;
					}
					count++;
				}
			}
			else{
				while(st[count]!='-') count++;
				for(int j = count; j<=end; j++){
					if(st[j]=='+') st[j]='-';
					else st[j]='+';
				}
				reverse(st.begin()+count,st.end());
				for(int j=0; j<=end; j++){
					if(st[j]=='+'){
						stack |= 1<<j;
					}
				}
			}
			sol++;	
		}
		printf("Case #%d: %d\n",i+1,sol);
	}
}
