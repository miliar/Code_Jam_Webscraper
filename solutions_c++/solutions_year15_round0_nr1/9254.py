#include<iostream>
#include<string>

using namespace std;

int main(){
    int no_t, s_max;
    string s_arr;


    cin>>no_t;
    for(int i=0; i<no_t; i++){
        int num;
        int no_fr = 0;        
        
        cin>>s_max>>s_arr;
        // cout<<s_max<<s_arr;
        int no_req= int(s_arr[0] - '0');
        for(int j=1; j<=s_max; j++){
            num = int(s_arr[j] - '0');
            //cout<<num;
            if(no_req >= j){
                no_req += num;
            }            
            else{
                int cur_fr = j - no_req;
                no_req += cur_fr + num;
                no_fr += cur_fr;
            }
            
        }
        cout<<"Case #"<<i+1<<": "<<no_fr<<endl;
    }
    return 0;
}
