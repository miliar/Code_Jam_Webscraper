#include <vector>
#include <conio.h>
#include <iostream>
#include <algorithm>
#include <fstream>
using namespace std;

int main(){
    long int N,T,c,n;
    vector <long int> no,digit;
    ifstream ifile ("A-large.in");
    ofstream ofile ("A-large.out");
    string line;
    getline(ifile,line,'\n');
    T = atoi(line.c_str());
    //cin>>T;
    for(int i=1;i<=T;i++){
        getline(ifile,line,'\n');
        n = atoi(line.c_str());
        //cin>>n;
        N = n;
        for(int j=0;j<10;j++)
            digit.push_back(j);
        int y=0;
        c=1;
        if(n==0)
            ofile<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        else{
                for(int x=1;y!=1;x++){
                    int temp = N;
                    for(int j=1;temp>0;j++) {
                        int d = temp % 10;
                        temp = temp / 10;
                        no.push_back(d);
                    }
                    sort(no.begin(),no.end());
                    unique(no.begin(),no.end());
                    for(int k=0;k < no.size();k++) {
                        if (no[k] == no[k + 1])
                            no.erase(no.begin()+k);
                    }
                    for(int k=0;k < no.size();k++){
                        for(int l=0;l<digit.size();l++){
                            if(no[k]==digit[l])
                                digit.erase(digit.begin()+l);
                        }
                    }
                    if(digit.size()==0){
                        ofile<<"Case #"<<i<<":"<<" "<<N<<endl;
                        y=1;
                    }
                    else{
                        c++;
                        N = c*n;
                    }
                }
            }
            digit.clear();
            no.clear();
        }
        ifile.close();
        ofile.close();
        return 0;
}
