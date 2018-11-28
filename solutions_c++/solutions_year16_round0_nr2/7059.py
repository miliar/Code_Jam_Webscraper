#include <iostream>
#include <fstream>
#include <sstream>
using namespace std;

int main()
{ int n ;
ifstream inp ;
ofstream outp ;
inp.open("input.txt");
outp.open("output.txt");

inp>>n ;
cout << n<<endl;
int res;
string s ;
for (int i=1 ;i<=n ;i++){
char a,b;
s="" ;
inp>>s ;cout<<s<<endl;
 int l =s.length();cout<<l<<endl;
res=0;
a=s[0];
   for (int j=0 ;j<l ;j++){
        b=s[j];
    if ( a != b) {res++; }
    cout<<a<<"  "<<b<<endl;
    a=b;

   }

    if (b =='-') {res++;}

cout<<"res "<<res<<endl;

      outp<< "Case #"<<i<<": "<<res<<endl;

}


    return 0;
}
