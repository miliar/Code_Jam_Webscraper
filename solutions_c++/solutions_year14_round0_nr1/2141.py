#include<cstdio>
using namespace std;
int t,k=0;
int n, m, br=0;
int a[4][4], b[4][4], r[4];
void solve(){
    int i,j;
    fscanf(stdin, "%d", &t);
    while(k++<t){
        fscanf(stdin, "%d", &n);
        for(i =0; i <4; i ++)
            for(j =0; j <4; j ++){
                fscanf(stdin, "%d", &a[i][j]);
            }
        fscanf(stdin, "%d", &m);
        for(i =0; i <4; i ++)
            for(j =0; j <4; j ++){
                fscanf(stdin, "%d", &b[i][j]);
            }
        for(i=0;i<4;i++){
            for(j=0;j<4;j++){
                if(a[n-1][i]==b[m-1][j]){
                    br++;
                    r[br]=a[n-1][i];
                }
            }
        }
        if(br<1)fprintf(stdout,"case #%d: Volunteer cheated!\n", k);
        else if(br>1)fprintf(stdout, "case #%d: Bad magician!\n", k);
        else fprintf(stdout, "case #%d: %d\n", k, r[br]);
        br=0;
    }
}
int main()
{
    solve();
    return 0;
}