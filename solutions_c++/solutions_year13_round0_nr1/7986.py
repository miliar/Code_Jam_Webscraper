#include<stdio.h>
#include<conio.h>

int main()
{
    int cases;
    int x,y;
    char kotak[5][5];
    scanf("%i\n",&cases);
    for(int i=1;i<=cases;i++)
    {
            for(y=0;y<=3;y++)
            {
                    scanf("%c%c%c%c",&kotak[y][0],&kotak[y][1],&kotak[y][2],&kotak[y][3]);
                    scanf("%*c");
            }
            scanf("%*c");
            printf("Case #%i: ",i);
            if((kotak[0][0]=='X'||kotak[0][0]=='T')&&(kotak[0][1]=='X'||kotak[0][1]=='T')&&(kotak[0][2]=='X'||kotak[0][2]=='T')&&(kotak[0][3]=='X'||kotak[0][3]=='T'))
                    printf("X won");                    
            else if((kotak[1][0]=='X'||kotak[1][0]=='T')&&(kotak[1][1]=='X'||kotak[1][1]=='T')&&(kotak[1][2]=='X'||kotak[1][2]=='T')&&(kotak[1][3]=='X'||kotak[1][3]=='T'))        
                    printf("X won");
            else if((kotak[2][0]=='X'||kotak[2][0]=='T')&&(kotak[2][1]=='X'||kotak[2][1]=='T')&&(kotak[2][2]=='X'||kotak[2][2]=='T')&&(kotak[2][3]=='X'||kotak[2][3]=='T'))        
                    printf("X won");        
            else if((kotak[3][0]=='X'||kotak[3][0]=='T')&&(kotak[3][1]=='X'||kotak[3][1]=='T')&&(kotak[3][2]=='X'||kotak[3][2]=='T')&&(kotak[3][3]=='X'||kotak[3][3]=='T'))        
                    printf("X won");
            else if((kotak[0][0]=='X'||kotak[0][0]=='T')&&(kotak[1][1]=='X'||kotak[1][1]=='T')&&(kotak[2][2]=='X'||kotak[2][2]=='T')&&(kotak[3][3]=='X'||kotak[3][3]=='T'))        
                    printf("X won");
            
            else if((kotak[0][0]=='O'||kotak[0][0]=='T')&&(kotak[0][1]=='O'||kotak[0][1]=='T')&&(kotak[0][2]=='O'||kotak[0][2]=='T')&&(kotak[0][3]=='O'||kotak[0][3]=='T'))
                    printf("O won");                    
            else if((kotak[1][0]=='O'||kotak[1][0]=='T')&&(kotak[1][1]=='O'||kotak[1][1]=='T')&&(kotak[1][2]=='O'||kotak[1][2]=='T')&&(kotak[1][3]=='O'||kotak[1][3]=='T'))        
                    printf("O won");
            else if((kotak[2][0]=='O'||kotak[2][0]=='T')&&(kotak[2][1]=='O'||kotak[2][1]=='T')&&(kotak[2][2]=='O'||kotak[2][2]=='T')&&(kotak[2][3]=='O'||kotak[2][3]=='T'))        
                    printf("O won");        
            else if((kotak[3][0]=='O'||kotak[3][0]=='T')&&(kotak[3][1]=='O'||kotak[3][1]=='T')&&(kotak[3][2]=='O'||kotak[3][2]=='T')&&(kotak[3][3]=='O'||kotak[3][3]=='T'))        
                    printf("O won");
            else if((kotak[0][0]=='O'||kotak[0][0]=='T')&&(kotak[1][1]=='O'||kotak[1][1]=='T')&&(kotak[2][2]=='O'||kotak[2][2]=='T')&&(kotak[3][3]=='O'||kotak[3][3]=='T'))        
                    printf("O won");  
            
            else if((kotak[0][0]=='O'||kotak[0][0]=='T')&&(kotak[1][0]=='O'||kotak[1][0]=='T')&&(kotak[2][0]=='O'||kotak[2][0]=='T')&&(kotak[3][0]=='O'||kotak[3][0]=='T'))
                    printf("O won");                    
            else if((kotak[0][1]=='O'||kotak[0][1]=='T')&&(kotak[1][1]=='O'||kotak[1][1]=='T')&&(kotak[2][1]=='O'||kotak[2][1]=='T')&&(kotak[3][1]=='O'||kotak[3][1]=='T'))        
                    printf("O won");
            else if((kotak[0][2]=='O'||kotak[0][2]=='T')&&(kotak[1][2]=='O'||kotak[1][2]=='T')&&(kotak[2][2]=='O'||kotak[2][2]=='T')&&(kotak[3][2]=='O'||kotak[2][3]=='T'))        
                    printf("O won");        
            else if((kotak[0][3]=='O'||kotak[0][3]=='T')&&(kotak[1][3]=='O'||kotak[1][3]=='T')&&(kotak[2][3]=='O'||kotak[2][3]=='T')&&(kotak[3][3]=='O'||kotak[3][3]=='T'))        
                    printf("O won");
            else if((kotak[0][3]=='O'||kotak[0][3]=='T')&&(kotak[1][2]=='O'||kotak[1][2]=='T')&&(kotak[2][1]=='O'||kotak[2][1]=='T')&&(kotak[3][0]=='O'||kotak[3][0]=='T'))        
                    printf("O won");         
                  
            else if((kotak[0][0]=='X'||kotak[0][0]=='T')&&(kotak[1][0]=='X'||kotak[1][0]=='T')&&(kotak[2][0]=='X'||kotak[2][0]=='T')&&(kotak[3][0]=='X'||kotak[3][0]=='T'))
                    printf("X won");                    
            else if((kotak[0][1]=='X'||kotak[0][1]=='T')&&(kotak[1][1]=='X'||kotak[1][1]=='T')&&(kotak[2][1]=='X'||kotak[2][1]=='T')&&(kotak[3][1]=='X'||kotak[3][1]=='T'))        
                    printf("X won");
            else if((kotak[0][2]=='X'||kotak[0][2]=='T')&&(kotak[1][2]=='X'||kotak[1][2]=='T')&&(kotak[2][2]=='X'||kotak[2][2]=='T')&&(kotak[3][2]=='X'||kotak[2][3]=='T'))        
                    printf("X won");        
            else if((kotak[0][3]=='X'||kotak[0][3]=='T')&&(kotak[1][3]=='X'||kotak[1][3]=='T')&&(kotak[2][3]=='X'||kotak[2][3]=='T')&&(kotak[3][3]=='X'||kotak[3][3]=='T'))        
                    printf("X won");
            else if((kotak[0][3]=='X'||kotak[0][3]=='T')&&(kotak[1][2]=='X'||kotak[1][2]=='T')&&(kotak[2][1]=='X'||kotak[2][1]=='T')&&(kotak[3][0]=='X'||kotak[3][0]=='T'))        
                    printf("X won");                 
                    
            else
            {
                for(y=0;y<=3;y++)
                {
                  for(x=0;x<=3;x++)
                  {
                     if(kotak[y][x]=='.') x=9,y=9;
                  }   
                }
                if(x>=9 && y>=9) printf("Game has not completed");
                else printf("Draw");
            }        
            printf("\n");
                    
    }
}
