#include <iostream>
#include <string>
#include <cmath>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

int n, s;
int t;

struct unif {
    int uni[1010];
    unif(){
        for (int i = 0; i < n; i++)
            uni[i] = i;
        }
    int find(int i){
        if (uni[i] == i)
            return i;
        else return uni[i] = find(uni[i]);
        }
    void unite(int i, int j){
        uni[find(i)] = uni[find(j)];
        }
    };


struct pnt{
    int x, y, z;

    int dist2(pnt &a){
        return (a.x-x)*(a.x-x) + (a.y-y)*(a.y-y) + (a.z-z)*(a.z-z);
        }
    };

pnt p[1010];

struct edge{
    int a, b;
    int w;
    edge(){}
    edge(int a, int b, int w) : a(a), b(b),w(w){}
    int operator < (const edge & that) const {
        return w < that.w;
        }
    };

edge e[1000010];
int ec;

int main()
{
    int tc;
    std::cin >> tc;
    for(int tn = 1; tn <= tc; tn++){
        std::cin >> n >> s;
        ec = 0;
        for (int i = 0; i < n; i++){
            std::cin >> p[i].x >> p[i].y >> p[i].z;
            std::cin >> t >> t >> t;
            for(int j = 0; j < i; j++)
                e[ec++] = edge(i, j, p[i].dist2(p[j]));
            }
        std::sort(e, e+ec);
        unif u;
        int a = -1;
        while(u.find(0) != u.find(1)){
            ++a;
            u.unite(e[a].a, e[a].b);
            }
        std::cout << "Case #" << tn << ": " << sqrt(e[a].w) << std::endl;
        }
    return 0;
}
