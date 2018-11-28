#include <stdio.h>
int main()
{
    FILE *fp1,*fp2;
    fp1=fopen("tttl.in","r");
    fp2=fopen("tttl.out","w");
    int tstcs;
    fscanf(fp1,"%d",&tstcs);
    int q,i,j,ii,c,cc,qq;
    char b[4][5];
    for(q=0;q<tstcs;q++)
    {
        cc=1;
        for(i=0;i<4;i++)
        {
              fscanf(fp1,"%s",b[i]);
              if(i<3)
                 fscanf(fp1,"\n");
        }
        for(i=0;i<4;i++)
        {
           
           qq=0;
           c=1;
           while(b[i][qq]=='.'||b[i][qq]=='T')
              qq++;
           if(qq>3)
              continue;
           if(b[i][qq]=='X')
           {
              for(j=0;j<4;j++)
                 if(b[i][j]=='O'||b[i][j]=='.')
                    c=0;
              if(c==1)
              {
                 cc=0;
                 fprintf(fp2,"Case #%d: X won\n",q+1);
                 break;
              }
           }
           else if(b[i][qq]=='O')
           {
              for(j=0;j<4;j++)
                 if(b[i][j]=='X'||b[i][j]=='.')
                    c=0;
              if(c==1)
              {
                 cc=0;
                 fprintf(fp2,"Case #%d: O won\n",q+1);
                 break;
              }
           }
        }
        if(cc==0)
           continue;
        for(i=0;i<4;i++)
        {
           qq=0;
           c=1;
           while(b[qq][i]=='.'||b[qq][i]=='T')
              qq++;
           if(qq>3)
              continue;
           if(b[qq][i]=='X')
           {
              for(j=0;j<4;j++)
                 if(b[j][i]=='O'||b[j][i]=='.')
                    c=0;
              if(c==1)
              {
                 cc=0;
                 fprintf(fp2,"Case #%d: X won\n",q+1);
                 break;
              }
           }
           else if(b[qq][i]=='O')
           {
              for(j=0;j<4;j++)
                 if(b[j][i]=='X'||b[j][i]=='.')
                    c=0;
              if(c==1)
              {
                 cc=0;
                 fprintf(fp2,"Case #%d: O won\n",q+1);
                 break;
              }
           }
        }
        if(cc==0)
           continue;
        if((b[0][0]=='X'||b[0][0]=='T')&&(b[1][1]=='X'||b[1][1]=='T')&&(b[2][2]=='X'||b[2][2]=='T')&&(b[3][3]=='X'||b[3][3]=='T'))
        {
            fprintf(fp2,"Case #%d: X won\n",q+1);   
            cc=0;
            continue;
        }         
        else if((b[3][0]=='X'||b[3][0]=='T')&&(b[2][1]=='X'||b[2][1]=='T')&&(b[1][2]=='X'||b[1][2]=='T')&&(b[0][3]=='X'||b[0][3]=='T'))
        {
            fprintf(fp2,"Case #%d: X won\n",q+1);   
            cc=0;
            continue;
        } 
        else if((b[0][0]=='O'||b[0][0]=='T')&&(b[1][1]=='O'||b[1][1]=='T')&&(b[2][2]=='O'||b[2][2]=='T')&&(b[3][3]=='O'||b[3][3]=='T'))
        {
           cc=0;
           fprintf(fp2,"Case #%d: O won\n",q+1); 
           continue;
        }
        else if((b[3][0]=='O'||b[3][0]=='T')&&(b[2][1]=='O'||b[2][1]=='T')&&(b[1][2]=='O'||b[1][2]=='T')&&(b[0][3]=='O'||b[0][3]=='T'))
        {
            fprintf(fp2,"Case #%d: O won\n",q+1);   
            cc=0;
            continue;
        }
        if(cc==1)
        for(i=0;i<4;i++)
        {
           for(j=0;j<4;j++)
              if(b[i][j]=='.')
              {
                 fprintf(fp2,"Case #%d: Game has not completed\n",q+1);
                 cc=0;
                 break;
              }
           if(cc==0)
              break;
        }
         if(cc==1)  
            fprintf(fp2,"Case #%d: Draw\n",q+1);  
    }
    fclose(fp1);
    fclose(fp2);
    scanf(" ");
    return 0;   
}
