#include <iostream>
#include <istream>
#include <sstream>
using namespace std;
int main(){
    int numberofcases;
    cin>>numberofcases;
    int result[numberofcases];
    for(int k=0;k<numberofcases;k++)
    result[k]=0;
    for(int i =0;i<numberofcases;i++){
            long long r,t;
            cin>>r>>t;
            while(true){
                        t= t-(2*r+1);
                        r+=2;
                        if(t>=0){
                               result[i]++; }
                        else     {break;}   
                        }
            }
            
            for(int i=0;i<numberofcases;i++){
            cout<<"Case #"<<i+1<<": "<<result[i]<<endl;
            
            }
    int l;
    cin>>l;
    
    return 0;}
