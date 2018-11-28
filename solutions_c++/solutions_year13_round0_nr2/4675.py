#include <cstdlib>
#include <cstdio>
#include <algorithm>

using namespace std;

int T, n, m;
int map[105][105];
int max_r[105];
int max_c[105];


int main()
{
    FILE* reader = fopen("B-large.in", "r");
    FILE* printer = fopen("B-large-out.txt", "w");
    fscanf(reader, "%d", &T);


    for(int case_id=1; case_id<=T; case_id++)
    {
        for(int i=0; i<105; i++)
        {
            max_r[i]=0;
            max_c[i]=0;
        }

        fscanf(reader, "%d %d", &n, &m);
        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
                fscanf(reader, "%d", &map[i][j]);

        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
                max_r[i]=max(max_r[i], map[i][j]);

        for(int j=0; j<m; j++)
            for(int i=0; i<n; i++)
                max_c[j]=max(max_c[j], map[i][j]);


        /*for(int i=0; i<n; i++)
            printf("%d ", max_r[i]);
        printf("\n");

        for(int j=0; j<m; j++)
            printf("%d ", max_c[j]);

        printf("\n\n");*/

        bool doable=true;

        for(int i=0; i<n; i++)
            for(int j=0; j<m; j++)
                if(max_r[i]!=map[i][j] && max_c[j]!=map[i][j])
                    doable=false;

        fprintf(printer, "Case #%d: ", case_id);
        if(doable)
            fprintf(printer, "YES");
        else
            fprintf(printer, "NO");
        fprintf(printer, "\n");

    }

    return 0;
}
