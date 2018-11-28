#include<iostream>
#include<fstream>
#include<string>
using namespace std;
int main(){
ifstream infile;
   //infile.open("D-large-practice.in");

  ofstream outfile;
 //  outfile.open("output.5");
int t,k=1;
cin>>t;
string s;

while(t--){
    cin>>s;
    string ans;
    char c =s[0];
    ans.append(s.begin(),s.begin()+1);


    for(int i=1;i<s.length();i++){
       string temp(s.begin()+i,s.begin()+1+i);
        if(temp[0]>=ans[0]) ans = temp +ans;
        else ans = ans+ temp;
    }
    cout<<"Case #"<<k++<<": "<<ans<<endl;
}
return 0;
}
