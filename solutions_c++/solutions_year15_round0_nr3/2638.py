#include<iostream>
#include<algorithm>
using namespace std;

char a[10005];
char aa[10005];
static int rule[5][5] = {{0,0,0,0,0},{0,1,2,3,4},{0,2,-1,4,-3},{0,3,-4,-1,2},{0,4,3,-2,-1}};

class element{
public:
	int sign; // 1 or -1
	int character; // 1 for 1, 2 for i, 3 for j, 4 for k
	void assign(int sign0,int character0){
		sign=sign0;
		character=character0;
	}
	element(int sign0,int character0){
		sign=sign0;
		character=character0;
	}
	element operate(element ele) {
		element result;
		result.sign = sign*ele.sign;
		result.character=rule[character][ele.character];
		if(result.character<0) {
			result.character *= -1;
			result.sign*=-1;
		}
		return result;
	}
	element(element& ele){
		sign=ele.sign;
		character=ele.character;
	}
	element(){}
};

char readchar(){
	char charin=getchar();
	while(charin==' ' || charin=='\r' || charin=='\n'){
		charin=getchar();
	}
	return charin;
}

int main()
{
	freopen("C-small-attempt1.in","r",stdin);
	freopen("C-small-attempt1.out","w",stdout);
	element elea[4];
	elea[0].assign(1,1);
	elea[1].assign(1,2);
	elea[2].assign(1,3);
	elea[3].assign(1,4);
	int t;
	scanf("%d",&t);
	for(int c=1;c<=t;c++){
		aa[0]=0;
		int l,x;
		scanf("%d%d",&l,&x);
		scanf("%s",a);

		// step 1: examine if l*x<3
		if(l*x<3){
			printf("Case #%d: NO\n",c);
			continue;
		}

		// step 2: see if the product of all characters is -1
		element m(elea[0]);
		for(int i=0;i<l;i++)
			m=m.operate(elea[a[i]-'i'+1]);
		if(m.sign==1 && m.character==1){
			printf("Case #%d: NO\n",c);
			continue;
		}
		if(m.sign==-1 && m.character==1){
			if(x%2==0){
				printf("Case #%d: NO\n",c);
				continue;
			}
		}
		else if(x%4!=2){
			printf("Case #%d: NO\n",c);
			continue;
		}

		// step 3: find if i and k exists
		for(int i=0;i<x;i++){
			strcat(aa,a);
		}
		element product(1,1);
		int prefixcnt;
		for(prefixcnt=0;prefixcnt<l*x;prefixcnt++){
			product = product.operate(elea[aa[prefixcnt]-'i'+1]);
			if(product.sign==1 && product.character==2)
				break;
		}
		if(prefixcnt==l*x){
			printf("Case #%d: NO\n",c);
			continue;
		}
		product.assign(1,1);
		int suffixcnt;
		for(suffixcnt=l*x-1;suffixcnt>=0;suffixcnt--){
			product = elea[aa[suffixcnt]-'i'+1].operate(product);
			if(product.sign==1 && product.character==4)
				break;
		}
		if(suffixcnt==-1){
			printf("Case #%d: NO\n",c);
			continue;
		}
		if(suffixcnt<=prefixcnt){
			printf("Case #%d: NO\n",c);
			continue;
		}
		printf("Case #%d: YES\n",c);
	}
	return 0;
}

