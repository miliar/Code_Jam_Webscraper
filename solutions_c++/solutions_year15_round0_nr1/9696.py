#include<bits/stdc++.h>
using namespace std;

int main(){
    int T,N;
    scanf("%d",&T);
    for(int i=1; i<=T; i++){
        string numb;
        cin >> N;
        cin >> numb;
        int aux=numb[0]-'0', resp=0,aux2;
        for(int j=1; j < numb.length(); j++){
            if((j > aux )&&(numb[j]-'0'!=0)){
                aux2 = j - aux;
                aux += aux2;
                aux+=numb[j]-'0';
                resp += aux2;
            }
            else
                aux+=numb[j]-'0';
        }
        cout << "Case #" << i << ": " << resp << endl;
    }
    return 0;
}
