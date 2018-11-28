#include<fstream>
#include<map>
using namespace std;

ifstream fin("updown.in");
ofstream fout("updown.out");

int T, N;
int val[1005];
map<int, int> idx;
int dp[1005][1005];

int main(){
    int T;
    fin >> T;
    for(int t=0; t<T; t++){
        fin >> N;
        for(int i=0; i<N; i++){
            fin >> val[i];
            idx[val[i]] = i;
        }
        sort(val, val + N);
        
        for(int w = 0; w<N; w++){
            for(int s = 0; s+w<N; s++){
                if(w == 0) dp[w][s] = 0;
                else{
                    int small = val[s];
                    int low = 0, high = 0;
                    for(int t=s+1; t<=s+w; t++)
                        if(idx[val[t]] < idx[small]) low++;
                        else high++;
                    dp[w][s] = min(low, high) + dp[w-1][s+1];
                }
            }
        }
        
        fout << "Case #" << t+1 << ": ";
        fout << dp[N-1][0] << endl;
    }
}
