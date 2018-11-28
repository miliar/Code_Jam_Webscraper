#include <bits\stdc++.h>

std::vector < int > solve(std::vector< std::vector < int > > lists);
int cmp(std::vector < int > a, std::vector < int > b);

using namespace std;

int main(){
    int T;
    cin >> T;
   
    for (int i = 0; i < T; i++){
        int n;
        cin >> n;
        
        vector < vector < int > > lists;
        lists.resize(2*n - 1);
        
        for (int j = 0; j < 2*n - 1; j++){
            for (int k = 0; k < n; k++){
                int x;
                cin >> x;
                lists[j].push_back(x);
            }
        }
        vector < int > ret = solve( lists );

        cout << "Case #" << i + 1 << ":";
        for (int j = 0; j < ret.size(); j++){
           cout << " " << ret[j];
        }
        cout << endl;
    }
}

vector < int > solve( vector< vector < int > > lists ){
    
    map <int , int > mymap;
    for (int i = 0; i < lists.size(); i++){
        for (int j = 0; j < lists[i].size(); j++){
            mymap[lists[i][j]] ++;
        }
    }
    
    vector < int > ret;
    
    for (auto a: mymap){
        if (a.second % 2 == 1){
            ret.push_back(a.first);
        }
    }
    
    sort(ret.begin(), ret.end());
    
    return ret;
    
 
}

int cmp(vector < int > a, vector < int > b){
    return a[0] > b[0];
}