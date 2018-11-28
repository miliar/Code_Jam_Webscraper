#include <iostream>
#include <cstring>
#include <climits>
#include <vector>
using namespace std;

int main()
{
    int t, n, k, x, y, a[5][5], b[5][5], res = 0;
	FILE *fp=fopen("in.txt", "r"), *ofp=fopen("out.txt", "w");
    fscanf(fp, "%d", &t);
    for(int k = 1; k <= t; k++) {
        int m[17] = {0}, c = 0;
        fscanf(fp, "%d", &x);
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                fscanf(fp, "%d", &a[i][j]);
        fscanf(fp, "%d", &y);
        for(int i = 0; i < 4; i++)
            for(int j = 0; j < 4; j++)
                fscanf(fp, "%d", &b[i][j]);
                
        x--;y--;                
        for(int i = 0; i< 4; i++)
            m[a[x][i]]++;
        for(int i = 0; i < 4; i++) {
            if(m[b[y][i]] == 1) {
                c++;
                res = b[y][i];   
            }
        }
        if(c == 0)
            fprintf(ofp, "Case #%d: Volunteer cheated!\n", k); 
        else if (c == 1)
            fprintf(ofp, "Case #%d: %d\n", k, res); 
        else 
            fprintf(ofp, "Case #%d: Bad magician!\n", k); 
    }
    fclose(fp);
    fclose(ofp);
    system("pause");
    return 0;
}
