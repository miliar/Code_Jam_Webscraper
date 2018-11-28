#include <bits/stdc++.h>

using namespace std;

int main(){
    int t,a,i,j,contador;
    string word;
    cin >> t;
    for(a=0;a<t;a++){
        contador = 0;
        cout << "Case #" << a+1 << ": ";
        cin >> word;
        i = word.length();
        i--;
        while(i>=0){
            if(word[i] == '+'){
                i--;
            } else {
                j=0;
                while(word[j]=='+'){
                    j++;
                }
                if(word[0]=='+')
                    contador++;
                while(j>=0){
                    word[j] = '-';
                    j--;
                }
                //cout << "-> " << word << endl;
                reverse(word.begin(),word.begin()+i+1);
                //cout << "#->" << word << endl;
                //cout << i << endl;
                for(j=i;j>=0;j--){
                    if(word[j]=='-')
                        word[j] = '+';
                    else
                        word[j] = '-';
                }
                //cout << "*->" << word << endl;
                i--;
                contador++;
            }
        }
        cout << contador << endl;
    }
    return 0;
}
