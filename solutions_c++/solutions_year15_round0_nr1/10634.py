#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <iomanip>


using namespace std;

int main() {

    //taking input
      freopen("in.in","r",stdin);    //for google codejam
      freopen("out.out","w",stdout);  // for google codejam
    //giving output


//Start Code
int t=0;

scanf("%d",&t);

for (int cc=1;cc<=t;cc++){
       printf("Case #%d: ", cc);
//Test code starts
//Delete from here for next program
unsigned long long int maxs=0,num=0,newnum=0,ans=0,sum=0,mod=0,curr=0;
scanf("%llu%llu",&maxs,&num);
int people[maxs+1];

for(int i=maxs;i>=0;i--){
        mod=num%10;
        people[i]=mod;
        newnum=((num-mod)/10);
        num=newnum;


}

for(int i=0;i<=maxs;i++){

        sum+=people[i];
        if((sum<(i+1))&&((i+1)<=maxs)){
            curr=((i+1)-sum);
            sum+=curr;
            ans+=curr;
        }
    }
printf("%llu\n",ans);


//Till here
//Test Code Ends
//End Code
}

return 0;

}
