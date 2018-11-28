#include<stdio.h>
char check(char a[4][4]);
int main()
{
	char n[4][4], x,f;
	
	int t, i, j,p=0,c;
	
	scanf("%d",&t);
	
	 c=1;
	 
	while(t>0)
    {
	    f=getchar();
	    
	    i=0; j=0; p=0;

        for(i=0;i<4;i++)
		  {
			for(j=0;j<4;j++)
		     {
			  n[i][j]=getchar();
			  //scanf("%c",&n[i][j]);
		     if(n[i][j]=='.')
			     p=1;
			 }
		   f=getchar();
		  } 
        x = check(n);	 	   
	
	   if(x=='X')
	   printf("Case #%d: X won\n",c);
	   
	   else if(x=='O')
	   printf("Case #%d: O won\n",c);
	   
	   else if((x=='.')&&(p==0))
	   printf("Case #%d: Draw\n",c);
	   
	   else
	   printf("Case #%d: Game has not completed\n",c);
	
	  c++;
	  t--;
	}	
	
	
		
   return 0;
	
}



char check(char a[4][4])
{
	char d, x, y;
	int i=0;
	
	while(i<=3)
   {
     d=x=y=a[i][i];;
     
     if(d!='.')
     {
        if(d=='T')
        {
		   x=a[i][(i+1)%4];
		   y=a[(i+1)%4][i];
		}
        
        if((a[i][0]==x||a[i][0]=='T')&&(a[i][1]==x||a[i][1]=='T')&&(a[i][2]==x||a[i][2]=='T')&&(a[i][3]==x||a[i][3]=='T'))  
		        return x;
        
		if((a[0][i]==y||a[0][i]=='T')&&(a[1][i]==y||a[1][i]=='T')&&(a[2][i]==y||a[2][i]=='T')&&(a[3][i]==y||a[3][i]=='T'))  
		        return y;
	 }
   
   
     i++;
   }	
	
	d=a[0][0];
	if(d!='.')
	{
		if(d=='T')
		  d=a[1][1];
		  
	   	if((a[0][0]==d||a[0][0]=='T')&&(a[1][1]==d||a[1][1]=='T')&&(a[2][2]==d||a[2][2]=='T')&&(a[3][3]==d||a[3][3]=='T'))  
		        return d;  
		 
	}
	
	d=a[0][3];
	if(d!='.')
	{
		if(d=='T')
		  d=a[1][2];
		  
	   	if((a[0][3]==d||a[0][3]=='T')&&(a[1][2]==d||a[1][2]=='T')&&(a[2][1]==d||a[2][1]=='T')&&(a[3][0]==d||a[3][0]=='T'))  
		        return d;  
		 
	}
	
	d='.';
	
	return d;
	
}

