#include<iostream>
#include<fstream>
#include<conio.h>
using namespace std;
int mainr[16];
int row1[4],rowa[4],index=0;
int main()
{
   ifstream readf("input.txt");
   ofstream writef("output.txt");
   
   int* getrow(int);
   unsigned int test,rno,sucess=0;
   readf>>test;
 for(int tt=1;tt<=test;tt++)
 {
   readf>>rno;
   for(int q=0;q<16;q++)
   {readf>>mainr[q];}
   getrow(rno);
  for(int i =0;i<4;i++)
  {
          rowa[i]=row1[i];
  }
   //cout<<row1[0]<<" "<<row1[1]<<" "<<row1[2]<<" "<<row1[3]<<" ";
   readf>>rno;
    for(int q=0;q<16;q++)
   {readf>>mainr[q];}
   // extract new grid into mainr[]
  
    getrow(rno);
    //cout<<row1[0]<<" "<<row1[1]<<" "<<row1[2]<<" "<<row1[3]<<" ";
    sucess=0;
   for(int i=0 ;i<4;i++)
   {
         for(int j=0;j<4;j++)
         { if(row1[i]==rowa[j]){ sucess++;index=j;} }  //cout<<"\ns= "<<sucess<<" i="<<index;
           
   }
   if (sucess==1)
   {writef<<"\n"<<"Case #"<<tt<<": "<<rowa[index];}
   else if (sucess==0)
   {writef<<"\n"<<"Case #"<<tt<<": Volunteer cheated!";}
   else
   {writef<<"\n"<<"Case #"<<tt<<": Bad magician!"; }
    
 }
//getch();
 return 1;        
}

void getrow(int n)
{
         
   row1[0]=mainr[(n-1)*4];
   row1[1]=mainr[(n-1)*4+1];
   row1[2]=mainr[(n-1)*4+2];
   row1[3]=mainr[(n-1)*4+3];


}   
         
         

