#include <fstream>
#include <iostream>
#include <set>
#include <vector>
#include <queue>
#include <map>

#define WAIT system("pause")
#define MP make_pair
#define PB push_back
#define FORi(i,a,b) for (int i=a; i<b; i++)

using namespace std;

int main(){
    ifstream fin("in.txt");
    ofstream fout("out.txt");
    int t;
    string s;
    fin >> t;
    int cnt[26], need[10][26]={0};
    vector<int> ans(10,0);
    string word[10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};
    FORi(i,0,10)
        FORi(j,0,word[i].size())
            need[i][word[i][j]-'A']++;
    FORi(q,0,t){
        FORi(j,0,26)
            cnt[j]=0;
        fin >> s;
        FORi(i,0,s.size())
            cnt[s[i]-'A']++;   
        
        ans[0]=cnt['Z'-'A'];
        FORi(i,0,word[0].size())
            cnt[word[0][i]-'A'] -= ans[0];
        ans[2]=cnt['W'-'A'];    
        FORi(i,0,word[2].size())
            cnt[word[2][i]-'A'] -= ans[2];
        ans[6]=cnt['X'-'A'];    
        FORi(i,0,word[6].size())
            cnt[word[6][i]-'A'] -= ans[6];
        ans[8]=cnt['G'-'A'];    
        FORi(i,0,word[8].size())
            cnt[word[8][i]-'A'] -= ans[8];
        ans[4]=cnt['U'-'A'];    
        FORi(i,0,word[4].size())
            cnt[word[4][i]-'A'] -= ans[4];
        ans[7]=cnt['S'-'A'];    
        FORi(i,0,word[7].size())
            cnt[word[7][i]-'A'] -= ans[7];
        ans[5]=cnt['V'-'A'];    
        FORi(i,0,word[5].size())
            cnt[word[5][i]-'A'] -= ans[5];
        ans[3]=cnt['R'-'A'];    
        FORi(i,0,word[3].size())
            cnt[word[3][i]-'A'] -= ans[3];
        ans[1]=cnt['O'-'A'];    
        FORi(i,0,word[1].size())
            cnt[word[1][i]-'A'] -= ans[1];
        ans[9]=cnt['I'-'A'];    
        FORi(i,0,word[9].size())
            cnt[word[9][i]-'A'] -= ans[9];
        
        fout << "Case #" << q+1 << ": ";
        FORi(i,0,ans.size()){
            FORi(j,0,ans[i])
                fout << i;
            ans[i]=0;
        }
        fout << endl;
    }
    //WAIT;
    fin.close();
    fout.close();
    return 0;    
}
