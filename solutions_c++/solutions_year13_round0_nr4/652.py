#include <iostream>
#include <map>
#include <vector>
#include <set>
using namespace std;

struct Chest {
    int key;
    int nKeys;
    vector<int> keys;
} chests[20];

int K, N;
map<int, int> myKeys;

void addKey(int key, map<int, int> &keySet)
{
    map<int, int>::iterator it = keySet.find(key);
    
    if (it != keySet.end()) {
        ++it->second;
    } else {
        keySet.insert(make_pair(key, 1));
    }
    
    //cout << "Added key: " << key << endl;
    //cout << myKeys.size() << endl;
}

bool removeKey(int key, map<int, int> &keySet)
{
    map<int, int>::iterator it = keySet.find(key);
    
    if (it == keySet.end()) {
        return false;
    }
    
    --it->second;
    if (it->second == 0) {
        keySet.erase(it);
    }
    
    return true;
}

bool canSolve(set<int> &opened)
{
    map<int, int> keysLeft = myKeys;
    vector<int> unopened;
    int chest;
    
    for (int i = 0; i < N; i++) {
        if (opened.find(i) == opened.end()) {
            unopened.push_back(i);
        }
    }
    
    //all the keys that can still be used
    for (int i = 0; i < unopened.size(); i++) {
        chest = unopened[i];
    
        for (int j = 0; j < chests[chest].keys.size(); j++) {
            addKey(chests[chest].keys[j], keysLeft);
        }
    }
    
    map<int, int> tempKeysLeft = keysLeft;
    for (int i = 0; i < unopened.size(); i++) {
        chest = unopened[i];
    
        if (! removeKey(chests[chest].key, tempKeysLeft)) {
            return false;
        }
    }
    
    //check for each chest if it's possible to open it
    for (int i = 0; i < unopened.size(); i++) {
        chest = unopened[i];
    
        for (int j = 0; j < chests[chest].keys.size(); j++) {
            removeKey(chests[chest].keys[j], keysLeft);
        }
    
        if (! removeKey(chests[chest].key, keysLeft)) {
            return false;
        } else {
            addKey(chests[chest].key, keysLeft);
        }
    
        for (int j = 0; j < chests[chest].keys.size(); j++) {
            addKey(chests[chest].keys[j], keysLeft);
        }
    }
    //cout << "I can still solve this" << endl;
    return true;
}


void closeChest(int chest)
{
    //readd chest key
    addKey(chests[chest].key, myKeys);
    
    //remove chest keys
    for (int i = 0; i < chests[chest].keys.size(); i++) {
        removeKey(chests[chest].keys[i], myKeys);
    }
}

bool canOpenAndOpen(int chest)
{
    if (! removeKey(chests[chest].key, myKeys)) {
        return false;
    }
    
    //add chest keys
    for (int i = 0; i < chests[chest].keys.size(); i++) {
        addKey(chests[chest].keys[i], myKeys);
    }
    
    return true;
}

bool dfs(set<int> &opened, vector<int> &path) {
    if (opened.size() == N) {
        return true;
    }
    
    if( !canSolve(opened)) {
        return false;
    }
    
    for (int i = 0; i < N; i++) {
         if (opened.find(i) == opened.end() && canOpenAndOpen(i)) {
            //cout << "Opened: " << i << " " << path.size() << endl;
            //cout << myKeys.size() << endl;
         
            opened.insert(i);
            path.push_back(i+1);
            
            if (dfs(opened, path)) {
                return true;
            }
            
            opened.erase(i);
            path.pop_back();
            closeChest(i);
         }
    }
    
    return false;
}

void solve(int case_) {
    set<int> opened;
    vector<int> path;
    
    cout << "Case #" << case_ << ": "; 
    
    if (!canSolve(opened) || !dfs(opened, path)) {
        cout << "IMPOSSIBLE" << endl;
    } else {
        cout << path[0];
        
        for (int i = 1; i < path.size(); i++) {
            cout << " " << path[i];
        }
        
        cout << endl;
    }
}

int main()
{
    int T, key, case_ = 0;
    
    cin >> T;
    
    while (T--) {
        cin >> K >> N;
        myKeys.clear();
        ++case_;
        
        for (int i = 0; i < K; i++) {
            cin >> key;
            addKey(key, myKeys);
        }
        
        for (int i = 0; i < N; i++) {
            cin >> chests[i].key >> chests[i].nKeys;
            chests[i].keys.clear();
            
            for (int j = 0; j < chests[i].nKeys; j++) {
                cin >> key;
                chests[i].keys.push_back(key);
            }
        }
        
        solve(case_);
    
    }
    
    return 0;
}
