#include <cstdio>
#include <string>
using namespace std;

int t, n, r, p, s;
int precalc[13][3] = {{1, 0, 0},};
string dp[13][3] = {{"R", "P", "S"},};

int main(void) {
    for (int i = 1; i <= 12; i++)
        for (int j = 0; j < 3; j++)
            precalc[i][j] = precalc[i-1][j] + precalc[i-1][(j+2)%3];
    
    for (int i = 1; i <= 12; i++)
        for (int j = 0; j < 3; j++) {
            if (dp[i-1][j].compare(dp[i-1][(j+2)%3]) < 0)
                dp[i][j] = dp[i-1][j] + dp[i-1][(j+2)%3];
            else 
                dp[i][j] = dp[i-1][(j+2)%3] + dp[i-1][j];
        }
        
    FILE * input = fopen("input.txt", "r");
    FILE * output = fopen("output.txt", "w");
    fscanf(input, "%d", &t);
    
    for (int tIter = 1; tIter <= t; tIter++) {
        fprintf(output, "Case #%d: ", tIter);
        fscanf(input, "%d%d%d%d", &n, &r, &p, &s);
        
        if (precalc[n][0] == p && precalc[n][1] == r && precalc[n][2] == s) 
            fprintf(output, "%s\n", dp[n][1].c_str());
        else if (precalc[n][0] == r && precalc[n][1] == s && precalc[n][2] == p) 
            fprintf(output, "%s\n", dp[n][0].c_str());
        else if (precalc[n][0] == s && precalc[n][1] == p && precalc[n][2] == r) 
            fprintf(output, "%s\n", dp[n][2].c_str());
        else
            fprintf(output, "IMPOSSIBLE\n");
    }
    fclose(input);
    fclose(output);
    return 0;
}