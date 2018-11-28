#include <cstdio>
#include <string>
#include <iostream>
using namespace std;
int main()
{
    int T;
    scanf("%d",&T);
    char s[1010];
    for(int I = 1; I <= T; ++I)
    {
          int k;
          cin>>k>>s;          
          int standing = 0, needed = 0;
          standing += s[0] - '0';
          for(int i = 1; i <= k; ++i)
          {
              //  cout<<"Before.. ";
              //  cout<<i<<" "<<standing<<" "<<needed<<endl;  
                if (s[i] == '0') {}
                else if (i <= standing)
                {
                     standing += s[i] - '0';
                }
                else
                {
                    needed += i - standing;
                    standing += needed;
                    standing += s[i] - '0';
                }
               // cout<<"After.. ";
             //   cout<<i<<" "<<standing<<" "<<needed<<endl;  
                
          
          }
          printf("Case #%d: %d\n",I,needed);
    }
    cin.get();
    cin.get();
}
                    
                
          
          
          
