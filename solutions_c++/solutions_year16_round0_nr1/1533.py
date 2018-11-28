
//#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <algorithm>
#include <map>
#include <cstdlib>
#include <string>
#include <sstream>

using namespace std;

ifstream cin("/Users/Nagi2/Downloads/GCJ2016/A-large.in");
ofstream cout("/Users/Nagi2/Downloads/aaaL.txt");


int main(int argc, const char * argv[]) {
    int T;
    cin >> T;
    for(int t=0;t<T;t++){
        long long a;
        cin >> a;
        ostringstream oss;
        oss<<a;
        if (a==0)
            cout << "Case #" << t+1<< ": " << "INSOMNIA" << endl;
        else{
            long long b = a;
            map<int,int> mp;
            
            while(mp.size()!=10){
                
                ostringstream oss2;
                oss2<< b;
                for(int i=0;i<oss2.str().size();i++){
                    int z = oss2.str().at(i)-'0';
                    mp[z] = 1;
                }
                b = b + a;
                
            }
            b = b -a;
            cout << "Case #" << t+1<< ": " << b << endl;
            
        }
        


        
    }
    
    return 0;
}
