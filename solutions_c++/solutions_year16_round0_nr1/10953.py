#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main ()
{
ofstream myfile;
myfile.open ("ans.txt");
ifstream myReadFile;
myReadFile.open("example.txt");
 if (myReadFile.is_open()) {
int ans[2];
int num_cases, i=0, n_items, credit;
myReadFile >> num_cases;
for(int k=1;k<=num_cases;k++)
{
unsigned long long N ;
unsigned long long ans ;
bool b=0;
myReadFile >> N;// number to be converted to a string
set<int> s;
string Result;          // string which will contain the result
int i=1;
while(s.size()!=10){
if(N==0){

b=1;
break;
}
ans = N*i;
//cout<<ans<<endl;
ostringstream convert;
convert << ans;      // insert the textual representation of 'Number' in the characters in the stream
Result = convert.str();
for(int j=0;j<Result.size();j++){
s.insert(int(Result[j]));
}
   // stream used for
if(s.size()==10){
break;

}
i++;
}
if(b)  myfile << "Case #" <<k<<": "<< "INSOMNIA"<<endl;
else {
myfile << "Case #" <<k<<": "<<ans<<endl;
}
}
}
}
