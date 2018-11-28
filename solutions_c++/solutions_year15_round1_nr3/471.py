#include <iostream>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <vector>
#include <math.h>
#include <queue>

using namespace std;

#include <stdlib.h>
#define eps 1e-8
#define zero(x) (((x)>0?(x):-(x))<eps)
struct point{double x,y;};

//计算cross product (P1-P0)x(P2-P0)
double xmult(point p1,point p2,point p0){
	return (p1.x-p0.x)*(p2.y-p0.y)-(p2.x-p0.x)*(p1.y-p0.y);
}
//graham算法顺时针构造包含所有共线点的凸包,O(nlogn)
point p1,p2;
int graham_cp(const void* a,const void* b){
	double ret=xmult(*((point*)a),*((point*)b),p1);
	return zero(ret)?(xmult(*((point*)a),*((point*)b),p2)>0?1:-1):(ret>0?1:-1);
}
void _graham(int n,point* p,int& s,point* ch){
	int i,k=0;
	for (p1=p2=p[0],i=1;i<n;p2.x+=p[i].x,p2.y+=p[i].y,i++)
		if (p1.y-p[i].y>eps||(zero(p1.y-p[i].y)&&p1.x>p[i].x))
			p1=p[k=i];
	p2.x/=n,p2.y/=n;
	p[k]=p[0],p[0]=p1;
	qsort(p+1,n-1,sizeof(point),graham_cp);
	for (ch[0]=p[0],ch[1]=p[1],ch[2]=p[2],s=i=3;i<n;ch[s++]=p[i++])
		for (;s>2&&xmult(ch[s-2],p[i],ch[s-1])<-eps;s--);
}

//构造凸包接口函数,传入原始点集大小n,点集p(p原有顺序被打乱!)
//返回凸包大小,凸包的点在convex中
//参数maxsize为1包含共线点,为0不包含共线点,缺省为1
//参数clockwise为1顺时针构造,为0逆时针构造,缺省为1
//在输入仅有若干共线点时算法不稳定,可能有此类情况请另行处理!
//不能去掉点集中重合的点
int graham(int n,point* p,point* convex,int maxsize=1,int dir=1){
	point* temp=new point[n];
	int s,i;
	_graham(n,p,s,temp);
	for (convex[0]=temp[0],n=1,i=(dir?1:(s-1));dir?(i<s):i;i+=(dir?1:-1))
		if (maxsize||!zero(xmult(temp[i-1],temp[i],temp[(i+1)%s])))
			convex[n++]=temp[i];
	delete []temp;
	return n;
}

struct line{point a,b;};


double xmult(double x1,double y1,double x2,double y2,double x0,double y0){
	return (x1-x0)*(y2-y0)-(x2-x0)*(y1-y0);
}

//计算dot product (P1-P0).(P2-P0)
double dmult(point p1,point p2,point p0){
	return (p1.x-p0.x)*(p2.x-p0.x)+(p1.y-p0.y)*(p2.y-p0.y);
}
double dmult(double x1,double y1,double x2,double y2,double x0,double y0){
	return (x1-x0)*(x2-x0)+(y1-y0)*(y2-y0);
}

//两点距离
double distance(point p1,point p2){
	return sqrt((p1.x-p2.x)*(p1.x-p2.x)+(p1.y-p2.y)*(p1.y-p2.y));
}
double distance(double x1,double y1,double x2,double y2){
	return sqrt((x1-x2)*(x1-x2)+(y1-y2)*(y1-y2));
}

//判三点共线
int dots_inline(point p1,point p2,point p3){
	return zero(xmult(p1,p2,p3));
}
int dots_inline(double x1,double y1,double x2,double y2,double x3,double y3){
	return zero(xmult(x1,y1,x2,y2,x3,y3));
}

//判点是否在线段上,包括端点
int dot_online_in(point p,line l){
	return zero(xmult(p,l.a,l.b))&&(l.a.x-p.x)*(l.b.x-p.x)<eps&&(l.a.y-p.y)*(l.b.y-p.y)<eps;
}
int dot_online_in(point p,point l1,point l2){
	return zero(xmult(p,l1,l2))&&(l1.x-p.x)*(l2.x-p.x)<eps&&(l1.y-p.y)*(l2.y-p.y)<eps;
}
int dot_online_in(double x,double y,double x1,double y1,double x2,double y2){
	return zero(xmult(x,y,x1,y1,x2,y2))&&(x1-x)*(x2-x)<eps&&(y1-y)*(y2-y)<eps;
}

typedef long long LL;

void checkmin(int &a, int b) {
	a = min(a, b);
}

int main() {
	freopen("C:/Users/dd/Downloads/C-small-attempt0.in", "r", stdin);
	freopen("C:/Users/dd/Downloads/C-small-attempt0.out", "w", stdout);

	int cas;
	cin >> cas;
	for (int te = 1; te <= cas; te ++) {
		int n;
		point p[555], con[555], tmp[555];
		cin >> n;
		for (int i = 0; i < n; i ++) {
			cin >> p[i].x >> p[i].y;
		}
		
		printf("Case #%d:\n", te);
		
		int mi[55];
		for (int i = 0; i < n; i ++) {
			mi[i] = n - 1;
		}
		for (int s = 0; s < (1 << n); s ++) {
				int ind = 0;
				vector<int> ids; 
				for (int j = 0; j < n; j ++) {
					if (s & (1 << j)) {
						tmp[ind ++] = p[j];
						ids.push_back(j);
					}
				}
				if (ind <= 1) {
					continue;
				}
				//检查共线
				bool gong = false; 
				for (int i = 0; i < ind; i ++) {
					for (int j = i + 1; j < ind; j ++) {
						int c = 0;
						for (int k = 0; k < ind; k ++) {
							if (dot_online_in(tmp[k], tmp[i], tmp[j])) {
								c ++;
							}
						}
						if (c == ind) {
							gong = true;
						}
					}
				}
				if (gong) {
					for (int i = 0; i < ind; i ++) {
						checkmin(mi[ids[i]], n - ind);
					}
					continue;
				}
				point cpy[555];
				memcpy(cpy, tmp, sizeof(cpy));
				//凸包
				int cc = graham(ind, tmp, con);
				/*
				printf("cc = %d, ind = %d\n", cc, ind);
				for (int i = 0; i < cc; i ++) {
					printf("(%lf, %lf) ", con[i].x, con[i].y); 
				} puts("");
				for (int i = 0; i < ind; i ++) {
					printf("(%lf, %lf) ", tmp[i].x, tmp[i].y); 
				} puts(""); */
				for (int k = 0; k < ind; k ++) {
					bool in = false;
					for (int i = 0; i < cc; i ++) {
						if (dot_online_in(cpy[k], con[i], con[(i + 1) % cc])) {
							in = true;
						}
					}
					if (in) {
						checkmin(mi[ids[k]], n - ind);
					}
				}
		}
		
		
		
		
		for (int i = 0; i < n; i ++) {
			printf("%d\n", mi[i]);
		}
	}
}
