#include<bits/stdc++.h>
using namespace std;
bool diferente(bool mas,char actual){
    if(actual=='+' and mas)return false;
    if(actual=='-' and !mas)return false;
    return true;
}
int solve(string s){
    int cantidad = 0;
    bool mas = true;
    for(int i=s.size()-1;i>=0;i--){
        char actual = s[i];

        if(diferente(mas,actual)){
            cantidad++;
            mas = !mas;
        }
    }
    return cantidad;

}
int main(){
    freopen("B-large.in","r",stdin);
	freopen("output.out","w",stdout);
    int T;scanf("%d",&T);
    for(int i=1;i<=T;i++){
        string s;cin>>s;
        cout<<"Case #"<<i<<": "<<solve(s)<<endl;
    }
    return 0;
}
