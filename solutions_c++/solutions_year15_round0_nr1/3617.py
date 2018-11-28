#include <iostream>
#include <fstream>
#include <string>
#include <sstream>

using namespace std;

long long solve(string n,string s){
    if(n=="0"||s.size()<=1) return 0;
    long long level = atoi(n.c_str());
    if(level!=s.size()-1) return -1;
    long long standed = (s[0]-'0');
    long long res = 0;
    for(int i=1;i<=level;i++){
        int need=i-standed;
        need = max(need,0);
        res += need;
        standed+=need;
        standed+=(s[i]-'0');
    }
    return res;
}

int main(){
    long long res;
    ifstream myfile;
    myfile.open("A-large.in.txt");
    ofstream outfile;
    outfile.open("output.txt");

    string line;
    getline(myfile,line);
    const int t=atoi(line.c_str());
    for(int i=0;i<t;i++){
        getline(myfile,line);
        istringstream iss(line);
        string str1,str2;
        iss >> str1;
        iss >> str2;
        res = solve(str1,str2);
        if(res<0) cout<<"Error In Line: #"<<i+1<<endl;
        outfile<<"Case #"<<(i+1)<<""<<": "<<res<<endl;
    }

    outfile.close();
    myfile.close();
    return 1;
}














