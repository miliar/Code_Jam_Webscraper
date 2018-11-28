#include <bits\stdc++.h>

std::vector < char > solve(std::string n);

using namespace std;

int main(){
   int T;
   cin >> T;
   
   for (int i = 0; i < T; i++){
       string n;
       cin >> n;
       
       vector < char > ret = solve(n);
       
       cout << "Case #" << i + 1 << ": ";
       for (int j = 0; j < ret.size(); j++){
           cout << ret[j];
       }
       cout << endl;
   }
}

vector < char > solve(string n){
    vector < char > ret;
    ret.push_back(n[0]);
    for (int i = 1; i < n.length(); i++){
        if (n[i] >= ret.front()){
            ret.emplace(ret.begin() , n[i]); 
        }else{
            ret.push_back(n[i]);
        }
    }
    
    return ret;
}