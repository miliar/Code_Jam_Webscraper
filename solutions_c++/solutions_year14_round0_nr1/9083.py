#include <fstream>
#include <string>
#include <algorithm>
using namespace std;


//ifstream fin("")

ofstream fout ("Sol00.txt");
ifstream cin ("Sol00.in");
int a,b,c;
int X[4][4];
int Y[4][4];
int A[4];
int B[4];
int found;


int read(){
    cin >> a;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            cin >> X[i][j];
    a--;
    for(int i=0;i<4;i++)
        A[i]=X[a][i];

    cin >> b;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            cin >> Y[i][j];

    b--;

    for(int i=0;i<4;i++)
        B[i]=Y[b][i];

    int res=0;
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
    if(A[i]==B[j]){
        res++;
        found = A[i];
    }



    return res;
}


void eval(int k){
    fout << "Case #";
    fout << c << ": ";
    if(k>1) fout << "Bad magician!";
    if(k==1) fout << found;
    if(!k) fout << "Volunteer cheated!";
    fout << endl;
}


int main(){
    int T;
    cin >> T;

    while(T--){
        c++;
        int res=read();
        eval(res);
    }
    return 0;
}




