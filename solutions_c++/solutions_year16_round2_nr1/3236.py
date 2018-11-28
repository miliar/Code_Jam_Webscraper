#include <iostream>
#include <cmath>
#include <algorithm>
#include <string>
#include <vector>
#include <map>
#include <cstdio>
typedef long long ll;
using namespace std;

int main(){
    freopen("A-large (3).in","r",stdin);
    freopen("output.txt","w",stdout);
    int t,i,j;
    cin >> t;
    for(int test = 1; test<=t; test++){
        string s;
        cin >> s;
        int letters['Z'+1] = {0};
        vector<int> nums;
        for(i = 0; i < s.length(); i++)
            letters[s[i]]++;

        // Удаление уникальных букв
        while(letters['Z']>0){
            letters['Z']--;
            letters['E']--;
            letters['R']--;
            letters['O']--;
            nums.push_back(0);
        }
        while(letters['W']>0){
            letters['T']--;
            letters['W']--;
            letters['O']--;
            nums.push_back(2);
        }
        while(letters['U']>0){
            letters['F']--;
            letters['O']--;
            letters['U']--;
            letters['R']--;
            nums.push_back(4);
        }
        while(letters['X']>0){
            letters['S']--;
            letters['I']--;
            letters['X']--;
            nums.push_back(6);
        }
        while(letters['G']>0){
            letters['E']--;
            letters['I']--;
            letters['G']--;
            letters['H']--;
            letters['T']--;
            nums.push_back(8);
        }
        // Удаление всех оставшихся
        while(letters['O']>0){
            letters['O']--;
            letters['N']--;
            letters['E']--;
            nums.push_back(1);
        }
        while(letters['T']>0){
            letters['T']--;
            letters['H']--;
            letters['R']--;
            letters['E']--;
            letters['E']--;
            nums.push_back(3);
        }
        while(letters['F']>0){
            letters['F']--;
            letters['I']--;
            letters['V']--;
            letters['E']--;
            nums.push_back(5);
        }
        while(letters['S']>0){
            letters['S']--;
            letters['E']--;
            letters['V']--;
            letters['E']--;
            letters['N']--;
            nums.push_back(7);
        }
        while(letters['N']>0){
            letters['N']--;
            letters['I']--;
            letters['N']--;
            letters['E']--;
            nums.push_back(9);
        }
        sort(nums.begin(),nums.end());
        cout << "Case #" << test << ": ";
        for(i = 0; i < nums.size(); i++)
            cout << nums[i];
        cout << endl;
    }
    return 0;
}