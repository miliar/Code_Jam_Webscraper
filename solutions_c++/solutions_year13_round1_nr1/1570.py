#include<iostream>
#include<vector>
#include<set>
#include<conio.h>
using namespace std;
int main()
{
    int n;
    int q =0;
    cin>>n;
    while(q<n) {
               long long int r;
               long long int t;
               cin>>r;
               cin>>t;
               long long int count = 0;
               for(long long int i=r;;i=i+2) {
                       t=t-i-i-1;
                       if(t>=0) {
                               count++;
                       } else {
                              break;
                       }
               }
               if(count>0) {
               cout<<"Case #"<<q+1<<": "<<count<<endl;
               } else {
                 cout<<"Case #"<<q+1<<": 1";
               }
               q++;
}
    
    getch();
}
