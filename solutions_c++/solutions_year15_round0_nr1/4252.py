# include <iostream>
# include <string>
# include <sstream>

using namespace std;

int main(){
    int n, aux, I = 0;
    stringstream ss;
    cin >> n;
    while(n--){
        int k;
        string s;

        cin >> k >> s;
        int amigos = 0, count = 0; 
        for (int i = 0; i <= k; ++i)
        {
            ss.clear();
            ss << s[i];
            ss >> aux;

            if(aux > 0){
                if(i > amigos + count){
                    amigos += i - (amigos + count);
                }
                count += aux;
            }
        }
        cout << "Case #" << ++I << ": " << amigos << endl;
    }
    return 0;
} 