#include<iostream>
#include<fstream>
#include<string>
#include<sstream>
using namespace std;
int main(){
    ifstream fin("B-large.in");
    ofstream fout("B-small-attempt0.out");
    int n;
    fin >> n;
    for(int i = 0 ;i < n ;i++){
        string a;
        fin >> a;
        a = a + "+";
        int j = 0, k = 0;
        int count = 0;
        while(k < a.size()){
            if(a[j] == a[k]){
                k++;
            }else{
                j = k;
                k++;
                count++;
            }
        }
        fout <<"Case #"<<i+1<<": " <<count << endl;
    }

}

