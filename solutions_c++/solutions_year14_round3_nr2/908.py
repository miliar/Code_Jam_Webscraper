#include <algorithm>
#include <string>
#include <fstream>
using namespace std;

ifstream cin ("Lol01.txt");
ofstream cout ("Sol00.txt");

string K[100];
string tmp;
string tmp2;
int T,N;

int solve(){
    int myint[100];
    for(int i=0;i<N;i++)
        myint[i]=i;
    int sol=0;
    do{
        string cntrl;
        for(int i=0;i<N;i++)
            cntrl += K[myint[i]];
        bool mark[26]={};
        string tmp2;
        int j=0,k=0,mm=0;
        int sze=cntrl.size();
        while(k<sze){
            tmp2 += cntrl[j];
            while(k<sze && cntrl[j]==cntrl[k]) k++;
            j=k;
        }
        bool ttt=1;
        sze=tmp2.size();
        for(int i=0;i<sze;i++){
            if(!mark[tmp2[i]-'a']) mark[tmp2[i]-'a']=1;
            else {ttt=0; break;}
        }
        if(ttt) sol++;
    }while(next_permutation(myint,myint+N));
    return sol;
}


int main(){
    int k=1;
    cin >> T ;
    while(T--){
        cin >> N;
        for(int i=0;i<N;i++){
            cin >> tmp;
            int j=0,k=0,mm=0;
            int sze=tmp.size();
            string tmp2;
            //cout << tmp << endl;
            while(k<sze){
                tmp2 += tmp[j];
                while(k<sze && tmp[j]==tmp[k]) k++;
                j=k;
            }
            K[i]=tmp2;
            //cout << K[i] << endl;
        }
        cout << "Case #" << k << ": " << solve() << endl;
        k++;
    }
    return 0;
}
