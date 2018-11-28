#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <queue>
#include <map>
#include <string>


using namespace std;

#define true 1
#define false 0

int main(){
    int cases;
    cin>>cases;
    for(int n=1; n<=cases; ++n){
        cout<<"Case #"<<n<<":";
        int rows;
        cin>>rows;
        //cout<<"rows="<<rows<<endl;
        int num;
        map<int, int> times;
        priority_queue<int, vector<int>, std::greater<int> > missing;
        for(int i=0; i<(rows*2-1)*rows; ++i){
            cin>>num;
            //cout<<num<<" ";
            if(times.count(num)==0){
                times[num] = 1;
            } else {
                ++times[num];
            }
        }
        for(map<int,int>::iterator it=times.begin(); it!=times.end(); ++it){
           // cout<<"num: "<<it->first<<" times:"<<it->second<<endl;
            if(it->second%2==1){
                missing.push(it->first);
            }
        }
        while(!missing.empty()){
            cout<<" "<<missing.top();
            missing.pop();
        }
        cout<<endl;
    }
    
}