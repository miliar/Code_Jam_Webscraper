#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>

#include <vector>
#include <string>
#include <map>
#include <algorithm>

using namespace std;

typedef enum{qv1=0,qvi=1,qvj=2,qvk=3}quaternion_value;

typedef struct quaternion{
	quaternion_value value;
	int sign;
}quaternion;

quaternion make_quaternion(char c, int sign){
	quaternion ret;
	ret.sign = sign;
	switch (c){
	case '1':
		ret.value=qv1;
		break;
	case 'i':
		ret.value=qvi;
		break;
	case 'j':
		ret.value=qvj;
		break;
	case 'k':
		ret.value=qvk;
		break;
	default:
		assert(0);
		break;
	}
	return ret;
}

const int qmul_v_table[4][4]={
	{qv1, qvi, qvj, qvk},
	{qvi, qv1, qvk, qvj},
	{qvj, qvk, qv1, qvi},
	{qvk, qvj, qvi, qv1},
};

const int qmul_s_table[4][4]={
	{1, 1, 1, 1},
	{1,-1, 1,-1},
	{1,-1,-1, 1},
	{1, 1,-1,-1},
};

quaternion mul_quaternion(quaternion a, quaternion b){
	quaternion ret;
	ret.value = (quaternion_value)qmul_v_table[a.value][b.value];
	ret.sign = a.sign * b.sign * qmul_s_table[a.value][b.value];
	return ret;
}

int equal_quaternion(quaternion a,quaternion b)
{
	return a.sign==b.sign && a.value==b.value;
}

const char q_print_table[4]={'1','i','j','k'};

void print_quaternion(quaternion q)
{
	if (q.sign==-1)printf("-");
	printf("%c",q_print_table[q.value]);
}

int main(void)
{
	int t,T;
	scanf("%d\n",&T);
	//printf("T=%d\n",T);
	for (t=1;t<=T;t++){
		int L,X;
		char str[10001];
		char full_str[10001];
		scanf("%d %d\n",&L,&X);
		scanf("%s\n",str);
		//printf("%d %d %s\n",L,X,str);
		int ok=0;
		if (L*X>=3){
			// Generate string
			int i,j;
			quaternion qs[10000];
			strcpy(full_str,"");
			for (i=0;i<X;i++){
				strcat(full_str,str);
				for (j=0;j<L;j++){
					qs[i*L+j]=make_quaternion(str[j],1);
				}
			}
			int full_len=L*X;
			int s0,s1,s2;
			s0=0;
			quaternion qi,qj,qk,q1;
			qi=make_quaternion('i',1);
			qj=make_quaternion('j',1);
			qk=make_quaternion('k',1);
			q1=make_quaternion('1',1);
			quaternion qii,qjj,qkk;
			qii=q1;
			for (s1=1;s1<=full_len-2;s1++){
				qii=mul_quaternion(qii,qs[s1-1]);
				if (equal_quaternion(qi,qii)){
					qjj=q1;
					for (s2=s1+1;s2<=full_len-1;s2++){
#if 0
						char str0[10000],str1[10000],str2[10000];
						memset(str0,0,sizeof(str0));
						memset(str1,0,sizeof(str1));
						memset(str2,0,sizeof(str2));
						memcpy(str0,&full_str[s0],s1-s0);
						memcpy(str1,&full_str[s1],s2-s1);
						memcpy(str2,&full_str[s2],full_len-s2);
						//printf("%s %s %s\n",str0,str1,str2);
#endif
						qjj=mul_quaternion(qjj,qs[s2-1]);
						if (equal_quaternion(qj,qjj)){
							qkk=q1;
							int ss;
							for (ss=s2;ss<full_len;ss++){
								qkk=mul_quaternion(qkk,qs[ss]);
							}
							if (equal_quaternion(qk,qkk)){
								ok=1;
								goto finish;
							}
						}
					}// s2 loop
				}
			}// s1 loop
		}
finish:;
		if (ok){
			printf("Case #%d: YES\n",t);
		}
		else printf("Case #%d: NO\n",t);
	}
	return 0;
}
