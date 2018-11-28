#include<iostream>
#include<fstream>
using namespace std;
void inverse(string &str,int i,int k){
    int j;
    for(j=i;j<i+k;j++){
        if(str[j]=='+')
        str[j]='-';
        else
        str[j]='+';
    }
}
int getNo(string str,int k){
    int i=0,l=str.size(),j,count=0;
    while(i<l){
        while(str[i] == '+' && i<l)
        i++;
        if(i == l)
        break;
        if(l-i < k)
        return -1;
        inverse(str,i,k);
        count++;
    }
    return count;
}
int main(){
    int t,i,k;
    string str;
    ifstream ip;
    ofstream op;
    ip.open("A-large.in");
    op.open("op.txt");
    ip>>t;
    for(i=1;i<=t;i++){
        ip>>str>>k;
        //cout<<k<<endl;
        op<<"Case #"<<i<<": ";
        int res = getNo(str,k);
        if(res != -1)
        op<<res<<endl;
        else
        op<<"IMPOSSIBLE\n";
    }
    return 0;
}
