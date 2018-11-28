#include <iostream>
#include <cstring>
#include <climits>
#include <vector>
using namespace std;

int main()
{
    int t;
	FILE *fp=fopen("in.txt", "r"), *ofp=fopen("out.txt", "w");
    fscanf(fp, "%d", &t);
    for(int k = 1; k <= t; k++) {
        double r = 2.0, y, z, c, f, x, res = 0;
        fscanf(fp, "%lf%lf%lf", &c, &f, &x);
        while(true) {
            y = x/r;
            z = c/r + x/(r+f);
            if(y > z) {
                res += c/r;
                r += f;
            } else {
                res += y;
                break;
            }            
        }
        fprintf(ofp, "Case #%d: %lf\n", k, res); 
    }
    fclose(fp);
    fclose(ofp);
    system("pause");
    return 0;
}
