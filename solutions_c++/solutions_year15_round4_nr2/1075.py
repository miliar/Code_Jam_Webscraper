#include<cstdio>
#include<cstring>
#include<set>
#include<map>
#include<vector>
#include<algorithm>
#include<iostream>
#include<cmath>

using namespace std;

const int N = 110;
typedef double real;
struct vec2{
    real x, y;
    vec2(real x=0.0, real y=0.0):x(x), y(y){}
    vec2 operator+(const vec2 &b)const{ return vec2(x+b.x, y+b.y);}
    vec2 operator-(const vec2 &b)const{ return vec2(x-b.x, y-b.y);}
    vec2 operator*(const real &b)const{ return vec2(x*b, y*b);}
	vec2 operator/(const real &b)const{ return vec2(x/b, y/b);} real operator*(const vec2 &b)const{ return x*b.x + y*b.y;}
    real operator^(const vec2 &b)const{ return x*b.y - y*b.x;}
    real len(){return sqrt(x*x+y*y);}
    vec2 unit(){ return *this/len();}
    vec2 rotate(real r){vec2 t(sin(r), cos(r));return vec2(*this ^ t, *this * t);}
};
double eps = 1e-8;
struct NODE{
    double v, t;
    bool operator<(const NODE &b) const{
	return t < b.t;
    }
}a[N*2];
int n;
double v, t;

double cal(vec2 a, vec2 b, vec2 t){
    if (b.x < 0){
	a = a + b;
	b = vec2(0, 0) - b;
    }
    double sum = 0;
    if (a.x > 0 && abs(a.y / a.x - t.y / t.x) < eps) sum += a.x;
    if (b.x > 0 && abs(b.y / b.x - t.y / t.x) < eps) sum += b.x;
    if (sum > eps) return t.x / sum;
    if ((a ^ t) * (t ^ b) >= 0){
    double va = (a.x * b.y) - (a.y * b.x);
    double vb = (t.x * b.y) - (t.y * b.x);
    double vc = (a.x * t.y) - (a.y * t.x);
    if (va > 0) return max(abs(vb / va), abs(vc / va));
    }
    return 1e10;
}
double gao(){
    cin >> n >> v >> t;
    for (int i=0; i<n; ++i){
	cin >> a[i].v >> a[i].t;
    }
    sort(a, a+n);
    for (int i=0; i<n; ++i){
	a[i+n].v = -a[i].v;
	a[i+n].t = a[i].t;
    }
    if (a[n-1].t < t || a[0].t > t) return -1;
    double ans = 1e10;
    vec2 cur;
    vec2 tar = vec2(v, v*t);
    for (int i=0; i<n*2; ++i){
	vec2 nxt = cur + vec2(a[i].v, a[i].v*a[i].t);
	ans = min(ans, cal(cur, nxt-cur, tar));
	cur = nxt;
    }
    return ans;
}

int main(){
    int T;
    cin >> T;
    for (int i=1; i<=T; ++i){
	printf("Case #%d: ", i);
	double ans = gao();
	if (ans < 0){
	    puts("IMPOSSIBLE");
	}else{
	    printf("%.12lf\n", ans);
	}

    }
    return 0;
}
