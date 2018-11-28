#include <iostream>
#include <fstream>
#include <sstream>
#include <cstring>
#include <string>

#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>

using namespace std;

int main(int argc, char * argv[])
{
    int t;
    scanf("%d", &t);
    while (t--) {
        int x;
        scanf("%d", &x);
        int xrow[4];
        for(int i = 0; i < 4; ++i)
        {
            int a,b,c,d;
            scanf("%d %d %d %d", &a, &b, &c, &d);
            if(i+1 == x) {
                xrow[0] = a; xrow[1] = b;
                xrow[2] = c; xrow[3] = d;
            }
        }
//        printf("1row: %d, %d, %d, %d\n", xrow[0],xrow[1],xrow[2],xrow[3]);
        sort(xrow, xrow+4);
//        printf("1row sorted : %d, %d, %d, %d\n", xrow[0],xrow[1],xrow[2],xrow[3]);
        int y;
        scanf("%d", &y);
        int yrow[4];
        for(int i = 0; i < 4; ++i)
        {
            int a,b,c,d;
            scanf("%d %d %d %d", &a, &b, &c, &d);
            if(i+1 == y) {
                yrow[0] = a; yrow[1] = b;
                yrow[2] = c; yrow[3] = d;
            }
        }
//        printf("2row: %d, %d, %d, %d\n", yrow[0],yrow[1],yrow[2],yrow[3]);
        sort(yrow, yrow+4);
//        printf("2row sorted: %d, %d, %d, %d\n", yrow[0],yrow[1],yrow[2],yrow[3]);
        vector<int> v(8);
        vector<int>::iterator it;
        it = set_intersection(xrow, xrow+4, yrow, yrow+4, v.begin());
        v.resize(it-v.begin());
//        printf("intersection size = %lu\n", v.size());
        static int id = 0;
        printf("Case #%d: ",++id);
        switch (v.size()) {
            case 0:
                printf("Volunteer cheated!\n");
                break;
            case 1:
                printf("%d\n", *v.begin());
                break;
            default:
                printf("Bad magician!\n");
                break;
        }
    }
    return 0;
}
