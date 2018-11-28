#include<iostream>
#include<algorithm>
#include <cstdio>
#include<string>
#include<vector>
#include<cmath>
#include<cstdio>
using namespace std;


int main(){
    freopen("output.txt","w",stdout);
    int testcases;
    string s;
    cin>>testcases;
    for (int i=0 ; i<testcases ; i++){
        cin>>s;
        if(i)cout<<endl;

        vector<int> numbers;
        int cnt[26]={0};
        for (int j=0 ; j<s.length() ; j++)
            cnt[(int)s[j]-65]++;
        // ZERO
        while(cnt[(int)'Z'-65] > 0){
            numbers.push_back(0);
            cnt[(int)'Z'-65]--;
            cnt[(int)'E'-65]--;
            cnt[(int)'R'-65]--;
            cnt[(int)'O'-65]--;
        }
        //TWO
        while(cnt[(int)'W'-65] > 0){
            numbers.push_back(2);
            cnt[(int)'T'-65]--;
            cnt[(int)'W'-65]--;
            cnt[(int)'O'-65]--;
        }
        //FOUR
        while(cnt[(int)'U'-65] > 0){
            numbers.push_back(4);
            cnt[(int)'F'-65]--;
            cnt[(int)'O'-65]--;
            cnt[(int)'U'-65]--;
            cnt[(int)'R'-65]--;
        }

        //SIX
        while(cnt[(int)'X'-65] > 0){
            numbers.push_back(6);
            cnt[(int)'S'-65]--;
            cnt[(int)'I'-65]--;
            cnt[(int)'X'-65]--;
        }

        //SEVEN
        while(cnt[(int)'S'-65] > 0){
            numbers.push_back(7);
            cnt[(int)'S'-65]--;
            cnt[(int)'E'-65]--;
            cnt[(int)'V'-65]--;
            cnt[(int)'E'-65]--;
            cnt[(int)'N'-65]--;
        }

        //EIGHT
        while(cnt[(int)'G'-65] > 0){
            numbers.push_back(8);
            cnt[(int)'E'-65]--;
            cnt[(int)'I'-65]--;
            cnt[(int)'G'-65]--;
            cnt[(int)'H'-65]--;
            cnt[(int)'T'-65]--;
        }

        //THREE
        while(cnt[(int)'H'-65] > 0){
            numbers.push_back(3);
            cnt[(int)'T'-65]--;
            cnt[(int)'H'-65]--;
            cnt[(int)'R'-65]--;
            cnt[(int)'E'-65]--;
            cnt[(int)'E'-65]--;
        }
        //FOUR
        while(cnt[(int)'R'-65] > 0){
            numbers.push_back(4);
            cnt[(int)'F'-65]--;
            cnt[(int)'O'-65]--;
            cnt[(int)'U'-65]--;
            cnt[(int)'R'-65]--;
        }

        //FIVE
        while(cnt[(int)'F'-65] > 0){
            numbers.push_back(5);
            cnt[(int)'F'-65]--;
            cnt[(int)'I'-65]--;
            cnt[(int)'V'-65]--;
            cnt[(int)'E'-65]--;
        }

        //NINE
        while(cnt[(int)'I'-65] > 0){
            numbers.push_back(9);
            cnt[(int)'N'-65]--;
            cnt[(int)'I'-65]--;
            cnt[(int)'N'-65]--;
            cnt[(int)'E'-65]--;
        }

        //ONE
        while(cnt[(int)'N'-65] > 0){
            numbers.push_back(1);
            cnt[(int)'O'-65]--;
            cnt[(int)'N'-65]--;
            cnt[(int)'E'-65]--;
        }
        std::sort (numbers.begin(), numbers.begin()+numbers.size());
        cout<<"Case #"<<(i+1)<<": ";
        //generateBinary(N-1,"1",J);
        for (int j=0 ; j<numbers.size() ; j++){
            cout<<numbers[j];
        }
    }
    return 0;
}
