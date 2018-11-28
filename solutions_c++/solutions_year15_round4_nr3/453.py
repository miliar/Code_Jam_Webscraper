#include <iostream>
#include <algorithm>
#include <map>
#include <cstdio>
#include <cstring>
#include <string>
#include <set>
#include <queue>
using namespace std;
#define ll long long
#define MA 10005
int n;
vector<string> split(string str){
    int length = str.length();
    //cout << length << endl;
    vector<string> ret;
    if (str[length - 1] == '\n'){
        --length;
    }
    int site = 0;
    while (site < length){
        string word;
        while (site < length && str[site] != ' '){
            word += str[site];
            ++site;
        }
        //cout << word << endl;
        ret.push_back(word);
        ++site;
    }
    return ret;
}
int vis[205];
int main()
{
    freopen("/Users/momo/Desktop/xcode_data/C-small-attempt0.in", "r", stdin);
    freopen("/Users/momo/Desktop/xcode_data/out.txt", "w", stdout);

    int cas;
    cin >> cas;
    int cc = 0;
    while (cas-- > 0){
        cin >> n;
        getchar();
        string str1;
        getline(cin, str1);
        vector<string> english = split(str1);
        set<string> already;
        set<string> eng;
        for (int i = 0; i < english.size(); ++i){
            eng.insert(english[i]);
            //cout << english[i] << endl;
        }
        getline(cin, str1);
        vector<string> franch = split(str1);
        set<string> fran;
        for (int i = 0; i < franch.size(); ++i){
            fran.insert(franch[i]);
        }
        set<string>::iterator it = eng.begin();
        for (; it != eng.end(); ++it){
            if (fran.find(*it) != fran.end()){
                already.insert(*it);
            }
        }
        it = already.begin();
        for (; it != already.end(); ++it){
            eng.erase(*it);
            fran.erase(*it);
        }
        vector<vector<string>> sentences;
        for (int i = 0; i < n - 2; ++i){
            getline(cin, str1);
            vector<string> vec = split(str1);
            set<string> ts;
            for (int j = 0; j < vec.size(); ++j){
                ts.insert(vec[j]);
            }
            vec.clear();
            set<string>::iterator it2 = ts.begin();
            for (; it2 != ts.end(); ++it2){
                vec.push_back(*it2);
            }
            sentences.push_back(vec);
        }
        memset(vis, 0, sizeof(vis));
        for (int i = 0; i < n - 2; i++){
            int maxx = 0;
            int chose = 0;
            int maxx_site = 0;
            for (int j = 0; j < sentences.size(); ++j){
                if (vis[i] == 1)
                    continue;
                int en = 0;
                int fn = 0;
                for (int k = 0; k < sentences[j].size(); ++k){
                    if (already.find(sentences[j][k]) != already.end()){
                        continue;
                    }
                    if (fran.find(sentences[j][k]) != fran.end()){
                        en++;
                    }
                    if (eng.find(sentences[j][k]) != eng.end()){
                        fn++;
                    }
                }
                if (max(en, fn) >= maxx){
                    maxx_site = j;
                    chose = 0;
                    if (fn < en)
                        chose = 1;
                }
            }
            vis[maxx_site] = 1;
            for (int j = 0; j < sentences[maxx_site].size(); ++j){
                string word = sentences[maxx_site][j];
                if (already.find(word) != already.end())
                    continue;
                if (chose == 0){
                    if (fran.find(word) != fran.end()){
                        already.insert(word);
                        fran.erase(word);
                    }
                    else{
                        eng.insert(word);
                    }
                }
                else{
                    if (eng.find(word) != eng.end()){
                        already.insert(word);
                        eng.erase(word);
                    }
                    else{
                        fran.insert(word);
                    }
                }
            }
        }
        printf("Case #%d: %d\n", ++cc, already.size());
    }
    return 0;
}

