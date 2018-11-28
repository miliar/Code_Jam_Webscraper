#include <iostream>
#include <fstream>

using namespace std;

int snum[1010];

int main()
{
    int T;
    ifstream in("D:/A-small-attempt1.in");
    ofstream out("D:/A-small-attempt1.out");
    in >> T;
    for(int ci=1; ci<=T; ci++){
        int smax;
        in >> smax;
        string nums;
        in >> nums;
        for(int i=0; i<=smax; i++){
            snum[i] = nums[i]-'0';
        }
        int pcurr=0, pneed = 0;
        if(snum[0] == 0){
            pcurr = 1;
            pneed = 1;
        }
        else{
            pcurr = snum[0];
        }
        for(int i=1; i<=smax; i++){
            if(snum[i] == 0) continue;
            if(pcurr < i){
                pneed += i - pcurr;
                pcurr = i;
            }
            pcurr += snum[i];
        }
        out << "Case #" << ci << ": " << pneed << endl;
    }
    return 0;
}
