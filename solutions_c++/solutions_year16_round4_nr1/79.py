#include <bits/stdc++.h>

using namespace std;

int T, C=1;

char outro[256];
int N, R, P, S, nvalidos;
string validos[1024];

string ganha(char w, int u) {
    if (u==N) {
        string r = "";
        r = r + w;
        return r;
    }
    string s1 = ganha(w, u+1);
    string s2 = ganha(outro[(int)w], u+1);
    if (s1 < s2)
        return s1 + s2;
    return s2 + s1;
}

int main() {

    outro['P'] = 'R';
    outro['R'] = 'S';
    outro['S'] = 'P';
    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%d %d %d %d",&N,&R,&P,&S);
        string tP = ganha('P', 0);
        string tR = ganha('R', 0);
        string tS = ganha('S', 0);

        nvalidos=0;
        int qtsR, qtsS, qtsP;
        qtsR=qtsS=qtsP=0;
        for (int i=0;i<(int)tP.size();i++)
            if (tP[i]=='S') qtsS++;
            else if (tP[i]=='R') qtsR++;
            else if (tP[i]=='P') qtsP++;
        if (qtsP==P and qtsR==R and qtsS==S)
            validos[nvalidos++] = tP;

        qtsR=qtsS=qtsP=0;
        for (int i=0;i<(int)tR.size();i++)
            if (tR[i]=='S') qtsS++;
            else if (tR[i]=='R') qtsR++;
            else if (tR[i]=='P') qtsP++;
        if (qtsP==P and qtsR==R and qtsS==S)
            validos[nvalidos++] = tR;

        qtsR=qtsS=qtsP=0;
        for (int i=0;i<(int)tS.size();i++)
            if (tS[i]=='S') qtsS++;
            else if (tS[i]=='R') qtsR++;
            else if (tS[i]=='P') qtsP++;
        if (qtsP==P and qtsR==R and qtsS==S)
            validos[nvalidos++] = tS;

        if (nvalidos==0)
            printf("IMPOSSIBLE\n");
        else {
            sort(validos,validos+nvalidos);
            printf("%s\n",validos[0].c_str());
        }

    }

    return 0;
}
