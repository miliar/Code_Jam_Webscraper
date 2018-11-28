#include<iostream>
#include<string>
#include<algorithm>
#include<cstring>

using namespace std;

int main() {
int flips = 0;
std::string sign;
int i;
int cases = 0;
cin >> cases;
int foo;
for(foo=1; foo<=cases; foo++)
{
flips = 0;
cin >> sign;
int signlen = sign.size();
for(i=signlen; i>0; i--)
{
if(sign[i-1] == '-'){
flips += 1;
std::replace( sign.begin(), sign.end(), '+', '*');
std::replace( sign.begin(), sign.end(), '-', '+');
std::replace( sign.begin(), sign.end(), '*', '-');
sign[i-1] = '\0';
}
}
cout << "Case #" << foo << ": " << flips << endl;
}
}
