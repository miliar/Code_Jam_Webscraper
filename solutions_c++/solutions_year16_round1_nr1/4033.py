
#include <cstdlib>
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <math.h>
#include <string.h>

using namespace std;
int main(int argc, char** argv) {
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    
    int t;
    cin>>t;
    for(int i=1;i<=t;i++){
        string ans;
        char inp[100000];
        cin>>inp;
        ans = inp[0];
        for(int j=1;inp[j]!='\0';j++){
            if(ans[0]>inp[j]){
                ans = ans + inp[j];
            }else{
                ans =  inp[j]+ ans;
            }
        }
        
        cout<<"Case #"<<i<<": "<<ans<<endl;
    }
    return 0;
}
