#include<iostream>
#include<string>

using namespace std;

int main(){
int t;
cin>>t;
int z=1;
while(t--){
   int n=0,d;
   cin>>d;
   int a[1000],max=-1;
   for(int i=0;i<d;i++)
   {cin>>a[i];if(max<a[i])max=a[i];}
   int curr_time=max,add=0;

   while(max>1){
   for(int i=0;i<d;i++){
    if(a[i]==max){
        a[i]=max/2;
        a[d+n]=max-a[i];
        n++;
        add++;
    }
   }
   d=d+n;
   max=-1;
   for(int i=0;i<d;i++)
    if(max<a[i])
    max=a[i];

   if(max+add<=curr_time)
    curr_time=max+add;
   else break;

   }

   cout<<"Case #"<<z<<": "<<curr_time<<endl;
   z++;
}

return 0;
}