#include<iostream>
#include<cstdio>
#include<cmath>
#include<queue>
#include<algorithm>
#include<stack>
#include<sstream>
#include<cstring>
#include<string>
#include<vector>
#include<map>
using namespace std;
#define LL long long
#define LD long double
#define cl(a,b) memset(a,b,sizeof(a));
const int INF=1<<30;
int numbers[10];

string numberToString(int number){
	stringstream ss;
	ss<<number;
	return ss.str();
}

void checkNumber(string str1){
	int l=str1.length();
	for(int i=0;i<l;i++){
		int n1 = str1[i] - '0';
		numbers[n1]=1;
	}
}

int isFull(){
	int flag=1;
	for(int i=0;i<10;i++){
		if(!numbers[i]){
			flag=0;
			break;
		}
	}
	return flag;
}

int main(){
	int T,n,answer=0;
	string sum;
	cin>>T;
	for(int ti=1;ti<=T;ti++){
		cl(numbers,0);
		scanf("%d",&n);
		sum=numberToString(n);
		if(n==0){
			printf("Case #%d: INSOMNIA\n",ti);
			continue;
		}
		int flag=0;
		for(int i=1;i<10086;i++){
			checkNumber(sum);
			if(isFull()){
				answer=i*n;
				printf("Case #%d: %d\n",ti,answer);
				flag=1;
				break;
			}
			sum=numberToString((i+1)*n);
		}
		if(!flag)printf("Case #%d: INSOMNIA\n",ti);
	}
	
	return 0;
}

