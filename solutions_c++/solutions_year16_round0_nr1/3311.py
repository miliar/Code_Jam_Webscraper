#include<iostream>


using namespace std;

int main(){
    ios::sync_with_stdio(false);
    int t, n, out;
    string tmp;
    cin >> t;
    for (int l = 0; l < t; l++){
        cin >> n;
        if (n == 0)
            cout << "Case #" << l+1 << ": INSOMNIA\n";
        else{
            out = n;
            unordered_set<int> set;
            for (int i = 0; i < 10; i++)
                set.insert(i);
            while (true){
                tmp = to_string(out);
                for (int j = 0; j < tmp.size(); j++)
                    set.erase(tmp[j] - '0');
                if (set.empty())
                    break;
                out += n;
            }
            cout << "Case #" << l+1 << ": "<< out << "\n";     
        }
    }
    return 0;
}
