#include <iostream>
#include <string>

using namespace std;

int main() {
int n;
string S,S2;
char C;
string :: iterator it;
cin >> n;
cin.ignore();
for (int i = 0 ; i < n ; i++){
getline (cin,S);
S2=S[0];
C=S[0];
for (int j = 1 ; j < S.length();j++){
if (int (S[j]) >= int (C)){it=S2.begin();
S2.insert(it,S[j]);C=S[j];}
else {it=S2.end();S2.insert(it,S[j]);}
}
cout << "Case #"<<i+1<<": "<<S2<<endl;
}
}

