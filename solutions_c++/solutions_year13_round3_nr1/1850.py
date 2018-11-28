//
//Arkadiusz "Shintero" Roussau
#include<iostream>
#include<algorithm>
#include<utility>
#include<vector>
#include<cmath>
#include<string>

using namespace std;

int T, n;
string NAME;

int oblicz(){
    bool czy;
    int result=0, pom=0;
    int len=NAME.length();
    for(int i=0; i<len; i++){
        czy=false; pom=0;
        for(int j=i; j<len; j++){
            if(czy==false){
                if(NAME[j]!='a' && NAME[j]!='e' && NAME[j]!='i' && NAME[j]!='o' && NAME[j]!='u')
                    pom++;
                else
                    pom=0;
                }
            if(pom==n){
                result++;
                czy=true;}
            }
    }
return result;
    
}

int main(){
    ios_base::sync_with_stdio(0);
    cin >> T;
    for(int i=1; i<=T; i++){
        cin >> NAME;
        cin >> n;
        cout << "Case #" << i << ": " << oblicz() << endl;
    }
    return 0;
}
