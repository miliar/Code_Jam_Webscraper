#include<iostream>
#include<fstream>
using namespace std;
class sol{
public:
string getlastword(string& s){
if(s=="")
return s;
string result="";
result+=s[0];
for(int i=1;i<s.size();i++){
if(s[i]>=result[0])
result=s[i]+result;
else
result+=s[i];
}
return result;
}
};
int main(){
sol s;
ifstream is("A-large.in");
ofstream os("Output.txt");
int num;
is>>num;
string wd;
for(int i=1;i<=num;i++){
is>>wd;
string result=s.getlastword(wd);
os<<"Case #"<<i<<": "<<result<<"\n";
}
is.close();
os.close();
}