#include<bits/stdc++.h>
using namespace std;

int main()
{
    int t;
    scanf("%d",&t);
    int smax;
    string arr;
    int tempsum=0,frnds=0;
    for(int var=1;var<=t;var++)
    {tempsum=0;frnds=0;
    scanf("%d",&smax);
    cin>>arr;
    for(int i=0;i<=smax;i++)
    { 
        if(tempsum<i){
                frnds++;tempsum++;}
      tempsum+=arr[i]-48;
     
    }
    
        printf("Case #%d: %d\n",var,frnds);
    }

}
