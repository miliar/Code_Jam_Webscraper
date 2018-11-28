#include<iostream>
#include<stdio.h>
#include<list>
#include<vector>
#include<utility>
#include<map>
#include<set>

using namespace std;

typedef long long int ll;
typedef pair<int,int> pp;

template<class T> inline void read(T&x){bool fu=0;char c;for(c=getchar();c<=32;c=getchar());if(c=='-')fu=1,c=getchar();for(x=0;c>32;c=getchar())x=x*10+c-'0';if(fu)x=-x;};
template<class T> inline void read(T&x,T&y){read(x);read(y);}
template<class T> inline void read(T&x,T&y,T&z){read(x);read(y);read(z);}
template<class T> inline void read(T&x,T&y,T&z,T&q){read(x);read(y);read(z);read(q);}

int main(void) {
    int testCases,s,i,j;
    string str;
    read(testCases);
    for (i = 0; i < testCases; i++) {
        cin >> s;
        cin >> str;
        int val[s];
        val[0] = 0;
        int result = 0;

        for (j = 1; j <= s; j++) {
            int n = str[j - 1] - 48;
            val[j] = val[j - 1] + n;
            
            if (j > val[j]) {
                result += (j - val[j]);
                val[j] += (j - val[j]);
            }         
        }

        cout << "Case #" << i + 1 << ": " << result << endl;
    }    
    return 0;
}
