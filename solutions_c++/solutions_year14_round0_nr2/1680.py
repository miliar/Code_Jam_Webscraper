#include <cstdio>
#include <cstring>
#include <map>
#include <vector>
#include <queue>
#include <string>
#include <iostream>
#include <unordered_map>
using namespace std;

const int N = 4;
double c, f, x;

int main()
{
    freopen("C:\\Users\\Administrator\\Desktop\\B-large.in", "r", stdin);
    freopen("C:\\Users\\Administrator\\Desktop\\1.out", "w", stdout);
    int T; scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        printf("Case #%d: ", t);
        scanf("%lf %lf %lf", &c, &f, &x);
        double pro = 2.f, res = 0.f;
        while (true) {
        	if ((c / pro + x / (pro + f)) < x / pro) {
        		res += c / pro;
        		pro += f;
        	} else {
        		res += x / pro;
        		printf("%.7lf\n", res);
        		break;
        	}
        }
    }
    return 0;
}
