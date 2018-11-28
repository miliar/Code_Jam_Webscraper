#include <map>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

#define enableFastIO ios_base::sync_with_stdio(false); cin.tie(NULL);
#define inc(i,j,k) for (auto i=j;i<=k;i++)
#define li long int
#define lli long long int

using namespace std;

int main()
{
    enableFastIO;
    int n,dig,rep;
    cin >> n;
    string s;
    map<int,char> unl = {{0,'Z'},{2,'W'},{4,'U'},{6,'X'},{8,'G'},{7,'S'},{5,'V'},{3,'T'},{1,'O'},{9,'I'}};
    map<int,string> spell = {{0,"ZERO"},{1,"ONE"},{2,"TWO"},{3,"THREE"},{4,"FOUR"},{5,"FIVE"},{6,"SIX"},{7,"SEVEN"},{8,"EIGHT"},{9,"NINE"}};
    inc(testcase,1,n) {
        cin >> s;
        vector<int> hist(26,0),ans;
        //cout << s << endl;
        for (char c:s)
            hist[c-'A']+=1;
        //for (int i=0;i<26;++i)  if (hist[i]> 0)cout << char('A'+i) << ":" << hist[i] << endl;
        for (char num:"0246875319"){
            dig = num - '0';
            rep = hist[unl[dig]-'A'];
            //cout << "Now " << num << " : " <<dig << ":"<<key<< endl;
            if (rep>0){
                //cout << "Found .." << dig << " : " << rep<< endl;
                for (int k=0;k<rep;++k)
                    ans.push_back(dig);
                for (char c:spell[dig])
                    hist[c-'A'] -= rep;
                //for (int i=0;i<26;++i)  if (hist[i]> 0)cout << char('A'+i) << ":" << hist[i] << endl;
            }
        }
        sort(ans.begin(),ans.end());
        cout << "Case #" << testcase << ": ";
        for (int i:ans) cout << i;
        cout << endl;
    }
}
