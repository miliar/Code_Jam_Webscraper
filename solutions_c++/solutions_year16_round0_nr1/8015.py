#include<string>
#include<fstream>
#include<sstream>
#include<iostream>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;

int main(int argc , char ** argv){
    ifstream match(argv[1]);      //open a file
    ofstream output(argv[2]);     //write into a file
    int n=0;
    string line ;
    while( getline(match, line) ){
        ++n;
    }
    ifstream matches(argv[1]);
    string r;
    string a1;
    string a2;
    getline(matches, r);
    n-=1;
    for (int i = 0; i<n; i++){
        vector<int> res(10, 0);
        getline(matches, r);
        int count = 0;
        int ti = 1;
        istringstream r1(r);
        r1>>a1;
        int num = atoi(a1.c_str());
        int sum = num;
        if (num==0) {output<<"Case #"<<i+1<<": INSOMNIA"<<endl; continue;}
        while (count<10) {
            a2 = to_string(sum);
            int len = a2.size();
            for (int j = 0; j<len; j++){
                int nn = a2[j]-'0';
                if (res[nn]==0) {
                    res[nn]=1;
                    count++;
                }
            }
            sum+=num;
        }
        output<<"Case #"<<i+1<<": "<<a2<<endl;
    }
}
