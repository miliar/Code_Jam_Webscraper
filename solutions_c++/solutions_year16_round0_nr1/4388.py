#include<cstdio>
#include<iostream>
#include<vector>
#include<algorithm>
#include<queue>
#include<memory.h>
#include<map>
using namespace std;


void test_case(){
    int n;
    cin >> n ;
    vector<bool> chk(11,false);
    if( n == 0 ){
        cout << "INSOMNIA" << endl;
        return;
    }
    int cnt = 0 ;
    int last = n;
    for(int i = 1; cnt < 10 ; i++){
        int val = n * i ;
        
        last = val;
        while(val > 0){
            int digit = val % 10;
            val /= 10;
            if(chk[digit] == false){
                cnt ++;
                chk[digit] = true;
            }
        }
    }
    cout << last << endl;
}
int main(){
    int t;
    cin >> t;
    for(int i = 1; i <= t; i ++){
        printf("Case #%d: ",i);
        test_case();
    }
    return 0;
}