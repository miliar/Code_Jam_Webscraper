#include<stdio.h>
#include<string.h>
int wonBy(char c, char b[][4]) {
		for(int i = 0; i < 4; ++i ) {
			int ct1 = 0, ct2 = 0;
			for(int j = 0; j < 4; ++j ) {
				if(b[i][j] == c || b[i][j] == 'T') ct1++;
				if(b[j][j] == c || b[i][j] == 'T') ct2++;
			}
			if(ct1 == 4 || ct2 == 4) return true;
		}
		int ct = 0;
		for(int i = 0, j = 0; i<4 && j<4; ++i, ++j)
			if(b[i][j] == c || b[i][j] == 'T') ct++;
		if(ct == 4) return true;
		
		ct = 0;
		for(int i = 0, j = 3; i<4 && j>=0; ++i, --j)
			if(b[i][j] == c || b[i][j] == 'T') ct++;
		if(ct == 4) return true;
		
		return false;
	}
	
	int inProgress(char b[][4]) {
		for(int i = 0; i < 4; ++i )
			for(int j = 0; j < 4; ++j )
				if(b[i][j] == '.')
					return true;
		return false;
		
	}
 int check(char b[][4]) {
		if(wonBy('X', b)) return 1 ;
		if(wonBy('O', b)) return 2 ;
		if(inProgress(b)) return 3;
		return 4;
}
int main()
{
    int i,t,n,j,result;
    char r[4][4];
	char a[]="X won";
	char b[]="O won";
	char c[]="Game has not completed";
	char d[]="Draw";
    
	FILE *fp;
   
    fp = fopen("c:\\d.in", "r");
    
    fscanf(fp,"%d",&t);
    
    for(j=1;j<=t;j++)
    {
              
              
              for(i=0;i<4;i++)
              {
                   fscanf(fp," %c%c%c%c",&r[i][0],&r[i][1],&r[i][2],&r[i][3]);
              }
			  
              
             result=check(r);
             if(result==1)
				 printf("Case #%d: %s\n",j,a);
			 else if(result==2)
				 printf("Case #%d: %s\n",j,b);
			 else if(result==3)
				 printf("Case #%d: %s\n",j,c);
			 else
				 printf("Case #%d: %s\n",j,d);
    }
   
	 fclose(fp);
}