#include <stdio.h>
#include <math.h>
#include <string.h>
#include <iostream.h>

/*#define MAXN 10000
class segtree{
public:
	int n,cnt[MAXN],len[MAXN];
	segtree(int t):n(t){
		for(int i = 1;i <= t; i++)
			cnt[i] = len[i] = 0;
	};
	void update(int t,int l,int r);
	void inc_seg(int t,int l0,int r0,int l,int r);
	void dec_seg(int t,int l0,int r0,int l,int r);
	int seg_len(int t,int l0,int r0,int l,int r);
};

int length(int l,int r){
	return r - l;
}

void segtree::update(int t,int l,int r){
	if(cnt[t] || r-l==1)
		len[t] = length(l,r);
	else
		len[t] = len[t<<1]+len[(t<<1) + 1];
}

void segtree::inc_seg(int t,int l0,int r0,int l,int r){
	if (l0==l&&r0==r)
		cnt[t]++;
	else{
		int m0 = (l0 + r0)>>1;
		if(l < m0)
			inc_seg(t<<1,l0,m0,l,m0<r?m0:r);
		if(r > m0)
			inc_seg((t<<1)+1,m0,r0,m0>l?m0:l,r);
		if(cnt[t<<1]&&cnt[(t<<1)+1]){
			cnt[t<<1]--;
			update(t+t,l0,m0);
            cnt[t+t+1]--;
			update(t+t+1,m0,r0);
			cnt[t]++;
		}
	}
	update(t,l0,r0);
}

void segtree::dec_seg(int t,int l0,int r0,int l,int r){
	if (l0==l&&r0==r)
		cnt[t]--;
	else if (cnt[t]){
		cnt[t]--;
		if (l>l0)
			inc_seg(t,l0,r0,l0,l);
		if (r<r0)
			inc_seg(t,l0,r0,r,r0);
	}
	else{
		int m0=(l0+r0)>>1;
		if (l<m0)
			dec_seg(t+t,l0,m0,l,m0<r?m0:r);
		if (r>m0)
			dec_seg(t+t+1,m0,r0,m0>l?m0:l,r);
	}
	update(t,l0,r0);
}

int segtree::seg_len(int t,int l0,int r0,int l,int r){
	if (cnt[t]||(l0==l&&r0==r))
		return len[t];
	else{
		int m0=(l0+r0)>>1,ret=0;
		if (l<m0)
			ret+=seg_len(t+t,l0,m0,l,m0<r?m0:r);
		if (r>m0)
			ret+=seg_len(t+t+1,m0,r0,m0>l?m0:l,r);
		return ret;
	}
}*/
class A{
public:
	int a;
};

class B:public A{
public:
	int a;
};

int get(char c){
	switch(c){
	case 'a':;
	case 'e':;
	case 'i':;
	case 'u':;
	case 'o':
			break;
	default:
		return 1;
	}
	return 0;
}

char str[1000000 + 2];
int main(){
	int t;
	int n;
	int len= 0;
	int mid,sum;
	__int64 res = 0;
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out1.txt","w",stdout);
    scanf("%d",&t);
	for(int k = 1; k <= t; k++){
		scanf("%s %d",str,&n);
		len = strlen(str);
		res = 0;
		for(int i = 0; i < len - n + 1; i++){
			sum = 0;
			for(int j = i; j < len; j++){
				if(get(str[j]))
					sum++;
				else
					sum = 0;
				if(sum >= n){
					res += len - j;
					break;
				}
			}
		}
		printf("Case #%d: %d\n",k,res);
	}
}