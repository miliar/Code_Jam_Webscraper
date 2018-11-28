#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
typedef struct array
{
	int val, sign;
}array;
array f(array c1, array c2)
{
	array mod;
	if(c1.val=='1' && c2.val=='1'){mod.val='1';mod.sign='+';}
	if(c1.val=='1' && c2.val=='i'){mod.val='i';mod.sign='+';}
	if(c1.val=='1' && c2.val=='j'){mod.val='j';mod.sign='+';}
	if(c1.val=='1' && c2.val=='k'){mod.val='k';mod.sign='+';}
	if(c1.val=='i' && c2.val=='1'){mod.val='i';mod.sign='+';}
	if(c1.val=='i' && c2.val=='i'){mod.val='1';mod.sign='-';}
	if(c1.val=='i' && c2.val=='j'){mod.val='k';mod.sign='+';}
	if(c1.val=='i' && c2.val=='k'){mod.val='j';mod.sign='-';}
	if(c1.val=='j' && c2.val=='1'){mod.val='j';mod.sign='+';}
	if(c1.val=='j' && c2.val=='i'){mod.val='k';mod.sign='-';}
	if(c1.val=='j' && c2.val=='j'){mod.val='1';mod.sign='-';}
	if(c1.val=='j' && c2.val=='k'){mod.val='i';mod.sign='+';}
	if(c1.val=='k' && c2.val=='1'){mod.val='k';mod.sign='+';}
	if(c1.val=='k' && c2.val=='i'){mod.val='j';mod.sign='+';}
	if(c1.val=='k' && c2.val=='j'){mod.val='i';mod.sign='-';}
	if(c1.val=='k' && c2.val=='k'){mod.val='1';mod.sign='-';}
//	printf("%c%c %c%c %c%c\n", c1.sign, c1.val, c2.sign, c2.val, mod.sign, mod.val);

	if(c2.sign=='-' && mod.sign=='-')mod.sign='+';
	else if(c2.sign=='-' && mod.sign=='+')mod.sign='-';
	else if(c1.sign=='-' && mod.sign=='-')mod.sign='+';
	else if(c1.sign=='-' && mod.sign=='+')mod.sign='-';
//	printf("%c%c %c%c %c%c\n", c1.sign, c1.val, c2.sign, c2.val, mod.sign, mod.val);
	return mod;
}
int tree[1000000], arr[120005];
void build_tree(int node, int a, int b) {
	if(a > b) return; // Out of range
	if(a == b) { // Leaf node
		tree[node] = arr[a]; // Init value
		return;
	}
	build_tree(node*2, a, (a+b)/2); // Init left child
	build_tree(node*2+1, 1+(a+b)/2, b); // Init right child
	tree[node] = tree[node*2]+tree[node*2+1]; // Init root value
}
int query_tree(int node, int a, int b, int i, int j) {
	if(a > b || a > j || b < i) return 0; // Out of range
	if(a >= i && b <= j) // Current segment is totally within range [i, j]
		return tree[node];
	int q1 = query_tree(node*2, a, (a+b)/2, i, j); // Query left child
	int q2 = query_tree(1+node*2, 1+(a+b)/2, b, i, j); // Query right child
	int res = q1+q2; // Return final result
	return res;
}

int main()
{
	int t;
	scanf("%d", &t);
	for(int q=1;q<=t;q++)
	{
		for(int i=0;i<1000000;i++)tree[i]=0;
		for(int i=0;i<120005;i++)arr[i]=0;
		int l, x;
		scanf("%d%d", &l ,&x);
		x=min(x,12);
		char in[10005], s[120005];
		s[0]='\0';
		scanf("%s", in);
		for(int i=0;i<x;i++)strcat(s,in);
//		printf("%s\n", s);
		int start[120005]={0}, end[120005]={0};
		l=strlen(s);
		array cur={'1','+'};
		for(int i=0;i<l;i++)
		{
			array tem={s[i],'+'};
//			printf("%c%c %c%c\n", cur.sign, cur.val, tem.sign, tem.val);
			cur = f(cur,tem);
			if(cur.val=='i' && cur.sign=='+')start[i]=1;
		}
		cur.val='1';cur.sign='+';
		for(int i=l-1;i>=0;i--)
		{
			array tem={s[i],'+'};
			cur = f(tem,cur);
			if(cur.val=='i' && cur.sign=='+')end[i]=1;
		}
		cur.val='1';cur.sign='+';
		for(int i=l-1;i>=0;i--)
		{
			array tem={s[i],'+'};
			cur = f(tem,cur);
			if(cur.val=='k' && cur.sign=='+')arr[i]=1;
		}
//		for(int i=0;i<l;i++)printf("%d ", start[i]);
//		printf("\n");
//		for(int i=0;i<l;i++)printf("%d ", end[i]);
//		printf("\n");
//		for(int i=0;i<l;i++)printf("%d ", arr[i]);
//		printf("\n");
		build_tree(1,0,l-1);
		int flag=0;
		for(int i=0;i<l-1;i++)
		{
			if(start[i] && end[i+1])
				if(query_tree(1,0,l-1,i+1,l-1)>0)
				{
					flag=1;
					break;
				}
		}
		if(flag)printf("Case #%d: YES\n", q);
		else printf("Case #%d: NO\n", q);
	}
	return 0;
}
