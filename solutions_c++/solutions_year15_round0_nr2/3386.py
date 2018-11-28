#include <bits/stdc++.h>
#pragma comment(linker, "/stack:256000")

using namespace std;


map< vector<int>,int > mapeo;
int brute(vector<int> c){
    sort(c.begin(),c.end());

    if(mapeo.find(c) != mapeo.end()){
        return mapeo[c];
    }

    int answer = c.back();
    if(answer <= 3) return answer;

    for(int i = 0; i < c.size(); ++i){
        if(c[i] <= 3){
            continue;
        }

        int tmp = c[i];
        vector<int> copia = c;
        swap(copia.back(),copia[i]);
        copia.pop_back();

        copia.push_back(tmp / 2);
        copia.push_back( tmp - (tmp / 2));
        answer = min(answer , 1 + brute(copia));
    }

    for(int i = 0; i < c.size(); ++i){
        c[i]--;
    }
    answer = min(answer , 1 + brute(c));

    for(int i = 0; i < c.size(); ++i){
        c[i]++;
    }

    return mapeo[c] = answer;
}


int main(){

   freopen("/home/docente/B-large.in","r",stdin);
    freopen("on.c","w",stdout);


    //freopen("in.c","r",stdin);


    int tc;
    cin >> tc;

    for(int nc = 1; nc <= tc; nc++){

        int dinners;
        cin >> dinners;

        vector<int> c;
        for(int i = 0; i < dinners; ++i){
            int x; cin >> x;
            c.push_back(x);
        }
        int cota = *max_element(c.begin(),c.end());

        int answer = 1<<30;
        for(int i = 1; i <= cota; ++i){
            int tmp = i;
            for(int j = 0; j < dinners; ++j){
                if(c[j] > i)
                tmp += (c[j] + i - 1 ) / i - 1;
            }
            answer = min(answer , tmp);
        }

        printf("Case #%d: %d\n",nc,answer);

    }


	return 0;
}




