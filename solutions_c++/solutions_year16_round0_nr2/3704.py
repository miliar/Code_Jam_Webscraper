#include<stdio.h>
#include<stdlib.h>
#include<stdint.h>

struct Data {
	int sum;
	bool data[100];
};


int len;
int best;
Data stack[101];

void init(char* src) {
	Data& d=stack[0];
	d.sum=0;
	for(len=0;src[len];++len) {
		if(d.data[len]=((src[len]=='+')?true:false)) ++d.sum;
	}
}

void toggle(Data& src, Data& dst, int pos) {
	dst.sum=src.sum;
	for(int i=0;i<=pos;++i) {
		if(dst.data[i]=!src.data[pos-i]) ++dst.sum; else --dst.sum;
	}
	for(int i=pos+1;i<len;++i) dst.data[i]=src.data[i];
}

void process(int level) {
	if(level>=best) return;
	
	if(stack[level].sum==len) {
		if(level<best) best=level;
		return;
	}
	if(stack[level].sum==0) {
		if(level+1<best) best=level+1;
		return;
	}
	
	for(int i=0;i<len;++i) {
		toggle(stack[level], stack[level+1], i);
		process(level+1);
	}
}

int inlineProcess() {
	Data& d=stack[0];
	int state=0;
	int toggle=0;
	for(int i=0;i<len;++i) {
		bool v=d.data[i];
		
		switch(state) {
		case 0:	// stan startowy
			if(v) state=1;	// w trybie +
			else state=2;	// w trybie -
			break;
		case 1:	// tryb +ów, czyli wszystko 0..i-1 jest +ami
			if(v) continue;	// kolejny +, czyli idziemy dalej
			// napotkaliśmy -, więc korygujemy do niego
			++toggle;
			state=2;	// więc wszystko teraz będzie -musami
			break;
		case 2: // tryb -ów, czyli wszystko 0..i-1 jest -ami
			if(!v) continue;	// kolejny -, czyli idzemy dalej
			++toggle;
			state=1;	// i teraz wszystko będzie plusami
			break;
		}
	}
	return toggle+(state==2?1:0);
}

int main(int argc, char** argv) {
	int tsts;
	char buf[105];
	
	scanf("%d", &tsts);
	for(int t=1;t<=tsts;++t) {
		scanf("%s", buf);
		init(buf);
		best=inlineProcess();
//		int il=best;
//		process(0);
//		if(il!=best) {
//			printf("ERRROR\n!");
//			return -1;
//		}
		
		printf("Case #%d: %d\n",t, best);
	}
	
	return 0;
}