#include <cstdio>
#include <cstring>
#include <utility>
#include <queue>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;
struct Num {
	bool neg;
	char ch;
	Num() {}
	Num(bool _neg,char _ch) {neg=_neg,ch=_ch;}
};
Num operator*(const Num &A,const Num &B) {
	bool neg=0;
	char ch;
	if(A.ch=='1') {
		ch=B.ch;
	}else if(A.ch=='i') {
		if(B.ch=='1') ch='i';
		if(B.ch=='i') ch='1',neg=1;
		if(B.ch=='j') ch='k';
		if(B.ch=='k') ch='j',neg=1;
	}else if(A.ch=='j') {
		if(B.ch=='1') ch='j';
		if(B.ch=='i') ch='k',neg=1;
		if(B.ch=='j') ch='1',neg=1;
		if(B.ch=='k') ch='i';
	}else if(A.ch=='k') {
		if(B.ch=='1') ch='k';
		if(B.ch=='i') ch='j';
		if(B.ch=='j') ch='i',neg=1;
		if(B.ch=='k') ch='1',neg=1;
	}
	return Num((A.neg)^(B.neg)^neg,ch);
}
char S[100001];
Num num[100001];
int main() {
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++) {
		int L,X;
		scanf("%d %d",&L,&X);
		scanf("%s",S);
		for(int i=0;i<L*X;i++) {
			num[i]=Num(0,S[i%L]);
		}
		for(int i=0;i+1<L*X;i++) {
			num[i+1]=num[i]*num[i+1];
		}
		bool OK=1;
		if(num[L*X-1].ch!='1'||!num[L*X-1].neg) {
			OK=0;
		}else {
			int pos1,pos2;
			for(pos1=0;pos1<L*X;pos1++) {
				if(num[pos1].ch=='i'&&!num[pos1].neg) break;
			}
			for(pos2=L*X-1;pos2>=0;pos2--) {
				if(num[pos2].ch=='k'&&!num[pos2].neg) break;
			}
			OK=(pos1<pos2);
		}
		printf("Case #%d: %s\n",t,OK?"YES":"NO");
	}
}