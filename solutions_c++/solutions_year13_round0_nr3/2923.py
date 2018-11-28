#include<iostream>
#include<math.h>
#include<algorithm>
#include<cstdio>
#include<string>
#include<fstream>
using namespace std;
int main()
{
     ifstream istr;
    ofstream ef;
    ef.open("ans.txt");
    istr.open("1.txt");
    int arr[]={1,4,9,121,484};
    int t,test,a,b,ct,i;
    istr>>t;
    for(test=1;test<=t;test++){
                               ct=0;
                               istr>>a>>b;
                               for(i=0;i<5;i++){
                                                if(arr[i]>=a && arr[i]<=b){
                                                             ct++;
                                                }
                               }
                               ef<<"Case #"<<test<<": "<<ct<<"\n";
    }
    istr.close();
    ef.close();
   system("pause");
   return 0;
}
