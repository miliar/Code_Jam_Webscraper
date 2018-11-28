#include <stdio.h>
#include <string.h>
#include <iostream>
#include <string>
#include <vector>
#include <cmath>
using namespace std;

#define fori(a,b) for(a=0;(a)<(b);a++)

vector<long long> pal;

bool isPal( long long n ) {
    char tmp[10];
    sprintf(tmp,"%lld",n);
    for (int i=0, j=strlen(tmp)-1; i<j; i++,j--) {
        if (tmp[i]!=tmp[j]) {
            return false;
        }
    }
    return true;
}

void generate() {
    char sum[3] = {4,1,5};
    long long val = 1,tmp;
    
    for( ; val*val < 10e14; val++ ){
        if( isPal(val) ){
            tmp = val*val;
            if( isPal(tmp) ) 
                pal.push_back(tmp);
        }
    }
}

int main() {
    int t,T,i,j;
    long long A,B;
    generate();
    cin>>T;
    
    fori(t,T) {
        cin>>A>>B;
        for (i=0; i<pal.size() && pal[i] < A; i++);
        for (j=pal.size()-1; i>-1 && pal[j] > B; j--);
        cout<<"Case #"<<t+1<<": "<<j-i+1<<endl;
    }
    
    return 0;
}
