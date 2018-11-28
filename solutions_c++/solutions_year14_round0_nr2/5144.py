#include<iostream>
#include<cstdio>
using namespace std;
int main()
{
    int N;
    cin>>N;
   long  double res[100000];
    for(int i=1;i<=N;i++)
    {
       long  double C,F,X;
        cin>>C>>F>>X;
       long  double num=2.0;
        res[0]=X/num;
        int n=1;
       long double sum=0.0;
        while(1)
        {
             sum=sum+(C/num);
          num=num+F;
          res[n]=sum+(X/num);
          if(res[n]> res[n-1]){
            printf("%s%d%s%.7llf\n","Case #",i,": ",res[n-1]);
            break;
            }

         // cout <<res[n]<<endl;
          n++;
        }
        }
    return 0;
}
