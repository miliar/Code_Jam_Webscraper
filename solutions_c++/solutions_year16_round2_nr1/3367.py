#include <iostream>
#include <cstring>
#include <string>
#include <fstream>
using namespace std;

int T,N,cnt[40],ans[20]; string w[20]; string s;

void del(int k,int nr){
    int i;
    for (i=0; i<w[k].length(); i++)
        cnt[w[k][i]-'A']-=nr;
}

int main(){
    ifstream fin("input.in");
    ofstream fout("output.txt");
    fin >> T;

    w[0]="ZERO",w[1]="ONE",w[2]="TWO",w[3]="THREE",w[4]="FOUR",w[5]="FIVE",w[6]="SIX",w[7]="SEVEN",w[8]="EIGHT",w[9]="NINE";

    int i,j,k;
    for (k=1; k<=T; k++){
        fin >> s;
        fout << "Case #" << k << ": ";
        N=s.length();
        memset(ans,0,sizeof(ans));
        memset(cnt,0,sizeof(cnt));

        for (i=0; i<N; i++) cnt[s[i]-'A']++;
        ans[0]=cnt['Z'-'A'];del(0,ans[0]);
        ans[2]=cnt['W'-'A'];del(2,ans[2]);
        ans[8]=cnt['G'-'A'];del(8,ans[8]);
        ans[3]=cnt['H'-'A'];del(3,ans[3]);
        ans[4]=cnt['R'-'A'];del(4,ans[4]);
        ans[1]=cnt['O'-'A'];del(1,ans[1]);
        ans[5]=cnt['F'-'A'];del(5,ans[5]);
        ans[7]=cnt['V'-'A'];del(7,ans[7]);
        ans[6]=cnt['S'-'A'];del(6,ans[6]);
        ans[9]=cnt['I'-'A'];del(9,ans[9]);
        for (i=0; i<10; i++)
            for (j=1; j<=ans[i]; j++) fout << i;

        fout << "\n";

    }

    return 0;
}
