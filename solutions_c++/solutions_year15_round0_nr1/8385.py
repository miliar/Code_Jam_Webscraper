#include<map>
#include<cmath>
#include<vector>
#include<iomanip>
#include<cstdlib>
#include<sstream>
#include<fstream>
#include<cstring>
#include<iostream>
#include<algorithm>
using namespace std;
int main(){
    fstream fin,fout;
    fin.open("A-large.in",ios::in);
    fout.open("out.txt",ios::out);
    int t;
    fin>>t;
    for(int nn=0;nn<t;++nn){
        int smax;
        fin>>smax;
        string num;
        fin>>num;
        int count=0,current_stand=0;
        for(int i=0;i<num.size();++i){
            if(current_stand>=i) current_stand+=num[i]-'0';
            else{
                int a=i-current_stand;
                count+=a;
                current_stand+=(num[i]-'0'+a);
            }
        }
        fout<<"Case #"<<nn+1<<": "<<count<<"\n";
    }
    return 0;
}
