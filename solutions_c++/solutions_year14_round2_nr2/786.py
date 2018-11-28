#include<algorithm>
#include<map>
#include<iomanip>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<iostream>
#include<cstring>
#include <fstream>
#include <stack>

#define FORA(a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define For(b) for(int i=0; i<(b); i++)
#define PB push_back
#define SQR(a) ((a)*(a))
#define ulld unsigned long long int
#define lld unsigned long long int


using namespace std;




int main(){
	ifstream fin("Data.in");
    ofstream fout("Data.out");
    
    int tt;
    fin>>tt;
    int c = 0;
    while(tt--) {
        c++;
        ulld a,b,k;
        fout<<"Case #"<<c<<": ";
        fin>>a>>b>>k;
        ulld total=0;
        if(k>b || k>a)
            total = a*b;
        else {
            total = b*k + (k*(a-k));
            for(ulld i=k; i<a; i++) {
                for(ulld j=k; j<b; j++) {
                    if((i&j) < k) total++;
                }
            }
        }
        
        fout<<total<<endl;
        
    }
    

	return 0;
}

