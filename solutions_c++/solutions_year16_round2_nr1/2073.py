//
// Created by 鲁蕴铖 on 16/4/30.
//


#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <thread>
#include <random>
#include <queue>
#include <set>
#include <map>
using namespace std;
int n;

int main()
{
//#ifndef ONLINE_JUDGE
    freopen("/Users/luyuncheng/Downloads/A-large.in", "r", stdin);
    freopen("/Users/luyuncheng/Downloads/A-large.out", "w", stdout);
//#endif
    int T;
    while(cin>>T) {
        int cas = 1;
        while(T--) {
            string s;
            cin>>s;
            map<char,int> mp;
            mp.clear();
            vector<int> ret;
            for(int i = 0; i<s.size(); i++) {
                mp[s[i]] ++;
            }
            while(mp['Z'] > 0) {
                mp['Z']--;
                mp['E']--;
                mp['R']--;
                mp['O']--;
                ret.push_back(0);
            }

            while(mp['X'] > 0) {
                mp['S'] --;
                mp['I'] --;
                mp['X'] --;
                ret.push_back(6);
            }
//            cout<<6<<endl;
            while(mp['S'] > 0) {
                mp['S'] --;
                mp['E'] --;
                mp['V'] --;
                mp['E'] --;
                mp['N'] --;
                ret.push_back(7);
            }
//            cout<<7<<endl;
            while(mp['V'] > 0) {
                mp['F'] --;
                mp['I'] --;
                mp['V'] --;
                mp['E'] --;
                ret.push_back(5);
            }
//            cout<<5<<endl;
            while(mp['F'] >0) {
                mp['F'] --;
                mp['O'] --;
                mp['U'] --;
                mp['R'] --;
                ret.push_back(4);
            }
//            cout<<4<<endl;
            while(mp['W'] >0) {
                mp['T'] --;
                mp['W'] --;
                mp['O'] --;
                ret.push_back(2);
            }
//            cout<<2<<endl;
            while(mp['O'] >0) {
                mp['O'] --;
                mp['N'] --;
                mp['E'] --;
                ret.push_back(1);
            }
            while(mp['R'] >0) {
                mp['T'] --;
                mp['H'] --;
                mp['R'] --;
                mp['E'] --;
                mp['E'] --;
                ret.push_back(3);
            }
            while(mp['N'] >0) {
                mp['N'] --;
                mp['I'] --;
                mp['N'] --;
                mp['E'] --;

                ret.push_back(9);
            }
            while(mp['E']>0) {
                mp['E'] --;
                mp['I'] --;
                mp['G'] --;
                mp['H'] --;
                mp['T'] --;

                ret.push_back(8);
            }
            sort(ret.begin(),ret.end());
            cout << "Case #" << cas++ <<": ";
            for(int i=0;i<ret.size();i++) {
                cout<<ret[i];
            }
            cout<<endl;
        }
    }
}