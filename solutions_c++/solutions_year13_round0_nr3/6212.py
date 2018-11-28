#include <iostream>
#include <fstream>
#include <sstream>
#include <cmath>

using namespace std;

//#define TEST

string reverse(string s);
bool isFair(string s);
long findAnswer(unsigned long long ini, unsigned long long end);


int main()
{
    streambuf * buf;
#ifdef TEST
    buf = cout.rdbuf();
#else
    ofstream of;
    of.open("/Users/ParNurZeal/Workspace/Qt-Project/CodeJam2013/c-small-attempt0.out.txt");
    //of.open("/Users/ParNurZeal/Workspace/Qt-Project/CodeJam2013/A-large.out");
    buf = of.rdbuf();
#endif
    ostream out(buf);


    string line;
    //ifstream infile("/Users/ParNurZeal/Workspace/Qt-Project/CodeJam2013/c.in.txt");
    ifstream infile("/Users/ParNurZeal/Workspace/Qt-Project/CodeJam2013/c-small.in");
    //ifstream infile("/Users/ParNurZeal/Workspace/Qt-Project/CodeJam2013/A-large.in.txt");
    if(!infile.is_open()){
        cout << "file error" <<endl;
    }
    // read to stringstream
    stringstream ss;
    ss << infile.rdbuf();
    infile.close();

    int num_case=0;
    ss>>num_case;
    cout << num_case <<endl;

    for(int i  =1;i<=num_case;i++){
        unsigned long long ini =0;
        unsigned long long end =0;
        ss>>ini;ss>>end;
        long count = findAnswer(ini,end);
        out<<"Case #"<<i<<": "<<count<<endl;
    }

    cout << ":::PROGRAM END:::" << endl;
#ifndef TEST
    of.close();
#endif
    return 0;
}

long findAnswer(unsigned long long ini, unsigned long long end){
    long count=0;
    for(unsigned long long i =ini;i<=end;i++){
        stringstream num;
        num<<i;
        if(!isFair(num.str())) continue;
        unsigned long long root = sqrtl(i);
        if(root*root==i){
            stringstream root_num;
            root_num<<root;
            if(isFair(root_num.str())) count++;
        }
    }
    return count;
}

bool isFair(string s){
    for(int i = 0;i<s.length()/2;i++){
        if(s[i]!=s[s.length()-1-i]) return false;
    }
    return true;
}

string reverse(string s){
    string result="";
    for(int i = s.length()-1 ;i>=0;i--){
        result+=s[i];
    }
    return result;
}
