#include<fstream.h>
#include<stdio.h>
#include<ctype.h>
#include<string.h>
#include<iostream.h>
#include<conio.h>
int main()
{
	      char c;
	      int t,s,j,i,sum,count,n,pos[1001];
	      clrscr();
	      ofstream out;
	      out.open("op.io");
	      ifstream in("inpl.in");
	      in>>t;
	      for(i=1;i<=t;i++){
	      in>>s;
	      for(j=0;j<=s;j++) {
	      in>>c;
	      pos[j]=(int)c-48;
	       }
	       sum=0;
	       count=0;
	       for(j=0;j<=s;j++) {
		 if(sum>=j)
		 {sum+=pos[j];}
		 else
		 {
			sum+=1;
			count++;
			j--;
		 }
	       }
	       cout<<count<<endl;
	     out<<"Case #"<<i<<": "<<count<<endl;
	      }
	      out.close();
	      getch();
	      return 0;

}
