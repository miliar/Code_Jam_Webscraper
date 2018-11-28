#include<iostream>
#include<string>
#include<fstream>
#define ll long long
#define pro 1935
char temp;
using namespace std;
void flip(string &s , int n){
for(int i =0 ; i <= (n-1)/2; i++ ){
    temp  = pro/s[i];
    s[i] = pro/s[n-i-1];
    s[n-i-1] = temp;

}

}
int main(){

ifstream input("B-large.in");
ofstream out("B.txt");
int  T ;
input >> T;
string s;
for(int t = 1; t <= T ; t++){
   int ans=0 , i , j = -1;
   input >> s;
for( i = s.length()-1 ; i >=0 ; i--,j=-1)
{
if(s[i] == '-'){
if(s[0] =='+'){
   ans++;
  while(s[++j]=='+' && j<s.length()-1); flip(s , j);} //cout << s << endl;
if(s[0]=='-') flip(s , i+1);
    ans++;
}
}
out << "Case #" << t << ": " << ans << endl;
}
out.close();
input.close();

return 0;
}
