#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <deque>
#include <algorithm>
#define forn(i,n) for(int i=0;(i)<(n);(i)++)

using namespace std;

typedef unsigned long long ull;

int main()
{
    int n;
    freopen("A.txt","r",stdin);
    freopen("A.out","w",stdout);
    cin>>n;
    cin.ignore();
    forn(i,n){
        string s;
        deque <char> news;
        cin>>s;

        int p=0;
        forn(j,s.length()){
            if(s[j]>=news.front()){
                news.push_front(s[j]);
                p++;
            }
            else
                news.push_back(s[j]);
        }
        cout<<"Case #"<<i+1<<": ";

        for(deque<char>::iterator it = news.begin(); it!= news.end(); it++){
            cout<<*it;
        }
        cout<<endl;
    }
    return 0;
}
