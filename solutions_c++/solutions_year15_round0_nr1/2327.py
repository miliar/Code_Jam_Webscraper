#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
    fstream plik;
	fstream out;
    out.open("out.txt");
	plik.open("plik.txt");

	int n;
	plik>>n;

	for(int i = 0; i < n; i++){
        int s;
        plik>>s;
        string a;
        plik>>a;
        int l = 0;
        int o = 0;
        if(s > 0){
            for(int j = 0; j < s + 1; j++){
                if(j > o) {
                        l += (j - o);
                        o += (j - o);
                }
                o += int(a[j]) - 48;
            }
            out<<"Case #"<<i+1<<": "<<l<<endl;
        }else{
            out<<"Case #"<<i+1<<": "<<0<<endl;
        }
	}
}
