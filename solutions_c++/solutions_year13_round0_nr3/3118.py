#include<iostream>
#include<fstream>
#include<vector>
#include<string>
#include<stdlib.h>
#include<sstream>
#include<math.h>
#include<stdexcept>
using namespace std;

template <typename T>
string tostring(const T& t)
{
    ostringstream ss;
    ss << t;
    return ss.str();
}//Convert from number to string
bool ispal(uint64_t num){
    if(num==1){return true;}
    string test_num = tostring(num);
    int length = test_num.length();
for(int i =0;i<(length+1)/2;i++){
    if(test_num[i]!= test_num[length-(1+i)]){
       // cout<<test_num[length] << "!= " << test_num[length-(1+i)]<<endl;
        return false;
    }
}// test if num is palindrome
return true;
   // cout<<num<<" is a palindrome" << endl;
}
bool fair(uint64_t num){
    if(!ispal(num)){return false;}
    else {
if(sqrt(num)==floor(sqrt(num)) && ispal(sqrt(num)))
    {
       // cout<<num << " and the sqrt : " << (long double) sqrt(num)<< " are palindromes" << endl;
      //  cout<<sqrt(num)<<endl;
    return true;
    }
else{
    return false;
    }
}

}
int main(){
int n;
ifstream file;
try{
file.open("C-small-attempt0.in", ios::in);
//cout<<"file opened success!" <<endl;
}
catch(exception e){
cout<<e.what();
}
ofstream outputfile;
try
{
     outputfile.open("C-small-out-attempt0.in", ios::out);


}catch(domain_error e)
    {
        cout<<e.what();
    }// open my files

file>>n;
cout<<n<<endl;
uint64_t start, finish;
int cnt=0;
for(int i =0;i<n;i++){
file>>start>>finish;
cnt=0;
        for(uint64_t x = start;x<=finish;x++){

            if(fair(x)){
                cnt++;
            }

        }
//cout<<"Case #" <<(i+1)<<": "<< cnt<<endl;
outputfile<<"Case #" << (i+1)<<": " <<cnt<<endl;
}// main loop

file.close();
outputfile.close();

return 0;
}
