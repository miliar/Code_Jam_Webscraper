#include<iostream>
#include<vector>
using namespace std;

int main()
{

    int t;
    cin>>t;
    for( int case_no=1 ; case_no<=t ; case_no++)
    {
        unsigned long long n;
        cin>>n;

        if(n==0)
        {
            cout<<"Case #"<<case_no<<": "<<"INSOMNIA"<<endl;
        }

       else
       {
           unsigned long long cnt = 1 , curr , temp , ans = 0  ;
           vector<bool> A(10,0);
           while(1)
           {

               curr = cnt*n;
               temp = curr;

               while(curr)
               {
                   if(A[curr%10] == 0)
                   {
                       ans++;
                       A[curr%10] = 1;
                   }

                   if(ans>=10)
                   {
                       cout<<"Case #"<<case_no<<": "<<temp<<endl;
                       break;
                   }
                   curr = curr/10;
               }

               if(ans>=10)
               {
                   break;
               }

               cnt++;
           }
       }
    }

    return 0;
}
