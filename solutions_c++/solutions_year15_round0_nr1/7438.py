#include<iostream>
#include<fstream>
using namespace std;

int main(){
    int t;
    ifstream in("A-small-practice.in");
    ofstream out("A-small-practice.txt");
    in>>t;
    int Case = 1;
    while(Case<=t){
        int sm;
        string s;
        in >> sm;
        in >> s;
        int re = 0,total=0 ;
        for(int i = 0;i<=sm;i++){
            if(total >= i)
                total += s[i]-'0';
            else{
                int temp = i-total;
                re += temp;
                total +=temp;
                total += s[i] -'0';
            }
        }
        out << "Case #" <<Case <<": " << re << endl;
        Case++;
    }
    return 0;
}
