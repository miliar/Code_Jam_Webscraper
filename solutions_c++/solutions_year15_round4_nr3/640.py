#include <bits/stdc++.h>

using namespace std;


typedef long long LL;


struct Case {

    int N;
    map<string, int> words;
    vector<vector<int>> lines;
    vector<bool> english;
    int result;
    int nwords;

    void input(){
        nwords = 0;
        string line;
        getline(cin, line);
        stringstream s(line);
        s >> N;
        
        lines.resize(N);
        for(int i = 0; i < N; i++){
            getline(cin, line);
            stringstream ss(line);

            string word;
            while(ss >> word){
                if(words.count(word) == 0){
                    words[word] = nwords++;
                }
                lines[i].push_back(words[word]);

            }
        }
    }

    void check(){
        vector<bool> en(nwords+1, false), fr(nwords+1, false);
        int cnt = 0;
        for(int i = 0; i < N; i++){
            for(int s : lines[i]){
                if(english[i] && !en[s]){
                    if(fr[s]) cnt++;
                    en[s] = true;
                }
                if(!english[i] && !fr[s]){
                    if(en[s]) cnt++;
                    fr[s] = true;
                }
            }
        }
        result = min(result, cnt);
    }

    void brute(int v){
        if(v == N){ check(); return; }
        english[v] = false;
        brute(v+1);
        english[v] = true;
        brute(v+1);
    }

    void run(){
        english.resize(N);
        english[0] = true;
        english[1] = false;
        result = 1e9;
        brute(2);

        printf("%d\n", result);
    }
};

int main(){
    int numTests;
    scanf("%d", &numTests);
    string SSSS;
    getline(cin, SSSS);

    for(int i = 1; i <= numTests; i++){
        cerr << i << " " << numTests << endl;
        Case C;
        C.input();
        printf("Case #%d: ", i);
        C.run();
    }
}
