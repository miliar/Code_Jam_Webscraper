#include<stdio.h>
#include<iostream>

using namespace std;
double C,F,X;

double func(double cookies){

if((X/cookies)<0.08889)
    {
        //cout<<"last time "<<(X/cookies)<<" "<<cookies<<endl;
        return (X/cookies);

        }

//if(C>=X)
  //  return (X/cookies);

//cout<<cookies<<"  "<<(C/cookies)<<" "<<(X/cookies)<<endl;

return (C/cookies)+min((X/(cookies+F)),func(cookies+F));
}

int main(){

int t,casecount=1;
cin>>t;

while(t--){
    cin>>C>>F>>X;

   // if(X<C)
     //   printf("Case #%d: %0.7lf\n",casecount,X/2);
    //else
        printf("Case #%d: %0.7lf\n",casecount,min(X/2,func(2)));
    casecount++;
}

return 0;
}
