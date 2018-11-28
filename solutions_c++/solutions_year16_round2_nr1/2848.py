#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <iterator>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <string>
#include <ctime>


using namespace std;

int main() {
    freopen("/Users/Shiva/Desktop/input.in", "r", stdin);
    freopen("/Users/Shiva/Desktop/output", "w", stdout);
    int tc;
    cin>>tc;
    vector<int>ph;
    string s;
    for (int i = 1;i <= tc;i++) {

        
        cin>>s;
        ph.clear();

         size_t f = s.find("Z");
        while(f != string::npos){
            s.replace(f,1,"");
            f = s.find("E");
            s.replace(f,1,"");
            f = s.find("R");
            s.replace(f,1,"");
                        f = s.find("O");
            s.replace(f,1,"");

            f = s.find("Z");
            ph.push_back(0);
        }

         f = s.find("X");
        while(f != string::npos){
            s.replace(f,1,"");
            f = s.find("S");
            s.replace(f,1,"");
            f = s.find("I");
            s.replace(f,1,"");

            f = s.find("X");
            ph.push_back(6);
        }
        f = s.find("W");
        while(f != string::npos){
            s.replace(f,1,"");
            f = s.find("T");
            s.replace(f,1,"");
            f = s.find("O");
            s.replace(f,1,"");

            f = s.find("W");
                        ph.push_back(2);
        }
        f = s.find("G");
        while(f != string::npos){
            s.replace(f,1,"");
            f = s.find("E");
            s.replace(f,1,"");
            f = s.find("I");
            s.replace(f,1,"");
            f = s.find("H");
            s.replace(f,1,"");
            f = s.find("T");
            s.replace(f,1,"");

            f = s.find("G");
                        ph.push_back(8);
        }
        f = s.find("H");
        while(f != string::npos){
            s.replace(f,1,"");
            f = s.find("T");
            s.replace(f,1,"");
            f = s.find("R");
            s.replace(f,1,"");
            f = s.find("E");
            s.replace(f,1,"");
            f = s.find("E");
            s.replace(f,1,"");

            f = s.find("H");
                        ph.push_back(3);

        }
        f = s.find("F");
        while(f != string::npos){
            if(s.find("U") != string::npos){
                s.replace(f,1,"");
                f = s.find("U");
                s.replace(f,1,"");
                f = s.find("O");
                 s.replace(f,1,"");
                f = s.find("R");
                 s.replace(f,1,"");
                             ph.push_back(4);

            }else{
                s.replace(f,1,"");
                f = s.find("I");
                s.replace(f,1,"");
                f = s.find("V");
                 s.replace(f,1,"");
                f = s.find("E");
                 s.replace(f,1,"");
                             ph.push_back(5);


            }
            f = s.find("F");
        }

        f = s.find("V");
        while(f != string::npos){
                s.replace(f,1,"");
                f = s.find("S");
                s.replace(f,1,"");
                f = s.find("E");
                 s.replace(f,1,"");
                f = s.find("E");
                 s.replace(f,1,"");
                f = s.find("N");
                 s.replace(f,1,"");
                f = s.find("V");

                            ph.push_back(7);

        }
        f = s.find("O");
        while(f != string::npos){
                s.replace(f,1,"");
                f = s.find("N");
                s.replace(f,1,"");
                f = s.find("E");
                 s.replace(f,1,"");
                f = s.find("O");
                            ph.push_back(1);
               
        }
        f = s.find("N");
        while(f != string::npos){
                s.replace(f,1,"");
                f = s.find("I");
                s.replace(f,1,"");
                f = s.find("N");
                 s.replace(f,1,"");
                f = s.find("E");
                 s.replace(f,1,"");
                f = s.find("N");
                            ph.push_back(9);

        }
       sort(ph.begin(),ph.end());

       cout<<"Case #"<<i<<": ";
       for(int j=0;j<ph.size();j++){
            cout<<ph[j];
       }
       cout<<endl;
    //    std::ostringstream oss;

    //     if (!ph.empty()){
    // // Convert all but the last element to avoid a trailing ","
    //       std::copy(ph.begin(), ph.end()-1,
    //     std::ostream_iterator<int>(oss, ","));

    // // Now add the last element with no delimiter
    //         oss << ph.back();
    //      }
    //     cout<<"Case #"<<i<<": "<<oss.str()<<endl;
    }
    return 0;
}
