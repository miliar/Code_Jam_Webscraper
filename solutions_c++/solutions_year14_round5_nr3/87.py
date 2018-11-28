#include<iostream>
#include<fstream>
#include<string>
#include<bitset>
#include<algorithm>
#include<set>
using namespace std;

bool possible[16][1<<15];

int cnt(int i){
    if (i==0) return i;
    return (i&1) + cnt(i>>1);
}

int main(){
    ifstream in("C.in"); ofstream out("C.out");
    int T;
    in>>T;

    for (int t=0;t<T;t++){
        out<<"Case #"<<t+1<<": ";
        int N;
        in>>N;
        bool enters[N];
        int person[N];
        int ID[2001];
        int IDs = 0;
        for (int i=0;i<2001;i++) ID[i] = -1;
        for (int i=0;i<N;i++){
            string s;
            int id;
            in>>s>>id;
            enters[i] = (s[0] == 'E');
            if (id==0){
                person[i] = -1;
            }
            else{
                if (ID[id] == -1) ID[id] = IDs++;
                person[i] = ID[id];
            }
        }


        for (int i=1;i<N+1;i++) for (int j=0;j<(1<<N);j++) possible[i][j] = false;
        for (int j=0;j<(1<<N);j++) possible[0][j] = true;

        for (int i=0;i<N;i++){
            for (int j=0;j<(1<<N);j++){
                if (possible[i][j]){
                    if (person[i] >= 0){
                        if (!enters[i]){
                            if (j & (1<<person[i])){
                                possible[i+1][j ^ (1<<person[i])] = true;
                            }
                        }
                        else{
                            if ((j & (1<<person[i])) == 0){
                                possible[i+1][j ^ (1<<person[i])] = true;
                            }
                        }
                    }
                    else{
                        for (int k = 0; k<N;k++){
                            if (!enters[i]){
                                if (j & (1<<k)){
                                    possible[i+1][j ^ (1<<k)] = true;
                                }
                            }
                            else{
                                if ((j & (1<<k)) == 0){
                                    possible[i+1][j ^ (1<<k)] = true;
                                }
                            }
                        }
                    }
                }
            }
        }
        int ans = N+1000;
        for (int i=0;i<(1<<N);i++){
            if (possible[N][i]) ans = min(ans, cnt(i));
        }
        if (ans > N){
            out<<"CRIME TIME\n";
        }
        else out<<ans<<"\n";
    }
}
