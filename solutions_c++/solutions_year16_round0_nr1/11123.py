#include <iostream>
#include <sstream>
#include <iterator>
#include <string>

using namespace std;

int main(void){
    int T,N;
    
    cin >> T;

    for(int i=1; i <= T; i++){
        cin >> N;
        int L,s=1;
        bool seen[10]={false};
        int nseen=0;
        ostringstream num;
        string snum;
        if(N == 0){
            cout << "Case #" << i << ": INSOMNIA" << endl;
        }else{
            while(nseen < 10){
                L=N*(s++);
                num.clear();
                num.str("");
                num << L;
                snum = num.str();
                for(string::iterator it = snum.begin();
                    it != snum.end();
                    ++it){
                    if(!seen[*it - 48]){
                        nseen++;
                        seen[*it - 48]=true;
                    }
                }
            }
            cout << "Case #" << i << ": " << L << endl;
        }
    }
}

