#include<iostream>

#include<vector>
#include<fstream>
#include<sstream>
#include<map>
#include<set>

using namespace std;

typedef unsigned long long ull;

struct Key{
    ull keys[4];

    bool operator<(Key _key)const{
        return (this->keys[0]<_key.keys[0]||this->keys[1]<_key.keys[1]||this->keys[2]<_key.keys[2]||this->keys[3]<_key.keys[3]);
    }

    bool operator==(Key _key)const{
        return (this->keys[0]==_key.keys[0]&&this->keys[1]==_key.keys[1]&&this->keys[2]==_key.keys[2]&&this->keys[3]==_key.keys[3]);
    }
};

void setKey(Key& key, int pos){
    key.keys[pos/64] |= (((ull)1)<<(pos%64));
}

void unsetKey(Key& key, int pos){
    key.keys[pos/64] &= ~(((ull)1)<<(pos%64));
}

bool isKeySet(Key& key, int pos){
    ull val = (key.keys[pos/64]&(((ull)1)<<(pos%64)));
    return (val>0);
}

map<Key, bool> dp;
map<int, int> initKeyCnt;
map<int, vector<int> > chestKeys;
map<int, set<int> > keyToChest;
map<int, int> chestToKey;
int chestCnt;

bool isPossible(Key& key){
    if(dp.find(key) != dp.end()){
        return dp[key];
    }

    bool finished=true;
    for(int ch=1;ch<=chestCnt;ch++){
        if(!isKeySet(key, ch)){
            finished=false;
            break;
        }
    }
    if(finished){
        dp[key]=true;
        return true;
    }

    //get keys
    map<int, int> avlbKeys = initKeyCnt;
    for(int i=1;i<=chestCnt;i++){
        if(isKeySet(key, i)){
            avlbKeys[chestToKey[i]]--;
            for(int j=0;j<chestKeys[i].size();j++)
                avlbKeys[chestKeys[i][j]]++;
        }
    }

    bool possible=false;
    for(int i=1;i<=chestCnt;i++){
        if(isKeySet(key, i)) continue;

        if(avlbKeys[chestToKey[i]]>0){
            setKey(key, i);
            bool ret=isPossible(key);
            unsetKey(key, i);

            if(ret){
                possible=true;
                break;
            }
        }
    }

    dp[key]=possible;

    return possible;
}

void findChests(Key& key, vector<int>& chests){
    if(chests.size()>=chestCnt) return;

    //get keys
    map<int, int> avlbKeys = initKeyCnt;
    for(int i=1;i<=chestCnt;i++){
        if(isKeySet(key, i)){
            avlbKeys[chestToKey[i]]--;
            for(int j=0;j<chestKeys[i].size();j++)
                avlbKeys[chestKeys[i][j]]++;
        }
    }

    for(int i=1;i<=chestCnt;i++){
        if(isKeySet(key, i)) continue;

        bool finished=false;
        if(avlbKeys[chestToKey[i]]>0){
            setKey(key, i);
            if(dp[key]){
                chests.push_back(i);
                findChests(key, chests);
                finished=true;
            }
            unsetKey(key, i);
        }
        if(finished) return;
    }
}

int main(int argc, char* argv[])
{
    if(argc != 2){
        cout<<argv[0]<<" input_file"<<endl;
        return 0;
    }

    fstream file(argv[1]);

    char line[1024];
    file.getline(line, 1024);

    int T = atoi(line);

    for(int t=0;t<T;t++){
        dp.clear();
        keyToChest.clear();
        initKeyCnt.clear();
        chestKeys.clear();
        chestToKey.clear();

        int K,N;
        file.getline(line, 1024);
        stringstream ss(line);
        ss>>K>>N;

        //get init keys
        file.getline(line, 1024);
        stringstream ss1(line);
        while(K-->0){
            int tmp = 0;
            ss1>>tmp;
            initKeyCnt[tmp]++;
        }

        chestCnt=N;

        //get chest mapping
        for(int n=1;n<=N;n++){
            file.getline(line, 1024);
            stringstream ss2(line);

            int Ti,Ki;
            ss2>>Ti>>Ki;
            keyToChest[Ti].insert(n);
            chestToKey[n] = Ti;

            vector<int> keys;
            while(Ki-->0){
                int tmp=0;
                ss2>>tmp;
                keys.push_back(tmp);
            }

            chestKeys[n]=keys;
        }

        //parsing input data finished.......
        Key key = {0};
        bool possible=isPossible(key);

        if(!possible){
            cout<<"Case #"<<t+1<<": "<<"IMPOSSIBLE"<<endl;
            continue;
        }

        memset(&key, 0x0, sizeof(key));
        vector<int> chests;
        findChests(key, chests);

        cout<<"Case #"<<t+1<<": ";

        for(int i=0;i<chestCnt;i++){
            cout<<chests[i];
            if(i<chestCnt-1)
                cout<<" ";
        }
        cout<<endl;
    }
    return 0;
}
