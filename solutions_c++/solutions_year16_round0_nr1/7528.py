#include <iostream>
#include <vector>
#include <math.h>
#include <algorithm>
#include <stdio.h>
using namespace std;


vector<int> const12;
int output12(int in)
{
    int counter=1;
    int last=-1; 

    while (const12.size()!=10 )
    
    {
  //  int counter=1;    
//    int last=-1;    
    int flag =1;
    int flag2=0;
    int a,b,c,in_cop,in_cop2;
    in_cop = counter*in;
    in_cop2 = counter*in;

    for (int i=0;flag!=0;i++)
    {
        flag2=0;
        a = in_cop%10;
     //   const12.push_back(a);
  //      cout<<a;
        for (int i=0;i<const12.size();i++)
            {
                if (a==const12[i])
                flag2=1;
            }
            if (flag2==0)
            {
                const12.push_back(a);
                last =in_cop2;
            }
        in_cop = floor(in_cop/10);
        if(in_cop==0)
        flag=0;
    }
    counter++;
    }
  
   
   return last; 
    
}
int main()
{
    int T,N,I=0;
    int res=0;
    std::cin >> T;
    while(I++ != T){
        const12.clear();
        std::cin >> N;
        std::cout <<"Case #"<<I<<":  ";
        if (N==0)
        cout<<"INSOMNIA"<<endl;
        else
        {
        res = output12(N);
        cout<<res<<endl;
        }
    }
}
