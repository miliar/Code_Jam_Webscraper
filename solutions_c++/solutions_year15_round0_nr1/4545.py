#include <iostream>
#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <string>
using namespace std;

int main(){
    //freopen("a.txt", "r", stdin);
    //freopen("A-large.in", "r", stdin);freopen("b.txt","w",stdout);
    int T;
    cin >> T;
    for(int k = 1; k <= T; k++){
        int n;
        string s;
        cin >> n >> s;
        int standPerson = 0;
        int needPerson = 0;
        for (int i = 0; i <= n; i++){
            int tmpNow = s.at(i) - '0';
            if (tmpNow > 0){
                if (i > standPerson){
                    needPerson += i - standPerson;
                    standPerson  = i;
                }
                standPerson += tmpNow;
            }
        }
        printf("Case #%d: %d\n", k, needPerson);
    }

	return 0;
}
