#include<stdio.h>
#include<conio.h>

main()
{
  int i,j,t,tc,flag;
  char arr[4][4],ch;
  FILE *fin,*fout;
  
  fin=fopen("A-large.in", "r");
  fout=fopen("output.txt","w");
  fscanf(fin,"%d\n",&tc);
  //printf("--%d--\n",tc);
  
  for(t=1;t<=tc;t++)
  { 
    flag=3;
    for(i=0;i<4;i++)
    {
      for(j=0;j<4;j++)
      {
        fscanf(fin,"%c",&ch);
        if(ch=='.')
          flag=4;
        arr[i][j]= ch;     
      }
      fscanf(fin,"\n");
    }
    
    fscanf(fin,"\n");
    
    for(i=0;i<4;i++)
    {     
        if(
              (arr[i][0]=='X' && arr[i][1]=='X' && arr[i][2]=='X' && arr[i][3]=='X')
            ||(arr[i][0]=='X' && arr[i][1]=='X' && arr[i][2]=='X' && arr[i][3]=='T')
            ||(arr[i][0]=='X' && arr[i][1]=='X' && arr[i][3]=='X' && arr[i][2]=='T')
            ||(arr[i][0]=='X' && arr[i][3]=='X' && arr[i][2]=='X' && arr[i][1]=='T')
            ||(arr[i][3]=='X' && arr[i][1]=='X' && arr[i][2]=='X' && arr[i][0]=='T')
            ||           
              (arr[0][i]=='X' && arr[1][i]=='X' && arr[2][i]=='X' && arr[3][i]=='X')
            ||(arr[0][i]=='X' && arr[1][i]=='X' && arr[2][i]=='X' && arr[3][i]=='T')
            ||(arr[0][i]=='X' && arr[1][i]=='X' && arr[3][i]=='X' && arr[2][i]=='T')
            ||(arr[0][i]=='X' && arr[3][i]=='X' && arr[2][i]=='X' && arr[1][i]=='T')
            ||(arr[3][i]=='X' && arr[1][i]=='X' && arr[2][i]=='X' && arr[0][i]=='T')
                        
           )           
        {  
           flag=1;
           goto lbl; 
        }
        
        if(
           
              (arr[i][0]=='O' && arr[i][1]=='O' && arr[i][2]=='O' && arr[i][3]=='O')
            ||(arr[i][0]=='O' && arr[i][1]=='O' && arr[i][2]=='O' && arr[i][3]=='T')
            ||(arr[i][0]=='O' && arr[i][1]=='O' && arr[i][3]=='O' && arr[i][2]=='T')
            ||(arr[i][0]=='O' && arr[i][3]=='O' && arr[i][2]=='O' && arr[i][1]=='T')
            ||(arr[i][3]=='O' && arr[i][1]=='O' && arr[i][2]=='O' && arr[i][0]=='T')
            ||            
              (arr[0][i]=='O' && arr[1][i]=='O' && arr[2][i]=='O' && arr[3][i]=='O')
            ||(arr[0][i]=='O' && arr[1][i]=='O' && arr[2][i]=='O' && arr[3][i]=='T')
            ||(arr[0][i]=='O' && arr[1][i]=='O' && arr[3][i]=='O' && arr[2][i]=='T')
            ||(arr[0][i]=='O' && arr[3][i]=='O' && arr[2][i]=='O' && arr[1][i]=='T')
            ||(arr[3][i]=='O' && arr[1][i]=='O' && arr[2][i]=='O' && arr[0][i]=='T')
                        
           )           
        {  
           flag=2;
           goto lbl;
        }     
    }
    if(
       
         (arr[0][0]=='X' && arr[1][1]=='X' && arr[2][2]=='X' && arr[3][3]=='X')
       ||(arr[0][0]=='X' && arr[1][1]=='X' && arr[2][2]=='X' && arr[3][3]=='T')
       ||(arr[0][0]=='X' && arr[1][1]=='X' && arr[3][3]=='X' && arr[2][2]=='T')
       ||(arr[0][0]=='X' && arr[3][3]=='X' && arr[2][2]=='X' && arr[1][1]=='T')
       ||(arr[3][3]=='X' && arr[1][1]=='X' && arr[2][2]=='X' && arr[0][0]=='T')
       ||        
         (arr[0][3]=='X' && arr[1][2]=='X' && arr[2][1]=='X' && arr[3][0]=='X')
       ||(arr[0][3]=='X' && arr[1][2]=='X' && arr[2][1]=='X' && arr[3][0]=='T')
       ||(arr[0][3]=='X' && arr[1][2]=='X' && arr[3][0]=='X' && arr[2][1]=='T')
       ||(arr[0][3]=='X' && arr[3][0]=='X' && arr[2][1]=='X' && arr[1][2]=='T')
       ||(arr[3][0]=='X' && arr[1][2]=='X' && arr[2][1]=='X' && arr[0][3]=='T')
       
      )
    {  
        flag=1;
        goto lbl; 
    }
    if(
       
         (arr[0][0]=='O' && arr[1][1]=='O' && arr[2][2]=='O' && arr[3][3]=='O')
       ||(arr[0][0]=='O' && arr[1][1]=='O' && arr[2][2]=='O' && arr[3][3]=='T')
       ||(arr[0][0]=='O' && arr[1][1]=='O' && arr[3][3]=='O' && arr[2][2]=='T')
       ||(arr[0][0]=='O' && arr[3][3]=='O' && arr[2][2]=='O' && arr[1][1]=='T')
       ||(arr[3][3]=='O' && arr[1][1]=='O' && arr[2][2]=='O' && arr[0][0]=='T')
       ||       
         (arr[0][3]=='O' && arr[1][2]=='O' && arr[2][1]=='O' && arr[3][0]=='O')
       ||(arr[0][3]=='O' && arr[1][2]=='O' && arr[2][1]=='O' && arr[3][0]=='T')
       ||(arr[0][3]=='O' && arr[1][2]=='O' && arr[3][0]=='O' && arr[2][1]=='T')
       ||(arr[0][3]=='O' && arr[3][0]=='O' && arr[2][1]=='O' && arr[1][2]=='T')
       ||(arr[3][0]=='O' && arr[1][2]=='O' && arr[2][1]=='O' && arr[0][3]=='T')
    
      )
    {  
        flag=2;
        goto lbl;
    }
     
   lbl:
       if(flag==1)
          fprintf(fout,"Case #%d: X won\n",t);
       if(flag==2)
          fprintf(fout,"Case #%d: O won\n",t);
       if(flag==3)
          fprintf(fout,"Case #%d: Draw\n",t);
       if(flag==4)
          fprintf(fout,"Case #%d: Game has not completed\n",t);
       
  } 
  
  fclose(fin);
  fclose(fout);
 
}

