#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <string>
#include <cstring>
#include <algorithm>
#include <map>
#include <set>

const int BEG = 0;
const int END = 1;

using namespace std;

bool arr[1000];

string str;

char firstLetter;
char secondLetter;

int main ()
{
    freopen ("input.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
    int t;
    cin >> t;
    for (int i = 0;i < t;i++){
        cin >> str;
        secondLetter = 'a';
        for (int j = 0;j < str.size();j++){
            if (j == 0){
                arr[j] = BEG;
                firstLetter = str[j];
            }
            else if (str[j] == firstLetter){
                if (secondLetter == 'a'){
                    arr[j] = BEG;
                }
                else if (str[j] < secondLetter){
                    arr[j] = END;
                }
                else{
                    arr[j] = BEG;
                }
            }
            else{
                if (str[j] < firstLetter){
                    arr[j] = END;
                    if (secondLetter == 'a'){
                        secondLetter = str[j];
                    }
                }
                else{
                    arr[j] = BEG;
                    secondLetter = firstLetter;
                    firstLetter = str[j];
                }
            }
        }
        printf ("Case #%d: ", i + 1);
        for (int j =  str.size() - 1;j >= 0;j--) {
            if (arr[j] == BEG){
                printf ("%c", str[j]);
            }
        }
        for (int j = 0;j < str.size();j++){
            if (arr[j] == END){
                printf ("%c", str[j]);
            }
        }
        printf ("\n");
    }
    return 0;
}