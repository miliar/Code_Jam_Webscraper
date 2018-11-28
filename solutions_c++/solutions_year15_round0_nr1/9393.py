#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cctype>
#include <vector>
#include <set>
#include <stack>
#include <iostream>
#include <string>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
using namespace std;
int main ()
{
READ("A-large2.in");
WRITE("outlarge2.out");

int t ; 
cin >> t;

string s; 

int counter ,sum;
int maxi;
int cnt=1;
while(cnt<=t)
{      
             counter=0;
             sum=0;
                       
             cin>> maxi;
             cin>> s;
             for(int i =0;i<s.size() ;i++)
             { 
                     if(i>sum)
                    {
                             counter+= (i-sum);
                             sum+= (i-sum); 
                    }
                    sum+=s[i]-'0';
                    
             }
                         
             
              cout <<"Case #" <<cnt<<": " <<counter<<endl;
              cnt++;
}

//system("pause");
return 0;
}


