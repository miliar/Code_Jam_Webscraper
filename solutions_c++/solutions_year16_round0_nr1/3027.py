#include<stdio.h>
#include<iostream>
#include<set>
#include<algorithm>
#define mod(x) x%1000000007
#include<cstring>
#include<vector>
#include<math.h>
#include <stdlib.h>
using namespace std;


int main(){
    int t;
    cin>>t;
    for(int tt=0;tt<t;tt++)
    {
        long long int no;
        cin>>no;
        int arr[]={0,0,0,0,0,0,0,0,0,0,0};
        int count=0;
      for(int i=1;i<100;i++)
      {
        long long int dno=no*i;
        while(dno!=0)
        {
            int dig = dno%10;
            if(arr[dig]==0) {arr[dig]=1;count++;}
            dno = dno/10;
        }
        if(count==10) {cout<<"Case #"<<tt+1<<": "<<no*i<<endl;break;}
      }
      if(count<10) cout<<"Case #"<<tt+1<<": "<<"INSOMNIA"<<endl;
    }
}
