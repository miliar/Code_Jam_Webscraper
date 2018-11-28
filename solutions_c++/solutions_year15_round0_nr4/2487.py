/***********************
By : Sujay Kumar
Sat 11 Apr 2015 09:52:04 AM IST
Code Jam 15 : Omnious Omino
************************/

#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
#include<stack>
#include<cstdio>
#include<cstdlib>
#include<cmath>

#define printexpr(EXPR) cout << #EXPR << " : " << EXPR << endl
#define newline std::cout << std::endl
#define printstr(STR) std::cout << STR << std::endl
#define rep(n) for(int i=0;i<n;++i)
#define reprev(n) for(int i=n-1;i>=0;--i)

typedef long long int ll;
using namespace std;


main()
{
	int cases;
	FILE *in = fopen("input.txt","r"),*out = fopen("output.txt","w");
	fscanf(in,"%d",&cases);
	for(int i=0;i<cases;++i)
	{
	  int ans = -1;
	  int n,x,y;
	  fscanf(in,"%d%d%d",&n,&x,&y);
	  if(((x*y)%n)!=0)
	    ans = 0;
	  else
	  {
	    switch(n)
	    {
	      case 1:
		 ans = 1;
		 break;
		 
	      case 2:
		if(((x*y)%2)==0)
		   ans = 1;
		else ans = 0;
		break;
		
	      case 3:
		if(x==1 || y==1)
		   ans = 0;
		else ans = 1;
		break;
		
	      case 4:
		if(x<3 || y<3)
		   ans = 0;
		else ans = 1;
		break;
		
	      case 5:
	      case 6:
		if(x<=3 || y<=3)
		    ans = 0;
		else ans = 1;
		break;
	  
	      default:
		  ans = 0;

	    }
	  }
	    if(ans)
	      fprintf(out,"Case #%d: GABRIEL\n",i+1);
	    else  fprintf(out,"Case #%d: RICHARD\n",i+1);
	  
	}

	return 0;
}
