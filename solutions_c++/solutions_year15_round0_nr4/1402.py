#include <iostream>
#include <cstdlib>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;

int f(int x, int c, int r){
    if(c == 1){
            if(r == 1)  return (x == 1 ? 1 : 0);
            if(r == 2)  return ((x == 1 || x == 2) ? 1 : 0);
            if(r == 3)  return (x == 1 ? 1 : 0);
            if(r == 4)  return ((x == 1 || x == 2) ? 1 : 0);
        }else{
            if(c == 2){
                if(r == 1)  return ((x == 1 || x == 2) ? 1 : 0);
                if(r == 2)  return ((x == 1 || x == 2) ? 1 : 0);
                if(r == 3)  return (x != 4 ? 1 : 0);
                if(r == 4)  return ((x == 1 || x == 2) ? 1 : 0);
            }else{
                if(c == 3){
                    if(r == 1)  return (x == 1 ? 1 : 0);
                    if(r == 2)  return (x != 4 ? 1 : 0);
                    if(r == 3)  return ((x == 1 || x == 3) ? 1 : 0);
                    if(r == 4)  return 1;
                }else{
                    if(c == 4){
                        if(r == 1)  return ((x == 1 || x == 2) ? 1 : 0);
                        if(r == 2)  return ((x == 1 || x == 2) ? 1 : 0);
                        if(r == 3)  return 1;
                        if(r == 4)  return (x != 3 ? 1 : 0);
                    }
                }
            }
        }
}

int main(){
    fstream plik;
	fstream out;
    out.open("out.txt");
	plik.open("plik.txt");

	int n;
	plik>>n;

    int x,c,r;
    for(int i = 0; i < n; i++){
        plik>>x;
        plik>>c;
        plik>>r;

        int q = f(x, c, r);
        if(q == 0){
            out<<"Case #"<<i+1<<": RICHARD"<<endl;
        }
        if(q == 1){
            out<<"Case #"<<i+1<<": GABRIEL"<<endl;
        }
    }
}


