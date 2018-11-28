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

        int l = 0;

        int maks = 1;

        int temp;
        vector<int> t;
        for(int j = 0; j < s; j++){
               plik>>temp;
               t.push_back(temp);
           }
        sort(t.begin(), t.end());

        int minimum = t[s-1];
        int w;
        for(int j = 1; j <= t[s-1]; j++){
            w = 0;
            for(int k = 0; k < s; k++){
                if(t[k] > j){
                    if(t[k] % j == 0){
                        w += (t[k] / j - 1);
                    }else{
                        w += (t[k] / j);
                    }
                }
            }
            w += j;
            minimum = min(minimum, w);
        }

        out<<"Case #"<<i+1<<": "<<minimum<<endl;
	}
}

