#include<iostream>
#include<vector>
#include<fstream>

using namespace std;

char rev(char ch){
    return ch == '+' ? '-' : '+';
}

int f(string str,int k){
    int times=0;
    int n = str.size();
    for(int i=0;i<n;++i){
        if(str[i] == '-' && i+k-1<n){
            times++;
            for(int j=i;j<k+i;++j){
                str[j] = rev(str[j]);
            }
        } else if(str[i] == '-'){
            return -1;
        }
    }
    return times;
}

int main(){
    int t;
    string str;
    int k;
    ofstream out("A-large.txt");
    ifstream in("A-large.in");
    in >> t;
    for(int h=0;h<t;++h){
        in >>str >> k;
        int ans = f(str,k);
        if(ans > -1){
            out << "Case #"<<h+1<<": "<<ans<<endl;
        } else{
            out << "Case #"<<h+1<<": IMPOSSIBLE\n";
        }
    }
}
