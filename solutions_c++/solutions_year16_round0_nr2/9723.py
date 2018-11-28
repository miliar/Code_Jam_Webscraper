#include <iostream>
#include <fstream>
int getlength(char[101]);
int chkcake(char[101],int);

using namespace std;
int main(){
    char pancake[101] = {}, buff;
    int length=0, i=0, j=0, times=0, Case,N;
    ifstream in;
    in.open("B-large.in");
    ofstream out;
    out.open("ProbBOut.txt");
    in >> Case;
    N = Case;
    while(Case >0){
        in >> pancake;
        length = getlength(pancake);
        times = 0;
        i = 0;
        j = 0;
        if(length==1&&pancake[0]=='-'){
            cout << "Case #" << N-Case+1 << ": 1" << endl;
            out << "Case #" << N-Case+1 << ": 1" << endl;
            Case-=1;
            continue;
        }
        while(chkcake(pancake,length)!=1){
            if(pancake[i]!=pancake[i+1]){
                for(j=0;j<=i;j++){
                    if(pancake[j]=='+') pancake[j] = '-';
                    else if(pancake[j]=='-') pancake[j] = '+';
                }
                for(j=0;j<=i;j++){
                    buff = pancake[j];
                    pancake[j] = pancake[i-j];
                    pancake[i-j] = buff;
                }
                i = 0;
                times++;
            }
            else i++;
            //cout << pancake << endl;
            //cout << times << endl;

        }
        cout << "Case #" << N-Case+1 << ": " << times << endl;
        out << "Case #" << N-Case+1 << ": " << times << endl;

        Case-=1;
    }
    in.close();
    out.close();
    return 0;
}

int getlength(char a[101]){
    int i = 0;
    while(a[i]!='\0')
        i++;
    return i;
}

int chkcake(char a[101],int len){
    int i = 0, j=0;
    for(i = 0;i<len;i++){
        if(a[i]=='+') j++;
    }
    if(j==len) return 1;
    else return 0;
}
