#include<iostream>
using namespace std;
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
         int a[10] = {0};
         long long n1,n,i;
         int flag =1;
         cin>>n;
         if(n ==0 )
         {
             cout<<"INSOMNIA"<<endl;
             continue;
         }
         int count =0;
         int j = 2 ;
         n1 = n;
         while(flag)
         {
             int n2 = n1;

             while(n2 != 0)
             {
                // cout<<"\n n =="<<n<<" n1 =="<<n1<<"  n2 == "<<n2;
                 a[n2%10]++;
                 n2 /= 10;
             }

             //for(int i=0 ; i<10; cout<<" "<<a[i++])
            count = 0;
             for(int i=0 ; i<10; i++)
             {

                if(a[i] == 0)
                {

                    n1  = n1 + n;
                    break;
                 }
                 else
                    count++;
                 if(count == 10)
                 {
                   flag = 0;
                   cout<<n1<<endl;
                   break;
                 }
              }

         }


    }
    return 0;
}

