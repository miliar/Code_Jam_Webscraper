#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;
ifstream fin("A-small-attempt0.in");
ofstream fout("out.txt");
int A[11];
int S,N;

int foo(int s,int index,int n) {
	if (index > n)
		return 0;
	if(s>A[index])
		return foo(s+A[index],index+1,n);
	else {
		if(s==1)
			return foo(s,index,n-1) + 1;
		else
			return min(foo(2*s-1,index,n) + 1,foo(s,index,n-1) + 1);
	}
}

void proc(int t){
	fin>>S>>N;
	for(int i=1;i<=N;i++)
		fin>>A[i];
	sort(A+1,A+N+1);

	fout<<"Case #"<<t<<": "<<foo(S,1,N)<<endl;
}

int main() {
	int T;
	fin>>T;

	for(int i=1;i<=T;i++)
		proc(i);
	return 0;
}
