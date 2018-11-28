#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <cmath>
#include <string>

#define N 1005

using namespace std;

int main(){
    int nc;
    scanf("%d", &nc);
    for(int caso = 1; caso <= nc; caso++){
        int n;
        scanf("%d", &n);
        
        bool val = true;
        string aux;
        vector< vector<int> > v;
        for(int i = 0; i < n; i++){
            string s;
            cin>>s;
            string red = "";
            int l = s.length();
            
            red += s[0];
            int tam = 1;
            vector<int> vaux;
            for(int j = 1; j < l; j++){
                if(s[j] != s[j - 1]){
                    vaux.push_back(tam);
                    tam = 1;
                    red += s[j];
                }
                else tam++;
            }
            vaux.push_back(tam);
            v.push_back(vaux);
            
            if(i > 0){
                if(aux != red){
                    val = false;
                }
            }
            aux = red;
        }
        
        if(!val) printf("Case #%d: Fegla Won\n", caso);
        else{
            int resp = 0;
            for(int i = 0; i < v[0].size(); i++){
                int temp = 1<<30;
                for(int k = 1; k <= 101; k++){
                    int ac = 0;
                    for(int j = 0; j < v.size(); j++){
                        ac += abs(v[j][i] - k);
                    }
                    temp = min(temp, ac);
                }
                resp += temp;
            }
            printf("Case #%d: %d\n", caso, resp);
        }
        
    }
}
