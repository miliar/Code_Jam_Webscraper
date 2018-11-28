#include<iostream>
#include<map>
#include<fstream>
#include<string>
#include<sstream>
using namespace std;
int main(){
    ifstream fin("A-large.in");
    ofstream fout("Counting_Sheep_output.out");
    int n;
    fin >> n;
    for(int i = 0 ; i < n ; i++){
        int count = 0;
        map<char,bool> num;
        int m = 0;
        int k;
        string n;
        fin >> k;
        if(k == 0)fout <<"Case #"<<i+1<<": "<< "INSOMNIA" << endl;
        else {
            while(count < 10){
                m = m + k;
                n = to_string(m);
                for(int j = 0 ; j < n.size(); j++){
                    if(count == 10)break;
                    if(!num[n[j]]){
                        num[n[j]] = true;
                        count++;
                    }
                }//cout << "count = " << count << endl;

            }
            fout <<"Case #"<<i+1<<": "<< m << endl;

        }
    }
}
