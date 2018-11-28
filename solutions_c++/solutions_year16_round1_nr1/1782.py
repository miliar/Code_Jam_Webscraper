#include <stdio.h>
#include <deque>
#include <string>
#include <iostream>
using namespace std;

int main(){
    int t;

    scanf ("%d", &t);

    for (int k=1; k<=t; k++){
        string s;
        deque<char> d;

        cin >> s;

        int sz = s.size();
        d.push_front(s[0]);

        for (int i=1; i<sz; i++){
            if (s[i] >= d.front())
                d.push_front(s[i]);
            else d.push_back(s[i]);
        }

        printf ("Case #%d: ", k);

        while (!d.empty()){
            printf ("%c", d.front());
            d.pop_front();
        }
        printf ("\n");
    }

    return 0;
}
