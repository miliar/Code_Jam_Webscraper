
/// CODEJAM PROBLEM A

#include <bits/stdc++.h>
using namespace std;

const int maxN = 55;
int n , R, P , S;

map<char,char> mapeo;


string solve(char ini){

    vector<char> current;
    current.push_back(ini);
    for(int i = 0; i < n; ++i){
        vector<char> tmp;
        for(char elem : current){
            tmp.push_back(elem);
            tmp.push_back(mapeo[elem]);
        }
        current = tmp;
    }
    vector<string> tt;
    for(char elem : current){
        tt.push_back(string() + elem);
    }
    /// GET LEXILOGRAFIC
    for(int i = 0; i < n; ++i){
        vector<string> other;
        for(int k = 0; k + 1 < tt.size(); k+=2){
            string x = tt[k] + tt[k + 1];
            string y = tt[k + 1] + tt[k];
            other.push_back(min(x , y));
        }
        tt = other;
    }
    assert(tt.size() == 1);
    return tt[0];
}

int main(){
   freopen("A-large.in","r",stdin);
   freopen("on.c","w",stdout);

    mapeo['P'] = 'R';
    mapeo['R'] = 'S';
    mapeo['S'] = 'P';

    int tc;
    cin >> tc;

    for(int number_Case = 1; number_Case <= tc; number_Case++){
            cin >> n >> R >> P >> S;

            string answer = "IMPOSSIBLE";
            string current = solve('P');
            int cR = 0 , cP = 0 , cS = 0;
            for(char elem : current){
                if(elem == 'R'){
                    cR++;
                }
                if(elem == 'P'){
                    cP++;
                }
                if(elem == 'S'){
                    cS++;
                }
            }
            if(cR == R && cP == P && cS == S && (answer == "IMPOSSIBLE" || current < answer)){
                answer = current;
            }


            current = solve('R');
            cR = 0 , cP = 0 , cS = 0;
            for(char elem : current){
                if(elem == 'R'){
                    cR++;
                }
                if(elem == 'P'){
                    cP++;
                }
                if(elem == 'S'){
                    cS++;
                }
            }

            if(cR == R && cP == P && cS == S && (answer == "IMPOSSIBLE" || current < answer)){
                answer = current;
            }

            current = solve('S');
            cR = 0 , cP = 0 , cS = 0;
            for(char elem : current){
                if(elem == 'R'){
                    cR++;
                }
                if(elem == 'P'){
                    cP++;
                }
                if(elem == 'S'){
                    cS++;
                }
            }
            if(cR == R && cP == P && cS == S && (answer == "IMPOSSIBLE" || current < answer)){
                answer = current;
            }

            printf("Case #%d: ",number_Case);
            cout << answer << endl;
    }



    return 0;
}
