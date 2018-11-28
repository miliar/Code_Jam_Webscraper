#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>

using namespace std;



int main()
{

    freopen("D-small-attempt1.in", "r", stdin);
    freopen("out.txt", "w", stdout);


    //Aufgabe 4
    int t = 0;
    cin >> t;

    for (int i = 1; i < t+1; i++){
        int k, c, s;
        cin >> k >> c >> s;
        cout << "Case #" << i << ":";
        if ((s*c) < k){
            cout << " IMPOSSIBLE" << endl;
            continue;
        }

        long long mult = 1;
        for(int j = 1; j<c; j++){
            mult *= k;
            mult += 1;
        }
        for(long long j = 0; j<s; j++){
            cout << " " << (j*mult)+1;
        }


        /*int ac = 0;
        bool endd = false;
        for (int j = 0; j < s; j++){
            long long number = 0;
            for (int m = 0; m < c; m++){

                number += pow(k,m)*ac;
                cout << "--" << pow(k,m) <<


                if (++ac >= k) {
                    endd = true;
                    break;
                }
            }
            cout << " " << (number+1);
            if (endd) break;
        }*/
        cout << endl;
    }



    //Aufgabe 3
    /*
    cout << "Case #1:" << endl;

    int N = 6;
    int J = 3;

    for (int i = 2; i < maxx*extend; i++){
        //cout << i << ": " << div[i] << endl;
        if (div[i/maxx][i%maxx] != 0){
            continue;
        }
        for (int j = 2; (j*i)<maxx*extend; j++){
            div[(i*j)/maxx][(i*j)%maxx] = j;
        }
    }


    //for (int i = 0; i < pow(2.0, N-2.0), i++){

    //}
    */


    //Aufgabe 2
    /*
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
    */



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
