#include <iostream>
#include <vector>
#include <unordered_set>
#include <unordered_map>
#include <stack>
#include <queue>
#include <string>
#include <fstream>
#include <sstream>
#include <algorithm>
using namespace std;

int main(){
	/*int T; cin>>T;
    for(int t=0;t<T;t++){
        int K, C, S;
        cin>>K>>C>>S;
        vector<long long> places, chunks;
        for(int i=0;i<K;i++) places.push_back(i);
        long long chunk_size = 1;
        for(int c=1;c<C+1;c++){
            for(int i=0;i<places.size();i++){
                if (i<places.size()-1){
                    places[i] = (places[i]%chunk_size)*chunk_size+places[i+1];
                    places.erase(places.begin()+i+1);
                }
            }
            chunk_size*=K;
        }
        printf("Case #%d: ", t+1);
        if (places.size()>S) cout<<"IMPOSSIBLE"<<endl;
        else {for(int i=0;i<places.size();i++) printf("%lld ", places[i]+1); cout<<endl;}
     }*/
     int T; cin>>T;
     for(int t=0;t<T;t++){
         int K, C, S; cin>>K>>C>>S;;
         printf("Case #%d: ", t+1);
         for(int i=0;i<K;i++) printf("%d ", i+1); cout<<endl;
     }
}