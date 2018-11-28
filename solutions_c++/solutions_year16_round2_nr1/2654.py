// Coder nyble
#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pi;
typedef vector<string> vs;

#define fi          first
#define se          second
#define all(x)      (x).begin(), (x).end()
#define ini(a, v)   memset(a, v, sizeof(a))
#define re(i,s,n)  	for(int i=s;i<(n);++i)
#define fr(i,n)     re(i,0,n)
#define tr(i,x)     for(__typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define pu          push_back
#define mp          make_pair
#define sz(x)       (int)(x.size())
#define nl          printf("\n")

int main()
{
    int t;
    cin>>t;
    for(int z=1; z<=t; z++)
    {
        string text;
        cin>>text;
        int cnt[10] = {0,0,0,0,0,0,0,0,0,0};
        int a[26];
        string n = "0123456789";
        string result = "";

        for(int i=0;i<26;i++){
            a[i] = 0;
        }
        int len = text.length();
        for(int i=0; i<len; i++){
            a[text.at(i) -65]++;
        }
        if(a[25]>0){ //Z
            //zero is present remove them
            while(a[25]>0){
                cnt[0]++;//0
                a[25]--;//Z
                a[4]--;//E
                a[17]--;//R
                a[14]--;//O
            }
        }
        if(a[22]>0){ //W
            //two is present remove them
            while(a[22]>0){
                cnt[2]++;//2
                a[19]--;//T
                a[22]--;//W
                a[14]--;//O
            }
        }
        if(a[20]>0){ //U
            //four is present remove them
            while(a[20]>0){
                cnt[4]++;//4
                a[5]--;//F
                a[14]--;//O
                a[20]--;//U
                a[17]--;//R
            }
        }
        if(a[23]>0){ //X
            //six is present remove them
            while(a[23]>0){
                cnt[6]++;//6
                a[18]--;//S
                a[8]--;//I
                a[23]--;//X
            }
        }
        if(a[6]>0){ //G
            //eight is present remove them
            while(a[6]>0){
                cnt[8]++;//8
                a[4]--;//E
                a[8]--;//I
                a[6]--;//G
                a[7]--;//H
                a[19]--;//T
            }
        }
        //when even are removed one is unique
        if(a[14]>0){ //O
            //one is present remove them
            while(a[14]>0){
                cnt[1]++;//1
                a[14]--;//O
                a[13]--;//N
                a[4]--;//E
            }
        }
        if(a[17]>0){ //R
            //three is present remove them
            while(a[17]>0){
                cnt[3]++;//3
                a[19]--;//T
                a[7]--;//H
                a[17]--;//R
                a[4]--;//E
                a[4]--;//E
            }
        }
        if(a[5]>0){ //F
            //five is present remove them
            while(a[5]>0){
                cnt[5]++;//5
                a[5]--;//F
                a[8]--;//I
                a[21]--;//V
                a[4]--;//E
            }
        }
        if(a[18]>0){ //S
            //seven is present remove them
            while(a[18]>0){
                cnt[7]++;//7
                a[18]--;//S
                a[4]--;//E
                a[21]--;//V
                a[4]--;//E
                a[13]--;//N
            }
        }
        if(a[4]>0){ //E
            //nine is present remove them
            while(a[4]>0){
                cnt[9]++;//9
                a[13]--;//N
                a[8]--;//I
                a[13]--;//N
                a[4]--;//E
            }
        }
        for(int i=0;i<10;i++){
            for(int j=0;j<cnt[i];j++){
                result += n.at(i);
            }
        }

        printf("Case #%d: %s\n",z,result.c_str());

    }
    return 0;
}
