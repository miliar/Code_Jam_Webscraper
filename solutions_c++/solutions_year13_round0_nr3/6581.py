
#include<iostream>
#include<vector>
#include<sstream>
#include<math.h>
#define READ(s) freopen(s, "r", stdin)
#define WRITE(s) freopen(s, "w", stdout)
using namespace std ;
bool isPali(int a)
{
    
     stringstream ss ;
                   ss<<a ;
                   string s,s1 ;
                   ss>>s ;
                   s1 = s ;
                   reverse(s1.begin(),s1.end()) ;
                   if (s1 == s)return true ;
                   return false ;
}
     
int main()
{
     READ("C-small-attempt0.in");
     WRITE("C-small-attempt0.out");
    int N ;
    cin>>N ;
    for(int t =0 ; t<N ; t++){
            int a,b ;
            cin>>a>>b ;
            int res = 0 ;
            for(int i = a ; i<=b ; i++)
            {
                    int c = sqrt(i) ;
                    double c2 = sqrt(i) ;
                    if (c2 ==c)
                    if (isPali(i) && isPali(c))res++;
            }
            cout<<"Case #"<<t+1<<": "<<res<<endl ;
                   
                              
    }
    //system("pause");
    }
