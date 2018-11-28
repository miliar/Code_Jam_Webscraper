#include <cstdio>

struct node {
	node *son[2], *fa;
	int str, key, size;
}

inline void get_newnode(int v)
{
	node *p = new(node);
	p->key = v;
	p->str = v % MOD;
	p->size = 1;
	p->son[0] = p->son[1] = p->fa = NIL;
	return p;
}

inline void update(node *p)
{
	p->size = p->son[0]->size + 1 + p->son[1]->size;
	p->str = ((p->son[0]->str*fac[1]+p->key)*fac[p->son[1]->size]+p->son[1]->str) % MOD;

inline void rotate(node *p, bool side)
{
	node *q = p->fa;
	q->son[!side] = p->son[side];
	p->son[side] = q;
	p->fa = q->fa;
	q->fa = p;
	update(q);
	update(p);
}

inline void splay(node *p, node *r)
{
	while (p->fa != r) {
		node *q = p->fa;
		bool side1 = (p == q->son[0]);
		if (q->fa == r)
			rotate(p, side1);
		else {
			bool side2 = (q == q->fa->son[0]);
			if (side1 ^ side2) {
				rotate(p, side1);
				rotate(p, side2);
			} else {
				rotate(q, side2);
				rotate(p, side1);
			}
		}
	}
}

inline node *find(node *p, int s)
{
	if (p->son[0]->size >= s)
		return find(p->son[0], s);
	if (p->son[0]->size = s-1) {
		splay(p, root);
		return p;
	}
	return (p->son[1], s-p->son[0]->size-1);
}

inline void modify(int k, int v)
{
	node *p = find(k);
	p->key = v;
	update(p);
}

inline void add(int k, int v)
{
	node *p = find(k);
	node *q = find(k+1);
	splay(p, q);
	q = get_newnode(v);
	p->son[1] = q;
	q->fa = p;
	update(p);
	update(p->fa);
}

inline int query(int l, int r)
{
		
}
