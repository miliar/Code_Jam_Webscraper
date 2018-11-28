#include <limits>
#include <iostream>
#include <vector>
#include <fstream>
using namespace std;

double f(string line){
    double n=0,d=10;
    bool pass=true;
    for(int i=0;i<line.size();i++){
            if(line[i]=='.')pass=false;
            if(pass){n=(n*10)+(line[i]-'0');}
            else if(line[i]!='.'){
                n+=(line[i]-'0')/d;
                d*=10;
            }
    }
    return n;
}
double f1(vector<double> ar){
    vector<double>rec,rate,arrive;
    rate.push_back(2.0);
    rec.push_back(ar[2]/rate[0]);
    arrive.push_back(0);
    for(int i=1;;i++){
        double prevrate=rate[rate.size()-1];
        double prevarrive=arrive[arrive.size()-1];
        rate.push_back(prevrate+ar[1]);
        arrive.push_back(prevarrive+(ar[0]/rate[i-1]));
        rec.push_back((ar[2]/rate[i])+arrive[arrive.size()-1]);
        if(rec[rec.size()-1]>rec[rec.size()-2])return rec[rec.size()-2];
    }
    return 0.0;
}
int main(){
    string line;
    int n;
    cout.precision(7);
    getline(cin,line);n=f(line);
    for(int i=0;i<n;i++){
            getline(cin,line);
            vector<double> ar;
            for(int j=0;j<line.size();j++){
                string t;
                while(j<line.size() && line[j]!=' '){
                    t+=line[j];j++;
                }
                ar.push_back(f(t));
            }
        cout << "Case #"<<fixed<<i+1<<": "<<f1(ar)<<"\n";
    }
    return 0;
}

