#include <iostream>
#include <bits/stdc++.h>
using namespace std;

int main()
{int t;
scanf("%d",&t);
int timer=0;
while(t){
    int n;
    scanf("%d",&n);
    string s;
    cin>>s;


    int sum=0;
    int coun=0,i;

    for(i=0;i<=n;i++){

                    if(sum>=i){
            sum=sum+s[i]-48;

        }
        else{
            coun=coun+i-sum;


            sum=i+s[i]-48;
        }
    }
    printf("Case #%d: %d\n",timer+1,coun);
    timer++;
    t--;
}
    return 0;
}
