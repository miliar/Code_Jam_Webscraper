#include<bits/stdc++.h>
using namespace std;
int t, k, i, l, j, flip, f;
char s[1005];
int main()
{
    FILE *fp, *fc;
    ifstream fin("A-large (1).in");
    ofstream fout("out.txt");
    fin>>t;
    for(int cas=1;cas<=t;cas++){
        fin>>s>>k;
        i = 0;
        flip = 0;
        f = 0;
        l = strlen(s);
        while(i < l){
            if(s[i] == '+')
                i++;
            else{
                if(i+k-1 >= l){
                    f = 1;
                    break;
                }
                else{
                    j = 0;
                    while(j < k){
                        if(s[j+i] == '+')
                            s[j+i] = '-';
                        else s[j+i] = '+';
                        j++;
                    }
                    i++;
                    flip++;
                }
            }
            if(f)
                break;
        }
        if(f)
            fout<<"Case #"<<cas<<": IMPOSSIBLE"<<endl;
        else fout<<"Case #"<<cas<<": "<<flip<<endl;
    }
    fin.close();
    fout.close();
    return 0;
}
