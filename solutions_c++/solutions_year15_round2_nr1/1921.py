


#include <cstdio>
#include <cstdlib>
#include <string.h>
#include <math.h>
#include <iostream>

#include <algorithm>
#include <map>
#include <vector>
#include <set>

using namespace std;

#define EPS 0.000000001
#define INF 1000000000
#define N 1000001

int n;

int mem[N];

int flip(int number) {
	int ret = 0;
	while (number>0) {
		ret=ret*10+number%10;
		number/=10;
	}
	return ret;
}

void fillArray()
{
	mem[1]=1;

	for (int i=1;i<N;i++) {
	
		int count=mem[i];
		
		int f = flip(i);
		int p = i+1;
		
		if (p<N&&(mem[p]==0||mem[p]>count+1)) {
			mem[p]=count+1;
		}
		
		if (f<N&&(mem[f]==0||mem[f]>count+1)) {
			mem[f]=count+1;
		}
	}
}

int main() {
	
	fillArray();
	
	int T;
	cin>>T;
	int n;
	
	int caseNum=0;
	
	while (T-->0)
	{
		cin>>n;
		int result=mem[n];
		
		cout<<"Case #"<<++caseNum<<": "<<result<<endl;
	}
	
	return 0;
}

