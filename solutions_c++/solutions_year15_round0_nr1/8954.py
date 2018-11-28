#include<conio.h>
#include<stdio.h>
#include<string.h>
#include<iostream.h>
#include<ctype.h>
#include<fstream.h>

int main()
{
	      char c;
	      int t,s,j,i,sm,cnt,n,p[7];
	      clrscr();
	      ofstream out;
	      out.open("output.io");
	      ifstream in("input.in");
	      in>>t;
	      for(i=1;i<=t;i++){
	      in>>s;
	      for(j=0;j<=s;j++) {
	      in>>c;
	      p[j]=(int)c-48;
	       }
	       sm=0;
	       cnt=0;
	       for(j=0;j<=s;j++) {
		 if(sm>=j)
		 {sm+=p[j];}
		 else
		 {
			++sm;
			cnt++;
			j--;
		 }
	       }
	       cout<<cnt<<endl;
	     out<<"Case #"<<i<<": "<<cnt<<endl;
	      }
	      out.close();
	      getch();
	      return 0;

}
