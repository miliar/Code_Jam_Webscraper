#include <iostream>
using namespace std;
int main(){

long long int r,t,result,i,sum;
int tc,count=0;

cin>>tc;

while(tc--){
count++;
cin>>r>>t;
result=0;
i=r;
sum=0;
while(sum<=t){
sum=sum+(i+1)*(i+1)-(i*i);
result++;
i=i+2;
}

cout<<"Case #"<<count<<": "<<result-1<<endl;

}
return 0;
}
