#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <fcntl.h>
#include <errno.h>
#include <unistd.h>
#include <string.h>


    int main()
    {
    int  a[4], b[4],c[4],d[4]; 
    int  row1=0,row2=0, cases, i,j, flag, bad , result, count = 0;
    FILE *fp1,*fp2;
    
    fp1 = fopen("A-small-attempt0.in","r");
    fp2 = fopen("output.out.cpp","w");
    
    fscanf(fp1,"%d",&cases); 
    
    for (int k =0;k<cases;k++)
    {
        flag = 0;bad = 0;result =0;
        count += 1;
        fscanf(fp1,"%d",&row1);
        
        for (i=1;i<=4;i++)
        {
            if ( i == row1)
            {
            fscanf(fp1,"%d",&a[0]); 
            fscanf(fp1,"%d",&a[1]);
            fscanf(fp1,"%d",&a[2]);
            fscanf(fp1,"%d",&a[3]);
            printf("%d %d %d %d\n",a[0],a[1],a[2],a[3]);
            }
            else
            {
            fscanf(fp1,"%d",&c[0]); 
            fscanf(fp1,"%d",&c[1]);
            fscanf(fp1,"%d",&c[2]);
            fscanf(fp1,"%d",&c[3]);
            }
        }
        fscanf(fp1,"%d",&row2);
        
        for ( j=1;j<=4;j++)
        {
            if ( j == row2)
            {
            fscanf(fp1,"%d",&b[0]); 
            fscanf(fp1,"%d",&b[1]);
            fscanf(fp1,"%d",&b[2]);
            fscanf(fp1,"%d",&b[3]);
            printf("%d %d %d %d\n",b[0],b[1],b[2],b[3]);
            }
            else
            {
            fscanf(fp1,"%d",&d[0]); 
            fscanf(fp1,"%d",&d[1]);
            fscanf(fp1,"%d",&d[2]);
            fscanf(fp1,"%d",&d[3]);
            }
        }
        
        
        for ( i = 0; i<4;i++)
        {
            for (j=0; j<4;j++)
            {
                if (a[i] == b[j])
                {
                    if (!flag) 
                    {
                        flag = 1;
                        result = a[i];
                        printf("flag 1\n");
                        break;
                    } 
                    else
                    {
                        fprintf(fp2,"Case #%d: Bad magician!\n",count); 
                        printf("bad 1\n");
                        bad = 1;
                        break;
                    }
                }
                if (bad) break;
            }
            if (bad) break;
        }
        
        if ( !bad && flag ) fprintf(fp2,"Case #%d: %d\n",count,result); 
        else if (!flag)  fprintf(fp2,"Case #%d: Volunteer cheated!\n",count); 
    }
    fclose(fp1);
    fclose(fp2);
    //getchar();
    return 0;
    
    }
