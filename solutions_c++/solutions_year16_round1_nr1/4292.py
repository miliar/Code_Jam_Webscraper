#include <stdio.h>
#include <string>
#include <fstream>
#include <string>
#include <string.h>
#include <cstdlib>
using namespace std;
int ret[1000];
int getAns(const char * str, int left){
    if(left <= 0){
        return 0;
    }
    int max = 0;
    int l = 0;
    for(int i = 0; i <= left; i++){
        if(str[i] > max){
            max = str[i];
            l = i;
        }
    }
    for(int j = 0; j <= left; j++)
        if(str[j] == max)
            ret[j] = 1;
   // ret[l] = 1;
    printf("Setting %c to 1", str[l]);
    getAns(str, l-1);
    return max;

}

int main(){
    int a;
    ifstream ifs("test6.in");
    ofstream out;
    out.open("output.txt");
    int b;
    ifs >> a;
    string str;
    int val[1000];
    int m;
    int c = -1;

    while (std::getline(ifs, str))
    {
        if(c++ == -1)
            continue;
        out << "Case #" << c << ": ";
        for(int o = 0; o < 1000; o++)
            ret[o] = 0;
        m = getAns(str.c_str(), str.length());
        printf("Max for this round is :%d %c\n", c, m);
        /*for(int u = 0; u < str.length(); u++){
                if(str.at(u) == m && ret[u] != 1){
                    out << str.at(u);
                    ret[u] = 2;
                }
            }
            */
        for(int q = str.length(); q >= 0; q--){
            if(ret[q] == 1){
                out << str.at(q);
            }
        }

            for(int h = 0; h < str.length(); h++){
                if(!ret[h])
                    out << str.at(h);
            }
            out << '\n';
printf("\n");
    }
}