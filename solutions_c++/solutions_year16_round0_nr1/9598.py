#include <iostream>
#include <vector>
#include <string>
#include <fstream>

using namespace std;

vector<bool> v(10, false);

bool check(long long int a){
    long long int t=a;
    while(t){
        v[t%10]=true;
        t=t/10;
    }
    for(int i=0; i<10; i++){
        if(!v[i])  return false;
    }
    return true;
}

int main(int argc, char** argv){
long long int T;
long long int N;
ifstream read("input.txt");
if(read.is_open()){
read>>T;

vector<string> s;
for(int i=0; i<T; i++){

    read>>N;
    int caseNum=i+1;
    long long int N2=N;
    for(int i=0; i<v.size(); i++){
        v[i]=false;
    }
    if(N!=0){
        int counter=1;
        while(!check(N2)){
            counter++;
            N2=N*counter;
        }
        cout<<"Case #"<<caseNum<<": "<<N2<<endl;
    }
    else
   	cout<<"Case #"<<caseNum<<": "<<"INSOMNIA"<<endl;
}

read.close();
}

return 0;
}
