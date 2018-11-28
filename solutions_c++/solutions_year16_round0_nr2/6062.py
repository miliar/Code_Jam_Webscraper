#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <cmath>
#include <iostream>
#include <vector>
#include <string>

using namespace std;

int main(){
    int T;
    cin >> T;
    vector <string> lists;
    string in;
    for(int i=0;i<T;i++) {
	
            cin >> in;
            lists.push_back(in);
    }
    for(int i=0;i<T;i++){
            int m=0;
            int prev=0;
            int siz=lists[i].length();
            for(int j=0;j<siz;j++){
                if((lists[i][siz-j-1]=='-') && (prev==0)){
                    m++;
                    prev=1;
                }
                else if((lists[i][siz-j-1]=='+') && (prev==1)){
                    m++;
                    prev=0;
                }
            }
            cout << "Case #" << i+1 << ": " << m << endl;
    }
}
