#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <inttypes.h>
#include <string.h> 
#include <vector>
using namespace std;


int main(){
    int T; cin>>T;
    for (int j = 1; j <=T ; j++) {
        uint16_t max_shy; cin>>max_shy;
        string num_str; cin>>num_str;
        int digit;
        vector<int> shy_list;shy_list.reserve(max_shy+1);
       // std::cout<<"Max shy "<<max_shy<<"\n";
        for (unsigned int i = 0; i < num_str.size(); i++) {
            digit = (int) num_str[i] - (int)('0');
            shy_list.push_back(digit);
        }
        
//        for (unsigned int i = 0; i < shy_list.size(); i++) {
//            cout<<shy_list[i];
//        }
//        cout<<"\n";
        
        uint16_t cur_count = 0;
        uint16_t added_count = 0;
        for (unsigned int i = 0; i < shy_list.size(); i++) {
            if(i == 0){
                cur_count += shy_list[i];
            }else if(cur_count >= i ){
                cur_count += shy_list[i];
            }else{
                added_count = added_count + i - cur_count;
                cur_count = i + shy_list[i];
            }
        }
        cout<<"Case #"<<j<<": "<<added_count<<"\n";
    }
    
    return 0;
}