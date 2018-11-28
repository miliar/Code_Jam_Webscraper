#include <iostream>
#include <fstream>
using namespace std;
int main()
{
    int T,N,i;
    cin >>T;

    ofstream cout1;
    cout1.open("A1.txt");
    for(i=1;i<=T;i++)
    {
        cin >>N;

        cout1<<"Case #"<<i<<": ";
        if(N==2)
        {


            int a,b;
            cin >>a>>b;


            while(a--)
            {
                cout1 <<"AB ";
            }
            cout1<<endl;
        }
        else
        {
           int a[4];
           cin >>a[1]>>a[2]>>a[3];

           if(a[3]>=a[2] && a[3]>=a[1])
           {
               if(a[2]>=a[1])
               {

                   while(a[3]!=a[2])
                   {
                       cout1 <<"C ";
                       a[3]--;
                   }

                   while(a[3]!=a[1])
                   {
                       cout1 <<"CB ";
                       a[3]--;
                       a[2]--;
                   }

                   while(a[1]!=1)
                   {
                       cout1 <<"A B C ";
                       a[1]--;
                   }

                   cout1 <<"A BC";
               }
               else
               {

                   while(a[3]!=a[1])
                   {
                       cout1 <<"C ";
                       a[3]--;
                   }
                   while(a[3]!=a[2])
                   {
                       cout1 <<"CA ";
                       a[3]--;
                       a[1]--;
                   }

                   while(a[2]!=1)
                   {
                       cout1 <<"A B C ";
                       a[2]--;
                   }
                    cout1 <<"A BC";
               }




           }
           else if(a[2]>=a[3] && a[2]>=a[1])
           {

               if(a[3]>=a[1])
               {

                   while(a[2]!=a[3])
                   {
                       cout1 <<"B ";
                       a[2]--;
                   }

                   while(a[2]!=a[1])
                   {
                       cout1 <<"BC ";
                       a[2]--;
                       a[3]--;
                   }

                   while(a[1]!=1)
                   {
                       cout1 <<"A B C ";
                       a[1]--;
                   }
                    cout1 <<"A BC";
               }
               else
               {

                   while(a[2]!=a[1])
                   {
                       cout1<<"B ";
                       a[2]--;
                   }
                   while(a[2]!=a[3])
                   {
                       cout1 <<"AB ";
                       a[2]--;
                       a[1]--;
                   }

                   while(a[3]!=1)
                   {
                       cout1 <<"A B C ";
                       a[3]--;
                   }
                    cout1 <<"A BC";
               }





           }
           else
           {

               if(a[2]>=a[3])
               {

                   while(a[1]!=a[2])
                   {
                       cout1 <<"A ";
                       a[1]--;
                   }

                   while(a[1]!=a[3])
                   {
                       cout1<<"BA ";
                       a[1]--;
                       a[2]--;
                   }

                   while(a[3]!=1)
                   {
                       cout1 <<"A B C ";
                       a[3]--;
                   }
                    cout1 <<"A BC";
               }
               else
               {

                   while(a[1]!=a[3])
                   {
                       cout1 <<"A ";
                       a[1]--;
                   }
                   while(a[1]!=a[2])
                   {
                       cout1 <<"AC ";
                       a[1]--;
                       a[3]--;
                   }

                   while(a[2]!=1)
                   {
                       cout1 <<"A B C ";
                       a[2]--;
                   }
                    cout1 <<"A BC";
               }






           }

            cout1 <<endl;
        }
    }

    return 0;
}
