#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

class Sq{
    public:
    Sq(bool a, char b){
        this->sign = a;
        this->q = b;
    };
    bool sign;
    char q;
};

Sq table[4][4] = {{Sq(false,'1'),Sq(false,'i'),Sq(false,'j'),Sq(false,'k')},
    {Sq(false,'i'),Sq(true,'1'),Sq(false,'k'),Sq(true,'j')},
    {Sq(false,'j'),Sq(true,'k'),Sq(true,'1'),Sq(false, 'i')},
    {Sq(false,'k'),Sq(false,'j'),Sq(true,'i'),Sq(true,'1')}};

Sq mult(Sq a, Sq b){
    int l,r;
    if(a.q == '1')
        l=0;
    else if(a.q == 'i')
        l = 1;
    else if(a.q == 'j')
        l = 2;
    else if(a.q == 'k')
        l = 3;
    if(b.q == '1')
        r=0;
    else if(b.q == 'i')
        r = 1;
    else if(b.q == 'j')
        r = 2;
    else if(b.q == 'k')
        r = 3;
    Sq result = table[l][r];
    return Sq(result.sign ^ a.sign ^ b.sign, result.q);
}

char buffer[10001];
int main(){
    int T;
    scanf("%d",&T);
    for(int t=0;t++<T;){
        int L, X;
        scanf("%d%d",&L,&X);
        scanf("%s",buffer);
        vector<Sq> input;
        for(int i = 0; i < X; i++)
        for(int j = 0; j < L; j++)
            input.push_back(Sq(false,buffer[j]));
        Sq current = Sq(false,'1');
        uint64_t index = 0;
        //TODO: i
        int success = 1;
        while(1){
            if(current.q == 'i' && !current.sign){
                break;
            }
            if(index == input.size()){
                success = 0;
                break;
            }
            current = mult(current,input[index]);
            index++;
        }
        //TODO: j
        current = Sq(false,'1');
        while(1){
            if(current.q == 'j' && !current.sign){
                break;
            }
            if(index == input.size()){
                success = 0;
                break;
            }
            current = mult(current,input[index]);
            index++;
        }
        //TODO: k 
        current = Sq(false,'1');
        while(1){
            if(current.q == 'k' && !current.sign){
                break;
            }
            if(index == input.size()){
                success = 0;
                break;
            }
            current = mult(current,input[index]);
            index++;
        }
        //TODO: 1
        current = Sq(false,'1');
        while(1){
            if(index == input.size()){
                if(current.q == '1' && !current.sign){
                    break;
                }else{
                    success= 0;
                    break;
                }
            }
            current = mult(current,input[index]);
            index++;
        }
        if(success)
            printf("Case #%d: YES\n", t);
        else
            printf("Case #%d: NO\n", t);
    }
    return 0;
}
