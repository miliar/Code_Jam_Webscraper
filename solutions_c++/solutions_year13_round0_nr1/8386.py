#include <iostream>
using namespace std;

struct cell
{
   int v,d,g,rd;
};

int main()
{
   int t,nem,ans;
   char ch,b[6][6],tv,td,tg,trd;
   freopen("A-small-attempt1.in","r",stdin);
   freopen("A-small-attempt1.out","w",stdout);
   cell a[6][6];
   cin>>t;
   for(int q=1; q<=t; q++)
   {
	  nem=0; ans=0; tv = td = tg = trd = 'T';
      for(int i=1; i<=4; i++)
		  for(int j=1; j<=4; j++)
		  {
		     cin>>ch;
			 b[i][j]=ch;
			 a[i][j].v= a[i][j].d= a[i][j].g= a[i][j].rd= 0;
			 if(ch=='.') nem++;
			 if(ch=='T')
			 {
				 if(j>1) {a[i][j].g=a[i][j-1].g+1;if(b[i][j-1]!='.'){tg=b[i][j-1];}} else a[i][j].g=1;
				 if(i>1) {a[i][j].v=a[i-1][j].v+1;if(b[i-1][j]!='.'){tv=b[i-1][j];}} else a[i][j].v=1;
				 if(i>1 && j>1) {a[i][j].d=a[i-1][j-1].d+1;if(b[i-1][j-1]!='.'){td=b[i-1][j-1];}} else a[i][j].d=1;
				 if(i>1 && j<4) {a[i][j].rd=a[i-1][j+1].rd+1;if(b[i-1][j+1]!='.'){trd=b[i-1][j+1];}} else a[i][j].rd=1;
			 }
			 if(ch=='O' || ch=='X')
			 {
				if(j>1) {if(b[i][j-1]==ch || (b[i][j-1]=='T' && (tg==ch || tg=='T'))) a[i][j].g=a[i][j-1].g+1;} else a[i][j].g=1;
				if(i>1) {if(b[i-1][j]==ch || (b[i-1][j]=='T' && (tg==ch || tg=='T'))) a[i][j].v=a[i-1][j].v+1;} else a[i][j].v=1;
				if(i>1 && j>1) {if(b[i-1][j-1]==ch || (b[i-1][j-1]=='T' && (tg==ch || tg=='T'))) a[i][j].d=a[i-1][j-1].d+1;} else a[i][j].d=1;
				if(i>1 && j<4) {if(b[i-1][j+1]==ch || (b[i-1][j+1]=='T' && (tg==ch || tg=='T'))) a[i][j].rd=a[i-1][j+1].rd+1;} else a[i][j].rd=1;
			 }
			 if((a[i][j].d==4 ||a[i][j].rd==4 || a[i][j].v==4 || a[i][j].g==4) && ans==0) 
			 {
					if(b[i][j]=='O'){ans=2;continue;}
					if(b[i][j]=='X'){ans=1;continue;}
					if(a[i][j].d==4)
					{
					   if(b[i-1][j-1]=='O'){ans=2;continue;}
					   if(b[i-1][j-1]=='X'){ans=1;continue;}
					}
					if(a[i][j].rd==4)
					{
					   if(b[i-1][j+1]=='O'){ans=2;continue;}
					   if(b[i-1][j+1]=='X'){ans=1;continue;}
					}
					if(a[i][j].v==4)
					{
					   if(b[i-1][j]=='O'){ans=2;continue;}
					   if(b[i-1][j]=='X'){ans=1;continue;}
					}
					if(a[i][j].g==4)
					{
					   if(b[i][j-1]=='O'){ans=2;continue;}
					   if(b[i][j-1]=='X'){ans=1;continue;}
					}
			 }
		  }
      if(ans==0 && nem==0) ans=3;
	  cout<<"Case #"<<q<<": ";
	  if(ans==1){cout<<"X won";}
	  if(ans==2){cout<<"O won";}
	  if(ans==3){cout<<"Draw";}
	  if(ans==0){cout<<"Game has not completed";}
	  cout<<endl;
   }
}