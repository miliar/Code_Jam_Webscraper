#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;


int main(){
    int TC;
    scanf("%d", &TC);
    for(int c = 1; c <= TC; c++){
        int D, tmp;
        vector<int> vec;
        vec.clear();
        scanf("%d", &D);
        for(int i = 0; i < D; i++){
            scanf("%d", &tmp);
            vec.push_back(tmp);
        }
        sort(vec.begin(), vec.end());
        int minim = 999999999;


        for(int i = 1; i <= vec.back(); i++){
            int cnt = 0;
            for(unsigned int j = 0; j < vec.size(); j++){
                if(vec[j] >= i){
                    cnt += vec[j] / i;
                    if(vec[j] % i == 0) cnt--;
                }
                //printf("CNT: %d %d\n", i, cnt);
            }
            minim = min(minim, cnt + i);
        }



        printf("Case #%d: %d\n", c, minim);
    }
}


/*
#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> vec;

int recur(int p, int k){
    if(p <= k) return 0;
    if(k == 1) return p - 1;
    return 1 + recur(p / k, k) + recur((p / k) + (p % k), k);
}

int main(){
    int TC;
    scanf("%d", &TC);
    for(int c = 1; c <= TC; c++){
        printf("Case #%d: ", c);
        int D, tmp;
        vec.clear();
        scanf("%d", &D);
        for(int i = 0; i < D; i++){
            scanf("%d", &tmp);
            vec.push_back(tmp);
        }
        sort(vec.begin(), vec.end());
        int minim = 999999999;
        for(int i = 1; i <= vec.back(); i++){
            int cnt = 0;
            for(unsigned int j = 0; j < vec.size(); j++){
                cnt += recur(vec[j], i);
            }
            minim = min(minim, cnt + i);
        }

        printf("%d\n", minim);
    }
}




#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

int minim = 999999999;
string last = "";

void func(int acum, vector<int> vec, string str){

    vector<int> v2;
    for(unsigned int i = 0; i < vec.size(); i++){
        if(vec[i] > 0) v2.push_back(vec[i]);
    }
    if(v2.size() == 0){
        if(acum < minim) last = str;
        //cout << str << endl;
        minim = min(minim, acum);
        return;
    }
    int Mpx = v2.back();

    vector<int> c1;
    for(unsigned int i = 0; i < v2.size(); i++){
        c1.push_back(v2[i] - 1);
    }
    func(acum + 1, c1, str + "K");

    if(Mpx > 1){
        vector<int> c2;
        for(unsigned int i = 0; i < v2.size(); i++){
            c2.push_back(v2[i]);
        }

        c2.pop_back();
        c2.push_back(Mpx / 2);
        c2.push_back((Mpx / 2) + (Mpx % 2));
        sort(c2.begin(), c2.end());

        func(acum + 1, c2, str + "D");
    }

    //return 1 + min(t1, t2);
}


int main(){
    int TC;
    scanf("%d", &TC);
    for(int c = 1; c <= TC; c++){
        int D, tmp;
        vector<int> vec;
        vec.clear();
        scanf("%d", &D);
        for(int i = 0; i < D; i++){
            scanf("%d", &tmp);
            vec.push_back(tmp);
        }
        sort(vec.begin(), vec.end());
        minim = 999999999;
        func(0, vec, "");
        printf("Case #%d: %d\n", c, minim);
        //cout << last << endl;
    }
}




#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

int func(vector<int> vec){

    int t2 = 999999999;

    vector<int> v2;
    for(unsigned int i = 0; i < vec.size(); i++){
        if(vec[i] > 0) v2.push_back(vec[i]);
    }
    if(v2.size() == 0) return 0;
    int Mpx = v2.back();

    vector<int> c1;
    for(unsigned int i = 0; i < v2.size(); i++){
        c1.push_back(v2[i] - 1);
    }
    int t1 = func(c1);

    if(Mpx > 1){
        vector<int> c2;
        for(unsigned int i = 0; i < v2.size(); i++){
            c2.push_back(v2[i]);
        }

        c2.pop_back();
        c2.push_back(Mpx / 2);
        c2.push_back((Mpx / 2) + (Mpx % 2));
        sort(c2.begin(), c2.end());

        t2 = func(c2);
    }

    return 1 + min(t1, t2);
}


int main(){
    int TC;
    scanf("%d", &TC);
    for(int c = 1; c <= TC; c++){
        int D, tmp;
        vector<int> vec;
        vec.clear();
        scanf("%d", &D);
        for(int i = 0; i < D; i++){
            scanf("%d", &tmp);
            vec.push_back(tmp);
        }
        sort(vec.begin(), vec.end());
        printf("Case #%d: %d\n", c, func(vec));
    }
}








#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> vec;

int recur(int p, int k){
    //printf("PK: %d %d\n", p, k);
    if(p <= k) return 0;
    return 1 + recur(p / 2, k) + recur((p / 2) + (p % 2), k);
}

int main(){
    int TC;
    scanf("%d", &TC);
    for(int c = 1; c <= TC; c++){
        printf("Case #%d: ", c);
        int D, tmp;
        vec.clear();
        scanf("%d", &D);
        for(int i = 0; i < D; i++){
            scanf("%d", &tmp);
            vec.push_back(tmp);
        }
        sort(vec.begin(), vec.end());
        int minim = 999999999;
        for(int i = 1; i <= vec.back(); i++){
            int cnt = 0;
            for(unsigned int j = 0; j < vec.size(); j++){
                //printf("D: %d\n", recur(vec[j], i));
                cnt += recur(vec[j], i);
            }
            //printf("CNT: %d\n", cnt + i);
            minim = min(minim, cnt + i);
        }

        printf("%d\n", minim);
    }
}





#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> vec;
int St, time;
void func(){
    int Mpx = vec.back();

    if(Mpx % 2 == 1){
        printf("K\n");
        for(unsigned int i = 0; i < vec.size(); i++){
            vec[i]--;
        }

    }

    int t1 = Mpx + St;
    int t2 = Mpx / 2 + St + 1;
    printf("%d %d\n", t1, t2);
    if(t1 <= t2){
        printf("K\n");
        time += Mpx;
        return;
    }
    printf("D\n");
    vec.pop_back();
    vec.push_back(Mpx / 2);
    vec.push_back(Mpx / 2 + Mpx % 2);
    St++;
    sort(vec.begin(), vec.end());
    return func();
}

int main(){
    int TC;
    scanf("%d", &TC);
    for(int c = 1; c <= TC; c++){
        printf("Case #%d: ", c);
        int D, tmp;
        vec.clear();
        scanf("%d", &D);
        for(int i = 0; i < D; i++){
            scanf("%d", &tmp);
            vec.push_back(tmp);
        }
        sort(vec.begin(), vec.end());
        St = 0;
        time = 0;
        func();
        printf("%d\n", time + St);
    }
}





#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> vec;
int St;
int func(){
    int t1 = vec.back() + St;
    int t2 = vec.back() / 2 + vec.back() % 2 + St + 1;
    if(t1 <= t2) return t1;
    int Mpx = vec.back();
    vec.pop_back();
    vec.push_back(Mpx / 2);
    vec.push_back(Mpx / 2 + Mpx % 2);
    St++;
    sort(vec.begin(), vec.end());
    return func();
}

int main(){
    int TC;
    scanf("%d", &TC);
    for(int c = 1; c <= TC; c++){
        printf("Case #%d: ", c);
        int D, tmp;
        vec.clear();
        scanf("%d", &D);
        for(int i = 0; i < D; i++){
            scanf("%d", &tmp);
            vec.push_back(tmp);
        }
        sort(vec.begin(), vec.end());
        St = 0;
        printf("%d\n", func());
    }
}

*/
