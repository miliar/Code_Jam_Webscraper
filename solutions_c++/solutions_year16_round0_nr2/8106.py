#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{
    int t;
  // freopen("in.txt","r",stdin);
  //   freopen("out.txt","w",stdout);

   cin>>t;
   char arr[105],brr[105];
   int count=0,mcount=0;
   int hulk=0;
   while(t--)
   {
       hulk++;
       count=0;
       mcount=0;
       cin>>arr;
       if(strlen(arr)==1)
       {
           if(arr[0]=='+')
          cout<<"Case #"<<hulk<<": "<<"0"<<endl;
           else
           cout<<"Case #"<<hulk<<": "<<"1"<<endl;
       }
       else
       {
       for(int i=0;i<strlen(arr);i++)
       {
            brr[i]=arr[i];
       }
       while(1)
       {
           count=0;
           for(int i=1;i<strlen(arr);i++)
           {
               if(arr[i-1]!=arr[i])
                break;
               else
                count++;
           }
           int cc;
           if((count+1)!=strlen(arr))
           {
               cc=0;
               for(int j=count;j>=0;j--)
               {
                   brr[cc]=arr[j];
                   if(brr[cc]=='-')
                    brr[cc]='+';
                    else
                    brr[cc]='-';
                   cc++;
               }
               mcount++;
           }
           else
            break;
            for(int i=0;i<strlen(arr);i++)
       {
            arr[i]=brr[i];
       }

       }
       if(arr[0]=='-')
        mcount++;
       cout<<"Case #"<<hulk<<": "<<mcount<<endl;
       }
   }
}
