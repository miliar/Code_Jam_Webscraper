#include <iostream>
#include <vector>
#include <string>
#include <map>
using namespace std;
map<char,int> M{{'1',0},{'i',1},{'j',2},{'k',3}};
map<char,int> M2{{0,'1'},{1,'i'},{2,'j'},{3,'k'}};
vector<vector<string> > Res(4,vector<string>(4));
void sett(){
    Res[0][0]="1";
    Res[0][1]="i";
    Res[0][2]="j";
    Res[0][3]="k";

    Res[1][0]="i";
    Res[1][1]="-1";
    Res[1][2]="k";
    Res[1][3]="-j";

    Res[2][0]="j";
    Res[2][1]="-k";
    Res[2][2]="-1";
    Res[2][3]="i";

    Res[3][0]="k";
    Res[3][1]="j";
    Res[3][2]="-i";
    Res[3][3]="-1";
}
main(){
    sett();
    ios_base::sync_with_stdio(false);
    int t;
    cin >> t;
    int licznik=1;
    while(t--){
        int l,x;
        cin >> l >> x;
        string s;
        cin >> s;
        string tmp=s;
        for(int i=1;i<x;i++)
            s=s+tmp;
        vector<pair<bool,int> > I(s.size());
        int re=0;
        int minuss=0;
        for(int i=0;i<s.size();i++){
            string k=Res[re][M[s[i]]];
            if(k[0]=='-'){
                minuss++;
                re=M[k[1]];
            }
            else
                re=M[k[0]];
            if(M2[re]=='i')
                I[i]=make_pair(true,minuss);
            else
                I[i]=make_pair(false,minuss);
                //cout << i << endl;
        }
        re=0;
        minuss=0;
        vector<pair<bool,int> > K(s.size());
        for(int i=s.size()-1;i>=0;i--){
            string k=Res[M[s[i]]][re];
            if(k[0]=='-'){
                minuss++;
                re=M[k[1]];
            }
            else
                re=M[k[0]];
            if(M2[re]=='k'){
                K[i]=make_pair(true,minuss);
                //cout << i << endl;
            }
            else
                K[i]=make_pair(false,minuss);
        }

        bool flaga=false;
        for(int i=0;i<I.size() && !flaga;i++){
            re=0;
            minuss=0;
            if(I[i].first){
                for(int j=i+1;j<I.size()-1 && !flaga;j++){
                    string k=Res[re][M[s[j]]];
                    if(k[0]=='-'){
                        minuss++;
                        re=M[k[1]];
                    }
                    else
                        re=M[k[0]];
                    if(M2[re]=='j' && (I[i].second+K[j+1].second+minuss)%2==0 && K[j+1].first)
                        flaga=true;
                }
            }
        }
        if(flaga)
            cout << "Case #"<< licznik++ << ": "<< "YES"<< endl;
        else
            cout << "Case #"<< licznik++ << ": "<< "NO"<< endl;
    }
    return 0;
}

