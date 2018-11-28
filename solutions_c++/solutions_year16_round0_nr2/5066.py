#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{

    freopen("B-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);


    int t = 0;
    cin >> t;

    for (int i = 1; i < t+1; i++){
        string s;
        cin >> s;
        int x = 0;
        for (int j = 1; j < s.length(); j++){
            if (s[j-1] != s[j]) x++;
        }
        if (s[s.length()-1] == '-') x++;

        cout << "Case #" << i << ": " << x << endl;
    }




    // Aufgabe 1
    /*
    int t = 0;
    cin >> t;


    for (int i = 1; i < t+1; i++){

        int z = 0;
        cin >> z;

        if (z==0){
            cout << "Case #" << i << ": INSOMNIA" << endl;
            continue;
        }

        vector<bool> bits = vector<bool>(10);
        for (int j = 0; j < 100; j++){
            int x = z*j;
            while (x != 0){
                bits[x%10] = true;
                x = x/10;
            }
            bool cont = false;
            for (int k = 0; k<10; k++){
                if (bits[k] == false) cont = true;
            }
            if (cont == false){
                cout << "Case #" << i << ": " << j*z << endl;
                break;
            }
        }
    }*/

    return 0;
}
