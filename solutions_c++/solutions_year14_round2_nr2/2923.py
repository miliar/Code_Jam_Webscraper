#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
using namespace std;

int t, a, b, k;


int main() {
    
    cin>>t;
    for(int i=0;i<t;i++){
        int counter=0;
        cin>>a>>b>>k;
        for(int m=0;m<a;m++){
            for(int n=0;n<b;n++){
                if(int(m&n)<k){
                    counter++;
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<counter<<endl;
    }
       
        
        
}