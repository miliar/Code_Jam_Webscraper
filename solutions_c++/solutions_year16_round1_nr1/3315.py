#include<iostream>
#include<cstdio>
#include<string.h>
#include<algorithm>
#include<vector>
#include<utility>
#include<deque>

#define ft first
#define sc second
#define pii pair<int,int>
#define mp make_pair
#define pb push_back

using namespace std;

const int MAX=2005;

string s;
int C[26];

int main(){
    freopen("A-large.in","r",stdin);
    freopen("o1.out","w",stdout);

    int T,i,len,j;
    cin>>T;
    for(int z=1;z<=T;z++){
        cin>>s;
        len=s.length();
        memset(C,0,sizeof(C));

        for(i=0;i<len;i++){
            C[s[i]-'A']+=1;
        }

        deque<char> Q;

        Q.push_front(s[0]);

        for(i=1;i<len;i++){
            if(s[i]>=Q.front()){
                Q.push_front(s[i]);
            }
            else{
                Q.push_back(s[i]);
            }
        }

        cout<<"Case #"<<z<<": ";

        for(auto it=Q.begin(); it!=Q.end(); it++){
            cout<<*it;
        }
        cout<<"\n";
    }


    return 0;
}
