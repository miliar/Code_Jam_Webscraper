#include <iostream>
#include <vector>
#include <string>

typedef long long ll;

using namespace std;

bool isNotVowel(char c){
if ((c=='a') ||(c=='e') ||(c=='i') ||(c=='o') ||(c=='u'))
    return false;
else return true;
}

ll solve(){
    string s; ll n; cin>>s>>n;
    ll inRow=0; ll result =0; ll p=0;
    for (ll i=0; i<s.length(); i++)
        {
            if (isNotVowel(s[i])) inRow++;
            else inRow=0;

            if (inRow>=n){
                result+=(i-n+1-p+1)*(s.length()-1-i+1);
                p=i-n+2;
            }
        }
    return result;
}

int main()
{
    int t; cin>>t;
    for (int i=1; i<=t; i++)
        cout<<"Case #"<<i<<": "<<solve()<<endl;
    return 0;
}
