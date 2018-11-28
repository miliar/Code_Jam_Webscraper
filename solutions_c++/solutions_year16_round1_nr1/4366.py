#include<iostream>
#include<fstream>
#include<cstring>

using namespace std;
int main(){
    string Str,Sout;
    char S[1005];
    int Case=0,N=0,i=0,j=0,k=0;
    int maxV=0,nowV=0;
    ifstream in;
    in.open("A-large.in");
    ofstream out;
    out.open("OutAlarge.txt");

    in >> Case;                    //Number of test cases
    N = Case;
    getline(in,Str);
    while(getline(in,Str)&&Case>0){
        Sout.clear();
        maxV = 0;
        nowV = 0;
        k = Str.size();
        Str.copy(S,k);
        for(i=0;i<k;i++){
            nowV = S[i];
            if(nowV<maxV) {
                Sout = Sout + S[i];
            }
            else if(nowV>=maxV){
                Sout = S[i] + Sout;
                maxV = nowV;
            }
        }
        cout << "Case #" << N-Case+1 << ": " << Sout <<endl;
        out << "Case #" << N-Case+1 << ": " << Sout <<endl;

        Case-=1;
    }

    return 0;
}
