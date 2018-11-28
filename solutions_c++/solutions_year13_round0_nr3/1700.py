
#include<fstream>
#include<vector>
#include<cmath>
#include<iostream>

using namespace std;

void buildTable(vector<string> &table){
    ifstream tablefile("square_fair.txt");
    string num;
    while(tablefile>>num){
        table.push_back(num);
        num.clear();
    }
    tablefile.close();
}
// 0 if a==b, >0 if a>b
int comp(string &a, string &b){
    if(a.size()<b.size()) return -1;
    else if(a.size()>b.size()) return 1;
    else return a.compare(b);
}

int main(){
    vector<string> table;
    buildTable(table);
    int T = (int)table.size();
    ifstream infile("C-large-1.in");
    ofstream outfile("C-large-1.out");
    //ifstream infile("C-small-attempt0.in");
    //ofstream outfile("C-small-attempt0.out");
    int N;
    infile >> N;
    string low, up;
    for(int i=0; i<N; ++i){
        infile >> low >> up;
        int begin = 0, end = T-1;
        while(begin<T && comp(low, table[begin]) > 0) ++begin;
        while(end>=0 && comp(up, table[end]) < 0) --end;
        int result = end-begin+1;
        outfile << "Case #"<< i+1 << ": " << result << endl;
    }
    infile.close();
    outfile.close();
    return 0;
}

