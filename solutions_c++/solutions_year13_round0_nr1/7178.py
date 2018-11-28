#include<iostream.h>
#include<fstream.h>
#include<conio.h>

char A[4][4];

int calc(int r,int c,char a)
{int ff,i,j,k;
 ff=1;
 if(r==1&&c==1)
 {for(i=0;i<4;i++)
    for(j=0;j<4;j++)
      if(i==j)
        if((A[i][j]!=a)&&(A[i][j]!='T'))
         return 0;
  return 1;
 }
 if(r==2&&c==2)
 {for(i=0;i<4;i++)
    for(j=0;j<4;j++)
      if((i+j)==3)
        if((A[i][j]!=a)&&(A[i][j]!='T'))
         return 0;
  return 1;
 }
 if(r==5)
   { for(i=0;i<4;i++)
     if((A[i][c]!=a)&&(A[i][c]!='T'))
        return 0;
    return 1;
   }
 if(c==5)
   {   for(i=0;i<4;i++)
      if((A[r][i]!=a)&&(A[r][i]!='T'))
        return 0;
  return 1;
   }
}
int main()
{int flag,i,j,k,n,t;
 ifstream fin;
 fin.open("input.txt");
 ofstream fout;
 fout.open("output.txt");
 fin>>t;
 for(i=0;i<t;i++)
   {for(j=0;j<4;j++)
     for(k=0;k<4;k++)
       fin>>A[j][k];
       
    flag=0;
    for(k=0;k<4;k++)
       {if(calc(k,5,'X'))
            {flag=1;
             break;
            }
        if(calc(k,5,'O'))
            {flag=2;
             break;
            }
        if(calc(5,k,'X'))
            {flag=1;
             break;
            }
       if(calc(5,k,'O'))
            {flag=2;
             break;
            }
    }
    if(calc(1,1,'X'))
            flag=1;
             
       if(calc(1,1,'O'))
            flag=2;
             
       if(calc(2,2,'X'))
            flag=1;
            
       if(calc(2,2,'O'))
            flag=2;
             
    if(!flag)
        for(j=0;j<4;j++)     
           for(k=0;k<4;k++)              
              if(A[j][k]=='.')
                 {flag=4;
                  break;
                 }
    fout<<"Case #"<<(i+1)<<": ";
    switch(flag)
    {case 1 : fout<<"X won\n";
              break;
     case 2 : fout<<"O won\n";
              break;
     case 4 : fout<<"Game has not completed\n";
              break;
     case 0 : fout<<"Draw\n";
    }
}
fin.close();
fout.close();
return 0;

}
