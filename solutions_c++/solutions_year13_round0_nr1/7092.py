#include<cstdio>
#include<cstring>
#include<iostream>
#include<conio.h>

using namespace std;

char row[4][4];
long long rprod, cprod;
long long x1, x2, o1, o2;
long long product[10];



int main()
{
    
    int t,test;
    int i,j;
    

    
    freopen("input.in","r",stdin);
    freopen("output.out","w",stdout);
    scanf("%d\n",&t);
    test=t;
    
    
    
    while(t--)
    {
            
            x1 = 'X'*'X'*'X'*'X';
            x2 = 'X'*'X'*'X'*'T';
            o1 = 'O'*'O'*'O'*'O';
            o2 = 'O'*'O'*'O'*'T';
            
            printf("Case #%d: ",test-t);
            
            for(i=0;i<4;i++)
            scanf("%c%c%c%c\n",&row[i][0], &row[i][1] , &row[i][2], &row[i][3]);
            
            for(i=0;i<4;i++)
    		{
    			rprod=1;
    			cprod=1;
				for(j=0;j<4;j++)
    			{
    				rprod = rprod * row[i][j];
    				cprod = cprod * row[j][i];
    			}
    			product[i]=rprod;
    			product[i+4]=cprod;
    		}
    		product[8] = row[0][0] * row[1][1] * row[2][2] * row[3][3]; 
    		product[9] = row[0][3] * row[1][2] * row[2][1] * row[3][0];
    		
    		char w = 'w';
			for(i=0;i<10;i++)
    		{
    			if((product[i]==x1)||(product[i]==x2))
    			{
    				w='x';
    				break;
    			}
    			if((product[i]==o1)||(product[i]==o2))
    			{
    				w='o';
    				break;
    			}
    			if((product[i]%'.')==0)
    			{
    				w='.';
    			}
    		}
    		
    		switch(w)
			{
				case 'x':cout<<"X won"<<endl;
						break;
				case 'o':cout<<"O won"<<endl;
						break;
				case 'w':cout<<"Draw"<<endl;
						break;
				case '.':cout<<"Game has not completed"<<endl;
						break;		
			}
            
    }
            
            //getch();
}
                        
