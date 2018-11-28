#include <iostream>
#include<math.h>
#include<string>
using namespace std;
int main()
{
  long int t,k,i,j,cou;
  string num;
  cin>>t;
  for(j=0;j<t;j++)
 { cin>>num;
   k = num.length();
   cou=0;
    if(k==1)
    {
        if(num[0]=='-')
        {
           cout<<"case #"<<(j+1)<<": 1\n";
           continue;
        }
        else
        {
           cout<<"case #"<<(j+1)<<": 0\n";
           continue;
        }
    }
    else
    {
       for(i=0;i<k-1;i++)
            {  if(num[i]!=num[i+1])
                {
                    cou++;
                }
            }
        if(num[k-1]=='-')
        {     cou++;
        }
     }
     cout<<"case #"<<(j+1)<<": "<<cou<<"\n";

}
return 0;
}
