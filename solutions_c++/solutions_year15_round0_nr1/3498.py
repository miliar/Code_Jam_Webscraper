#include<bits/stdc++.h>
#include<fstream>



#define ll long long
#define fin cin
#define fout cout

using namespace std;

ll t,n,l,store,ans,cur;
string s;

int main(){
    ifstream fin("A-large.in");
    ofstream fout("output.txt");

    fin>>t;
    for( ll ca = 1; ca <= t; ca++ ) {
        fin>>n;
        fin>>s;
        l=s.length();

        store=0;
        ans=0;

        for( ll i = 0; i < l; i++ ) {
            cur = s.at( i ) - '0';
            if( i> store ){
                ans   += (i-store);
                store += (i-store);
            }
            store += cur;
        }

        fout<<"Case #"<<ca<<": "<<ans<<"\n";
    }
    return 0;
}
