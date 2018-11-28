#include <cstdio>
#include <cstdlib>

using namespace std;

char A[4][4];

bool check(char key)
{
	for (int i=0;i<4;i++) for (int j=0;j<4;j++)
		for (int dx=-1;dx<=1;dx++) for (int dy=-1;dy<=1;dy++) if (abs(dx)+abs(dy)>0)
		{
			bool isGood=true;
			for (int d=0;d<4;d++)
			{
				int x=i+dx*d;
				int y=j+dy*d;
				if (x<0 || x>=4 || y<0 || y>=4 || A[x][y]!=key)
				{
                    if(A[x][y]!='T')
                    {
					   isGood=false;
					   break;
                    }
				}
			}
			if (isGood) return true;
		}
	return false;
}
int main()
{
    freopen("C:/Users/fafo/Desktop/tic/A-small-attempt0.in","r",stdin); 
    freopen("C:/Users/fafo/Desktop/tic/A-small-attempt0.out","w",stdout);
    
   	int testcase,counter;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{
        counter=0;
		printf("Case #%d: ",caseId);
	    for (int j=3;j>=0;j--) 
		{
			for (int i=0;i<4;i++)
			{
				char c;
				do{scanf("%c",&c);
				}while (c!='.' && c!='X' && c!='O' && c!='T');
				A[i][j]=c;
			}
		}
		bool bX=check('X');
		bool bO=check('O');
		
		for (int j=3;j>=0;j--) 
		{
			for (int i=0;i<4;i++)
			{
                if(A[i][j]=='.')
                {
                   counter=counter+1;
                }
            }
        }
        if(counter>0)
        {
           if (!bX && !bO)
			printf("Game has not completed\n");
  	       else if (bX && !bO)
			printf("X won\n");
		   else if (!bX && bO)
			printf("O won\n");
        }
        else
        {
             if (!bX && !bO)
			printf("Draw\n");
  	       else if (bX && !bO)
			printf("X won\n");
		   else if (!bX && bO)
			printf("O won\n");
		   else
			printf("Draw\n");
        }
		fflush(stdout);
	}
	return 0;
}

