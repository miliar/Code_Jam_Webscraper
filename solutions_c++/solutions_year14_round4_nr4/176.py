#include<fstream>
#include<vector>
#include<set>
#include<string.h>
using namespace std;

ifstream fin("trie.in");
ofstream fout("trie.out");

int T, M, N;
string str[10];

int trie_size(vector<string> use){
    set<string> pfx;
    for(int i=0; i<use.size(); i++)
        for(int pf=0; pf<=use[i].length(); pf++)
            pfx.insert(use[i].substr(0, pf));
    return pfx.size();
}

int main(){
    int T;
    fin >> T;
    for(int t=0; t<T; t++){
        
        fin >> M >> N;
        for(int i=0; i<M; i++)
            fin >> str[i];
                
        int bigm = 1;
        for(int i=0; i<M; i++)
            bigm *= N;
            
        int worst = 0;
        int ways = 0;
            
        for(int mask = 0; mask < bigm; mask++){
            bool good = true;
            int ans = 0;
            
            for(int serv = 0; serv < N; serv++){
                vector<string> use;
                int temp = mask;
                for(int ws = 0; ws < M; ws++){
                    if(temp%N == serv)
                        use.push_back(str[ws]);
                    temp /= N;
                }
                if(use.size() == 0){ good = false; break; }
                ans += trie_size(use);
            }
            
            if(good){
                if(ans > worst){ worst = ans; ways = 1; }
                else if(ans == worst) ways ++;
            }
        }
                
        fout << "Case #" << t+1 << ": ";
        fout << worst << " " << ways << endl;
    }
}
