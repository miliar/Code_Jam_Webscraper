#include<iostream>
#include<string.h>
using namespace std;
int main()
{
string str ;

int counter =0 ;
int t ;
cin>>t ;
int z=1 ;

while(z<=t)
{

cin>>str  ;
int l =str.length() ;
counter = 0  ;
for(int i =0 ; i<l ;i++)
{
    if(str[i]=='+')
    {
        if(i+1!=l)
        {
            if(str[i+1]=='+')
            {
                continue ;
            }
            else
            {
                counter ++ ;
              //  i++;
                if(i+1==l-1)
                {
                    counter++;
                    break ;
                }
            }

        }


    }
    else if(str[i]=='-')
    {
       if(i+1!=l)
        {   if(str[i+1]=='-')
            {
                continue ;
            }
             else
             {
                 counter++ ;
             }


        }
        else
        {
            counter=counter ++ ;
        }


    }








}

cout<<"Case #"<<z<<": "<<counter<<endl ;
z++;
}



return  0  ;
}
