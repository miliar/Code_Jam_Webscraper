#include <iostream> 
#include <sstream> 
#include <vector> 
#include <set> 
#include <map> 
#include <algorithm> 
#include <string> 
#include <cstring> 

using namespace std; 

int ttt, tttt;
int n,i;
int x[2000], y[2000], p[2000], pp[2000];
int ans,s;

struct pt {
	int x, y;
	
	pt(int a, int b):x(a),y(b){}
};
 
inline int area (pt a, pt b, pt c) {
	return (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);
}
 
inline bool intersect_1 (int a, int b, int c, int d) {
	if (a > b)  swap (a, b);
	if (c > d)  swap (c, d);
	return max(a,c) <= min(b,d);
}
 
bool intersect (pt a, pt b, pt c, pt d) {
	return intersect_1 (a.x, b.x, c.x, d.x)
		&& intersect_1 (a.y, b.y, c.y, d.y)
		&& area(a,b,c) * area(a,b,d) <= 0
		&& area(c,d,a) * area(c,d,b) <= 0;
}

void check(){
     p[n] = p[0];
     int i,j;
     s = 0;
     for (i=0;i<n;i++){
         s += (x[p[i]]-x[p[i+1]])*(y[p[i]]+y[p[i+1]]);
     }
     if (s<0) s = -s;
     if (s>ans){
        for (i=0;i<n;i++)
            for (j=i+2;j<n;j++){
                if ((i==0) && (j+1 == n)) continue;
                
                if (intersect(pt(x[p[i]],y[p[i]]),pt(x[p[i+1]],y[p[i+1]]), pt(x[p[j]],y[p[j]]),pt(x[p[j+1]],y[p[j+1]]))) return ;
            }
        ans = s;
        for (i=0;i<n;i++)
            pp[i] = p[i];
     }
     
}

void gen(int v){
     if (v == n){
           check();
           return ;
        }
     int i;
     for (i=v;i<n;i++){
         swap(p[v], p[i]);
         gen(v+1);
         swap(p[v], p[i]);
     }
}

int main(){
    freopen("b1.dat","r",stdin);
    freopen("b1.sol","w",stdout);
    cin >> ttt;
    for (tttt=1;tttt<=ttt;tttt++){
        cout << "Case #" << tttt << ": ";
        
        cin >> n;
        for (i=0;i<n;i++) {
            cin >> x[i] >> y[i];
            p[i] = i;
        }
        
        ans = 0;
        
        gen(0);
        
        for (i=0;i<n;i++) {
            cout << pp[i];
            if (i<n-1) cout << " "; else cout << endl;
        }
        
    }
//    system("pause");
    return 0;
}

 
