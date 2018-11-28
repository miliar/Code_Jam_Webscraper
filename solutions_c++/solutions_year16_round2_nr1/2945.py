#include <bits/stdc++.h>
#include <iomanip>
typedef long long ll;
using namespace std;

int main(){
    string s;
    int T,i,j;
    cin >> T;
    for(int test = 1; test<=T; test++){
        cin >> s;
        int letters['Z'+1] = {0};
        vector<int> num;
        for(i = 0; i < s.length(); i++)
            letters[s[i]]++;

        // Удаление уникальных букв
        while(letters['Z']>0){
            letters['Z']--;
            letters['E']--;
            letters['R']--;
            letters['O']--;
            num.push_back(0);
        }
        while(letters['W']>0){
            letters['T']--;
            letters['W']--;
            letters['O']--;
            num.push_back(2);
        }
        while(letters['U']>0){
            letters['F']--;
            letters['O']--;
            letters['U']--;
            letters['R']--;
            num.push_back(4);
        }
        while(letters['X']>0){
            letters['S']--;
            letters['I']--;
            letters['X']--;
            num.push_back(6);
        }
        while(letters['G']>0){
            letters['E']--;
            letters['I']--;
            letters['G']--;
            letters['H']--;
            letters['T']--;
            num.push_back(8);
        }
        // Удаление всех оставшихся
        while(letters['O']>0){
            letters['O']--;
            letters['N']--;
            letters['E']--;
            num.push_back(1);
        }
        while(letters['T']>0){
            letters['T']--;
            letters['H']--;
            letters['R']--;
            letters['E']--;
            letters['E']--;
            num.push_back(3);
        }
        while(letters['F']>0){
            letters['F']--;
            letters['I']--;
            letters['V']--;
            letters['E']--;
            num.push_back(5);
        }
        while(letters['S']>0){
            letters['S']--;
            letters['E']--;
            letters['V']--;
            letters['E']--;
            letters['N']--;
            num.push_back(7);
        }
        while(letters['N']>0){
            letters['N']--;
            letters['I']--;
            letters['N']--;
            letters['E']--;
            num.push_back(9);
        }
        sort(num.begin(),num.end());
        cout << "Case #" << test << ": ";
        for(i = 0; i < num.size(); i++)
            cout << num[i];
        cout << endl;
    }
    return 0;
}