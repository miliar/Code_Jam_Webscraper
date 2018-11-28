#include <cstdio>

int lawn[100][100];

bool check_row(int height, int x, int m)
{
     for(int i=0;i<m;++i)
             if(lawn[x][i]>height)
             {
                            // printf("FALSE: %d %d\n",x,y);
                             return false;
             }
             return true;
}

bool check_column(int height, int y, int n)
{
     for(int i=0;i<n;++i)
             if(lawn[i][y]>height)
             {
                             //printf("FALSE: %d %d\n",x,y);
                             return false;
             }
             return true;
}

bool check_square(int x, int y, int n, int m)
{
     //n x m- size of the garden
     //x, y - coordinates of particular square
     int h=lawn[x][y];
     bool row=check_row(h,x,m);
     bool column=check_column(h,y,n);
     if(row || column)
            return true;
     return false;
}

bool check_pattern(int n, int m)
{
     for(int i=0;i<n;++i)
             for(int j=0;j<m;++j)
                     if(!check_square(i,j,n,m))
                     {
                                               printf("FALSE: %d %d\n",i,j);
                                               return false;
                     }
     return true;
}

int main()
{
    FILE *fwrite=fopen("output.txt","w");
    FILE *fread=fopen("B-large.in","r");
    
    
    int tests;
    fscanf(fread,"%d", &tests);
    int n,m;  //size of the lawn
    for(int i=0;i<tests;++i)
    {
            fscanf(fread,"%d", &n);
            fscanf(fread,"%d", &m);
            
            for(int ii=0;ii<n;ii++)
                   for(int jj=0;jj<m;jj++)
                            fscanf(fread, "%d", &lawn[ii][jj]);
            bool result=check_pattern(n,m);
            if(result)
                      fprintf(fwrite, "Case #%d: YES\n",i+1);
            else
                fprintf(fwrite, "Case #%d: NO\n",i+1);
            
    }

        
    fclose(fwrite);
    fclose(fread);
    return 0;
}
