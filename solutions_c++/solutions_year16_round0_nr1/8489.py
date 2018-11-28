
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>

using namespace std;

int main(int argc, char** argv) {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int n;
    cin>>n;
    for(int i=1;i<= n;i++){
        int num;
        cin>>num;
        if(num == 0){
            cout<<"Case #"<<i<<": INSOMNIA"<<endl;
        }else{
            int has[10] = {0};
            int cnt = 0;
            int ans = 0;
            int multi = 1;
            while(cnt <10){
                int temp = num* multi;
                ans= temp;
                while(temp>0){
                    int tt = temp %10;
                    if(has[tt]==0){
                        has[tt]++;
                        cnt++;
                    }
                    temp = temp/10;
                }
                multi++;
                
            }
            
            
            cout<<"Case #"<<i<<": "<<ans<<endl;
        }
    }
    
    return 0;
}

