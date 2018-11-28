#include <bits/stdc++.h>

using namespace std;

int number(char c);

int main(){
    ifstream fin("SO.in");
    ofstream fout("SO.out");
    int T;
    fin>>T;
    for(int i=1; i<=T; i++){
        int n,result=0,already=0;
        string x;
        fin>>n>>x;
        for (int j=0; j<x.length(); j++){
            if (already<j){
                result+=(j-already);
                already+=(j-already+number(x[j]));
            }
            else{
                already+=number(x[j]);
            }
        }
        //if (result<0) result=0;
        fout<<"Case #"<<i<<": "<<result<<endl;
    }
    return 0;
}

int number(char c){
    if(c=='0')
        return 0;
    else if(c=='1')
        return 1;
    else if(c=='2')
        return 2;
    else if(c=='3')
        return 3;
    else if(c=='4')
        return 4;
    else if(c=='5')
        return 5;
    else if(c=='6')
        return 6;
    else if(c=='7')
        return 7;
    else if(c=='8')
        return 8;
    else if(c=='9')
        return 9;
}
