#include<cstdio>
#include<iostream>
using namespace std;
bool palindrome(unsigned long long int a)
{
     char str[15];
     int i=0;
     while(a)
     {
             str[i++]=a%10+'0';
             a=a/10;
     }
     for(int j=0; j<=i/2; j++)
     {
             if(str[j]!=str[i-j-1])
                                   return false;
     }
     return true;
}
main()
{
      freopen("codejam13_0_2_in.txt", "r", stdin);
      freopen("codejam13_0_2_out.txt", "w", stdout);
     // int arr[]={1, 2, 3, 11, 22};
      unsigned long long int brr[100];
      int total=0;
     for(unsigned long long int i=1; i<10000001; i++)
     {
           if(palindrome(i) && palindrome(i*i))
                            brr[total++]=i*i;
     } 
    int t;
    cin>>t;
    for(int tt=1; tt<=t; tt++)
    {
            unsigned long long int a, b, lessa=0, lessb=0;
            cin>>a>>b;
            for(int i=0; i<total; i++)
            {
                  if(brr[i]<a)
                              lessa++;  
            }
            for(int i=0; i<total; i++)
            {
                  if(brr[i]<=b)
                              lessb++;  
            }
            cout<<"Case #"<<tt<<": "<<lessb-lessa<<endl;
    }
}
