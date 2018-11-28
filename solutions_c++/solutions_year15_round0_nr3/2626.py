#include<cstdio>
#include<cstring>

struct result{
	char p;
	int m;
	bool operator==(const result& another)const{
		return p==another.p && m==another.m;
	}
};
int mqval[4][4]={{1,1,1,1},{1,-1,1,-1},{1,-1,-1,1},{1,1,-1,-1}};
result multiply(result ar, result br){
	char a=ar.p;
	char b=br.p;

	if(b=='1')b=0;
	if(b>='i')b-='i'-1;
	char pval[5];
	int qval[5];
	if(a=='1'){
		strcpy(pval,"1ijk");
		for(int i=0;i<4;i++)qval[i]=mqval[0][i];
	}
	if(a=='i'){
		strcpy(pval,"i1kj");
		for(int i=0;i<4;i++)qval[i]=mqval[1][i];
	}
	if(a=='j'){
		strcpy(pval,"jk1i");
		for(int i=0;i<4;i++)qval[i]=mqval[2][i];
	}
	if(a=='k'){
		strcpy(pval,"kji1");
		for(int i=0;i<4;i++)qval[i]=mqval[3][i];
	}
	result r;
	r.p=pval[b];
	r.m=ar.m*br.m*qval[b];
	return r;
}
result divide(result rs,result qs){//qs * ? = rs
	const char* possible="1ijk";
	for(int i=0;i<2;i++){
		result q;
		q.m=i*2-1;
		for(int j=0;j<4;j++){
			q.p=possible[j];
			if(multiply(qs,q)==rs)
				return q;
		}
	}
}

result s[10240];
char in[10240];

int go(){
	int l,x;
	int n;
	char* raw_in = new char[10240];
	scanf("%d%d",&l,&x);
	scanf("%s",raw_in);
	in[0]=0;
	for(int i=0;i<x;i++)
		strcat(in,raw_in);
	result r;
	r.p='1';
	r.m=1;
	n=l*x;
	for(int i=0;i<n;i++){
		result q;
		q.p=in[i];
		q.m=1;
		s[i]=r=multiply(r,q);
	}
	//[0..i), [i..j), [j..n)
	for(int i=1;i<n;i++){
		for(int j=i+1;j<n;j++){
			result q1=s[i-1];
			if(q1.m!=1)continue;
			result q2=divide(s[j-1],s[i-1]);
			if(q2.m!=1)continue;
			result q3=divide(s[n-1],s[j-1]);
			if(q3.m!=1)continue;
			if(q1.p=='i'&&q2.p=='j'&&q3.p=='k')
				return 1;
		}
	}
	delete raw_in;
	return 0;
}

const char* r[]={"NO","YES"};
void doCount(int k){
	printf("Case #%d: %s\n",k,r[go()]);
}

int main(){
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++){
		doCount(i+1);
	}
}
