#include <bits/stdc++.h>

using namespace std;

const double eps = 1e-8;

const double eps2 = 1e-15;

int dcmp(double x)
{
    if(fabs(x)<eps)
        return 0;
    if(x<0)
        return -1;
    return 1;
}

int dcmp2(double x)
{
    if(fabs(x)<eps2)
        return 0;
    if(x<0)
        return -1;
    return 1;
}

double v[110],r[110],W,X;

int n;

struct Point
{
    double x,y;
    Point() {}
    Point(double _x,double _y)
    {
        x=_x;
        y=_y;
    }
    Point operator -(const Point &b)const {
        return Point(x-b.x,y-b.y);
    }
    double operator *(const Point &b)const {
        return x*b.y-y*b.x;
    }
}a[210],ans[210];

int xmulti(Point p1,Point p2,Point p3)
{
    return dcmp((p1-p3)*(p2-p3));
}

double CalcArea(Point p[],int nn)
{
	double res = 0;
	for (int i = 0;i < nn;i++)
		res += (p[i]*p[(i+1)%nn])/2;
	return res;
}

bool cmp(Point p1,Point p2)
{
    if(dcmp(p1.y-p2.y)!=0)
        return p1.y<p2.y;
    return p1.x<p2.x;
}

bool check(double res)
{
    for(int i=1;i<=n;i++) {
        a[i].x=v[i]*res;
        a[i].y=v[i]*res*r[i];
    }
    a[0]=Point(0.0,0.0);
    int m=n+1;

    sort(a,a+m,cmp);
    int top=0;
    for(int i=0;i<m;i++) {
        while(top>1&&xmulti(a[i],ans[top-1],ans[top-2])>=0)
            top--;
        ans[top++]=a[i];
    }
    int len=top;
    for(int i=m-2;i>=0;i--) {
        while(top>len&&xmulti(a[i],ans[top-1],ans[top-2])>=0)
            top--;
        ans[top++]=a[i];
    }
    top--;
    double res1=CalcArea(ans,top);
    if(dcmp(res1)==0) {
        for(int i=1;i<=n;i++) {
            if(dcmp(v[i]*res-W)>=0&&dcmp(r[i]*W-X)==0)
                return true;
        }
        return false;
    }
    a[m++]=Point(a[1].x+a[2].x,a[1].y+a[2].y);

    sort(a,a+m,cmp);
/*
    printf("fuck %.15f\n",res);
    for(int i=0;i<m;i++)
        printf("%d %.15f %.15f\n",i,a[i].x,a[i].y);
    printf("%d %.15f %.15f\n",m,W,X);
*/
    top=0;
    for(int i=0;i<m;i++) {
        while(top>1&&xmulti(a[i],ans[top-1],ans[top-2])>=0)
            top--;
        ans[top++]=a[i];
    }
    len=top;
    for(int i=m-2;i>=0;i--) {
        while(top>len&&xmulti(a[i],ans[top-1],ans[top-2])>=0)
            top--;
        ans[top++]=a[i];
    }
    top--;
    res1=CalcArea(ans,top);
    a[m++]=Point(W,X);
    sort(a,a+m,cmp);
    top=0;
    for(int i=0;i<m;i++) {
        while(top>1&&xmulti(a[i],ans[top-1],ans[top-2])>=0)
            top--;
        ans[top++]=a[i];
    }
    len=top;
    for(int i=m-2;i>=0;i--) {
        while(top>len&&xmulti(a[i],ans[top-1],ans[top-2])>=0)
            top--;
        ans[top++]=a[i];
    }
    top--;
    double res2=CalcArea(ans,top);
    //printf("%.15f %.15f\n",res1,res2);

    if(dcmp2(res1-res2)==0)
        return true;
    return false;
}

int main()
{
    freopen("B-small-attempt4.in","r",stdin);
    freopen("B-small-attempt4.out","w",stdout);
    int T,cas=0;
    scanf("%d",&T);
    while(T--) {
        scanf("%d%lf%lf",&n,&W,&X);
        X*=W;
        for(int i=1;i<=n;i++)
            scanf("%lf%lf",&v[i],&r[i]);
        double low=0.0f,high=1e10,mid;
        for(int times=1;times<=200;times++) {
            mid=(low+high)/2.0;
            if(check(mid))
                high=mid;
            else
                low=mid;
        }
        if(dcmp(high-1e10)>=0)
            printf("Case #%d: IMPOSSIBLE\n",++cas);
        else
            printf("Case #%d: %.10f\n",++cas,high);
    }
    return 0;
}
