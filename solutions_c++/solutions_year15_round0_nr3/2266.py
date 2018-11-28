#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <iostream>
#include <cmath>
#include <climits>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <bitset>
#include <utility>
using namespace std;


pair<char,int> table(char a,int sign,char b)
{
    if(a == '1')
        return make_pair(b,sign);
    else if(b == '1')
        return make_pair(a,sign);
    else if(a == 'i' && b == 'j')
        return make_pair('k',sign);
    else if(a == 'j' && b == 'i')
        return make_pair('k',-1*sign);
    else if(a == 'i' && b == 'k')
        return make_pair('j',-1*sign);
    else if(a == 'k' && b == 'i')
        return make_pair('j',sign);
    else if(a == 'j' && b == 'k')
        return make_pair('i',sign);
    else if(a == 'k' && b == 'j')
        return make_pair('i',-1*sign);
    else if(a == 'i' && b == 'i')
        return make_pair('1',-1*sign);
    else if(a == 'j' && b == 'j')
        return make_pair('1',-1*sign);
    else 
        return make_pair('1',-1*sign);
}

int main()
{
    // freopen("in","r",stdin);
    // freopen("output","w",stdout);
    int T,cas=1;
    long long int L,X;
    string str;
    scanf("%d",&T);
    while(T--){
        scanf("%lld %lld",&L,&X);
        cin >> str;
        char res = '1';
        int sign = 1;
        int period = X;
        bool aa = false;
        bool bb = false;
        bool cc = false;
        for(int i=0;i<X;i++){
            for(int j=0;j<str.length();j++){
                pair<char,int> pci = table(res,sign,str[j]);
                res = pci.first;
                sign = pci.second;
                // printf("%c %d\n",pci.first,pci.second);
            }
            if(res == '1' && sign == 1){
                period = i+1;
                break;
            }
        }
        int l = X % period;
        char mm = '1';
        int nn = 1;
        for(int i=0;i<2*period;i++){
            for(int j=0;j<str.length();j++){
                pair<char,int> pci = table(mm,nn,str[j]);
                mm = pci.first;
                nn = pci.second;
                if( mm == 'i' && nn == 1)
                    aa = true;
                if(aa == true && mm == 'k' && nn == 1)
                    bb = true;
            }
        }

        if(l>0){
            res = '1';
            sign = 1;
            for(int i=0;i<l;i++){
                for(int j=0;j<str.length();j++){
                    pair<char,int> pci = table(res,sign,str[j]);
                    res = pci.first;
                    sign = pci.second;
                }
            }
        }
        if( aa==true && bb == true && res == '1' && sign == -1)
            printf("Case #%d: YES\n",cas++);
        else
            printf("Case #%d: NO\n",cas++);
    }
}