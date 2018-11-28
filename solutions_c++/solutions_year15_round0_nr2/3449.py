#include <iostream>
#include <cstdio>
using namespace std;
int main(){
    int t,c=1;
    cin>>t;
    while(t--) {
               int d;
               cin>>d;
               int arr[d],max=arr[0],min;
               for(int i=0;i<d;i++){
                       cin>>arr[i];
                       if (arr[i]>max)
                          max=arr[i];
               }
               min=max;
               for(int i=1;i<=max;i++){
                       int sumtime=0;
                       for(int j=0;j<d;j++)
                               sumtime+=(arr[j]-1)/i;
                       if(min>sumtime+i)
                                        min=sumtime+i;
               } 
               cout<<"Case #"<<c++<<": "<<min<<endl;
    }
    return 0;
}
