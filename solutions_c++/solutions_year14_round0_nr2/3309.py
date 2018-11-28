#include<fstream>
#include<iostream>

using namespace std;

int main()
{
    int t,case_no = 0;
    FILE *in = fopen("C:\\Users\\Rizaraf\\Desktop\\input.in", "r");
    FILE *out = fopen("C:\\Users\\Rizaraf\\Desktop\\output.txt", "w");
    fscanf(in, "%d", &t);
    while(t--)
    {
        case_no++;
        int ans1, ans2, a[4][4], b[4][4], temp, count = 0, i, j ;
        fscanf(in, "%d", &ans1);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fscanf(in, "%d", &a[i][j]);
            }
        }
        fscanf(in, "%d", &ans2);
        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                fscanf(in, "%d", &b[i][j]);
            }
        }

        for(i=0;i<4;i++)
        {
            for(j=0;j<4;j++)
            {
                if(a[ans1-1][i]==b[ans2-1][j])
                {
                    count++;
                    temp = a[ans1-1][i];
                }
            }
        }
        if(count==0)
        {
            fprintf(out, "Case #%d: Volunteer cheated!\n", case_no);
        }
        else if(count==1)
        {
            fprintf(out, "Case #%d: %d\n", case_no,temp);
        }
        else
        {
            fprintf(out, "Case #%d: Bad magician!\n", case_no);
        }
    }

    return 0;
}
