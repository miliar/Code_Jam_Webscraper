#include <cstdlib>
#include <algorithm>
//#include <iomanip>
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
READ("B-large.in");
WRITE("out.out");
int t ; 
cin >> t;
int ok=1;
int cnt =1;
int counter=0;
double Time,C,F,X, res1,res2,result=0.0, temp1;
while(cnt<=t)
{
    cin>>C>>F>>X;
    ok=1;
    counter=0;
    temp1=0;
    result=0;
    while(ok!=2)
    {
       counter++;        
    if(counter ==1)temp1=2.000000;   
    
    Time = (C/temp1);
    
    res1= (X/C) *Time;
    res2= Time+((C/(temp1+F))*(X/C));
  //  cout << res1 << "  " <<res2 << "  " ;
    if(res1>res2)result+=Time;
    else {result+=res1; ok=2;}
   // cout << result << endl;
    temp1+=F;
   // ok++;
   // F+=4;
    }
    cout.setf(ios::fixed,ios::floatfield);
    cout.precision(7);
    cout <<"Case #" <<cnt<<": " <<result<<endl;
    cnt++;
}


return 0;
}


