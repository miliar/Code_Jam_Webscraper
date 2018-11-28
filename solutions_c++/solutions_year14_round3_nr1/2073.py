#include<iostream>
#include<fstream>


using namespace std;
fstream f1,f2;



int main()
{  f1.open("large.in",ios::in);
   f2.open("out.out",ios::out);
   int num,den,cas,count=0,flag=0,c=0;
   char gar;
   f1>>cas;
   while(cas)
   {   count=0;
       cas--;
       c++;
       f1>>num;
       cout<<"\n"<<num;
       f1>>gar;
       cout<<"\n"<<gar;
       f1>>den;
       cout<<"\n"<<den;


       do
       {
           if(den==num)
           {
               flag=1;
               break;
           }
           else if(den<num)
           {
            if(den%2==0)
            {flag=1;
            break;
           }
            else
            {
                flag=0;
                break;
            }

           }
           else
           {
               if((den%2)==0)
               {
                   den=den/2;
                   count++;

               }
               else
               {
                   flag=0;
                   break;
               }


           }
       }while(1);
       if(flag==0)
       f2<<"Case #"<<c<<": "<<"impossible\n";
       else
       f2<<"Case #"<<c<<": "<<count<<"\n";
   }

    return 0;
}

