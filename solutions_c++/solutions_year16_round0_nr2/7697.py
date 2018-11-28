#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<string.h>
void main()
{  int number,length;
   char line[150],temp;
   ifstream read;
   ofstream write;
   read.open("pancakes.txt");
   write.open("panoutput.txt");
   read>>number;
   int i,j,k=0,l,counter=0;
   for(i=0;i<number;i++)
   {
      read>>line;
      length=strlen(line);
      {
        k=1;
        while(k<length)
        {
           if(line[j]==line[k])
           k++;
           else
           {
             for(l=0;l<k;l++)
             {
             temp=line[l];
             line[l]=line[k-l];
             line[k-l]=temp;
             } //for
            counter++;
            k++;
           }    //else
       }     //while
      }      //outer for
      if(line[0]=='+')
     { cout<<"Case #"<<(i+1)<<": "<<counter<<endl;
      write<<"Case #"<<(i+1)<<": "<<counter<<endl;  }
      else
     { cout<<"Case #"<<(i+1)<<": "<<(counter+1)<<endl;
      write<<"Case #"<<(i+1)<<": "<<(counter+1)<<endl; }
      counter=0;
   }           //outer most for
   read.close();
   write.close();
   getch();
}