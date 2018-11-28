#include <iostream>
#include <string>
#include <fstream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
int main()
{
    int t,a,b,ans,flag,tmp;
    int used[20];
    ifstream f_in("A-small-attempt1.in");
    ofstream f_out("answer.out");
    f_in >> t;
    for(int cas = 1; cas <= t; cas++)
    {
        memset(used,0,sizeof(used));
        f_in >> a;
        for(int i = 1; i <= 4; ++i)
        {
            int cnt = 4;
            while(cnt--){
                f_in >> tmp;
                if(i == a)
                    used[tmp] = 1;
            }
        }
        f_in >> b;
        flag = 0;
        for(int i = 1; i <= 4; ++i)
        {
            int cnt = 4;
            while(cnt--){
                f_in >> tmp;
                if(i == b){
                    if(used[tmp] == 1){
                        ans = tmp, flag += 1;
                    }
                }
            }
        }
        if(flag == 1){
            f_out <<"Case #"<<cas<<": "<<ans<<endl;
        }else if(flag == 0){
            f_out <<"Case #"<<cas<<": "<<"Volunteer cheated!"<<endl;
        }else{
            f_out <<"Case #"<<cas<<": "<<"Bad magician!"<<endl;
        }
    }
    return 0;
}
