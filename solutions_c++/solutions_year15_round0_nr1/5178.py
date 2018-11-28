// Example program
#include <iostream>
#include <string>
#include <vector>
#include <string>
#include <fstream>
using namespace std;

int main()
{
	ifstream file("A-small-attempt0.in");
	ofstream ofile("out.txt");
    int testNum;
    file>>testNum;
    int maxS;
    string shyls;
    vector<int> shy_vec;
    int cur_stand_p = 0;
    int add_p = 0;
    
    for(int i = 1; i <= testNum;++i) {
        file>>maxS>>shyls;
        for(int j = 0; j < shyls.length(); ++j) {
            shy_vec.push_back(shyls[j]-'0');
        }
        
        for(int k = 0; k < shy_vec.size(); ++k) {
            if(cur_stand_p >= k) {
                cur_stand_p += shy_vec[k];    
            }
            else {
                if(shy_vec[k] > 0){
                    add_p += k-cur_stand_p;
                    cur_stand_p += add_p;
                    cur_stand_p += shy_vec[k];
                }
            }
        }
        ofile<<"Case #"<<i<<": "<<add_p<<endl;
        cur_stand_p = 0;
        add_p = 0;
        shy_vec.clear();
    }
}
