# include <bits/stdc++.h>
using namespace std;

struct game{
    int c, j, dif;
    void setVal(int code, int jam){
        c = code;
        j = jam;
        dif = abs(c-j);
    }
    bool operator < (const game &n) const{
        if (dif < n.dif) return true;
        if (dif > n.dif) return false;
        if (c < n.c) return true;
        if (c > n.c) return false;
        if (j < n.j) return true;
        return false;
    }
};

int main(){
    freopen("B-small-attempt0.in", "r", stdin);
    freopen("B-small-output.txt", "w", stdout);
    int cases, caseno=0, numC[3][10], numJ[3][10], _c[1005], _j[1005], len;
    vector <game> match;
    game temp;
    char C[20], J[20];
    scanf("%d", &cases);
    while(cases--){
        match.clear();
        scanf("%s %s", C, J);
        len = strlen(C);
        //printf("%d\n", len);
        for (int i=0; i<len; i++){
            if (C[i]=='?'){
                for (int j=0; j<10; j++) numC[i][j] = j;
            }
            else{
                for (int j=0; j<10; j++) numC[i][j] = C[i]-'0';
            }
            if (J[i]=='?'){
                for (int j=0; j<10; j++) numJ[i][j] = j;
            }
            else{
                for (int j=0; j<10; j++) numJ[i][j] = J[i]-'0';
            }
        }
        if (len==3){
            for (int i=0; i<10; i++){
                for (int j=0; j<10; j++){
                    for (int k=0; k<10; k++){
                        _c[i*100+j*10+k] = (numC[0][i]*100) + (numC[1][j]*10) + numC[2][k];
                        _j[i*100+j*10+k] = (numJ[0][i]*100) + (numJ[1][j]*10) + numJ[2][k];
                    }
                }
            }
        }
        else if (len==2){
            for (int i=0; i<10; i++){
                for (int j=0; j<10; j++){
                    _c[i*10+j] = (numC[0][i]*10) + numC[1][j];
                    _j[i*10+j] = (numJ[0][i]*10) + numJ[1][j];
                }
            }
        }

        else{
            for (int i=0; i<10; i++){
                _c[i] = numC[0][i];
                _j[i] = numJ[0][i];
            }
        }

        int upto = 1;
        for (int i=0; i<len; i++) upto*=10;

        for (int i=0; i<upto; i++){
            for (int j=0; j<upto; j++){
                temp.setVal(_c[i], _j[j]);
                //printf ("%d:%d %d:%d\n", i, _c[i], j, _j[j]);
                //getchar();
                match.push_back(temp);
            }
        }
        sort(match.begin(), match.end());
        temp = match[0];
        //printf("%d %d\n", temp.c, temp.j);
        printf("Case #%d: ", ++caseno);
        if (temp.c/100==0 && len==3) printf("0");
        if (temp.c/10==0 && len>=2) printf("0");
        printf("%d ", temp.c);
        if (temp.j/100==0 && len==3) printf("0");
        if (temp.j/10==0 && len>=2) printf("0");
        printf("%d\n", temp.j);
    }
    return 0;
}
