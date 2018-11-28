#include<iostream.h>
#include<conio.h>
#include<stdlib.h>
#include<string.h>
#include<fstream.h>

char brd[4][8];

void print_res()
{
 int gc=1,j,i;
 char p;
 for(i=0;i<4;i++)
 {
   p='T';
   for(j=0;j<4;j++)
   {
     if(p=='T')
      p=brd[i][j];
     else if(brd[i][j]=='.')
     {
      gc=0;
       break;
      }

     else if(brd[i][j]!='T' && brd[i][j]!=p)
     {
       break;
     }
   }
   if(j==4 && p!='.')
   {
    cout<<p<<" won";

    return;
    }
  }

 for(i=0;i<4;i++)
 {
   p='T';
   for(j=0;j<4;j++)
   {
     if(p=='T')
      p=brd[j][i];
     else if(brd[j][i]=='.')
	  {
      gc=0;
       break;
      }
      else if(brd[j][i]!='T' && brd[j][i]!=p)
     {
       break;
     }
   }
   if(j==4 && p!='.')
   {
    cout<<p<<" won";
    return;
    }
  }

   p='T';
   for(j=0;j<4;j++)
   {
     if(p=='T')
      p=brd[j][j];
     else if(brd[j][j]=='.')
     {
      gc=0;
      break;
      }
     else if(brd[j][j]!='T' && brd[j][j]!=p)
     {
       break;
     }
   }
   if(j==4 && p!='.')
   {
    cout<<p<<" won";
    return;
    }



   p='T';
   for(j=0;j<4;j++)
   {
     if(p=='T')
      p=brd[j][3-j];
     else if(brd[j][3-j]=='.')
	   {
      gc=0;
       break;
      }

     else if(brd[j][3-j]!='T' && brd[j][3-j]!=p)
     {
       break;
     }
   }
   if(j==4 && p!='.')
   {
    cout<<p<<" won";
    return;
    }

    if(gc==1)
     cout<<"Draw";
    else
     cout<<"Game has not completed";

}


void main()
{
 clrscr();
 long nc,i;
 char str[10],*ptr;
 int j;
 fstream mf("ipfile.txt",ios::in);
 mf.getline(str,5,'\n');
 nc=strtol(str,&ptr,10);

 for(i=1;i<=nc;i++)
 {
   cout<<"\nCase #"<<i<<": ";
   for(j=0;j<4;j++)
   {
    mf.getline(brd[j],6,'\n');
   }
    mf.getline(str,6,'\n');
    print_res();
    //for(j=0;j<4;j++)
    // cout<<"\n"<<brd[j];
 }

 getch();
}