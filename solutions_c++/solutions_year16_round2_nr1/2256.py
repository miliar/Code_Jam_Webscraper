/**
submitted by: prakhar8795
Sleep. Code. Eat. Repeat.
*/

#include<bits/stdc++.h>
using namespace std;


typedef long long int ll ;
typedef unsigned long long int ull ;

void solve()
{
    int test ;
    scanf("%d",&test) ;
    int k=1 ;
    while(test--) {
        string s ;
        cin>>s ;
        int coun[200]={0} ;
        int len = s.length() ;
        for(int i=0 ; i<len ; i++) {
            coun[s[i]]++ ;
        }
        int finalCoun[12]={0} ;
        if(coun['Z']>0) {
            finalCoun[0] += coun['Z'] ;
            coun['E'] -= coun['Z'] ;
            coun['R'] -= coun['Z'] ;
            coun['O'] -= coun['Z'] ;
            coun['Z'] = 0 ;
        }
        if(coun['W']>0) {
            finalCoun[2] += coun['W'] ;
            coun['T'] -= coun['W'] ;
            coun['O'] -= coun['W'] ;
            coun['W'] = 0 ;
        }
        if(coun['G']>0) {
            finalCoun[8] += coun['G'] ;
            coun['E'] -= coun['G'] ;
            coun['I'] -= coun['G'] ;
            coun['H'] -= coun['G'] ;
            coun['T'] -= coun['G'] ;
            coun['G'] = 0 ;
        }
        if(coun['X']>0) {
            finalCoun[6] += coun['X'] ;
            coun['S'] -= coun['X'] ;
            coun['I'] -= coun['X'] ;
            coun['X'] = 0 ;
        }
        if(coun['T']>0) {
            finalCoun[3] += coun['T'] ;
            coun['H'] -= coun['T'] ;
            coun['R'] -= coun['T'] ;
            coun['E'] -= coun['T'] ;
            coun['E'] -= coun['T'] ;
            coun['T'] = 0 ;
        }
        if(coun['R']>0) {
            finalCoun[4] += coun['R'] ;
            coun['F'] -= coun['R'] ;
            coun['O'] -= coun['R'] ;
            coun['U'] -= coun['R'] ;
            coun['R'] = 0 ;
        }
        if(coun['F']>0) {
            finalCoun[5] += coun['F'] ;
            coun['I'] -= coun['F'] ;
            coun['V'] -= coun['F'] ;
            coun['E'] -= coun['F'] ;
            coun['F'] = 0 ;
        }
        if(coun['S']>0) {
            finalCoun[7] += coun['S'] ;
            coun['E'] -= coun['S'] ;
            coun['V'] -= coun['S'] ;
            coun['E'] -= coun['S'] ;
            coun['N'] -= coun['S'] ;
            coun['S'] = 0 ;
        }
        if(coun['I']>0) {
            finalCoun[9] += coun['I'] ;
            coun['N'] -= coun['I'] ;
            coun['E'] -= coun['I'] ;
            coun['N'] -= coun['I'] ;
            coun['I'] = 0 ;
        }
        if(coun['O']>0) {
            finalCoun[1] += coun['O'] ;
            coun['E'] -= coun['O'] ;
            coun['N'] -= coun['O'] ;
            coun['O'] = 0 ;
        }
        string c = "" ;
        printf("Case #%d: ",k) ;
        for(int i=0 ; i<10 ; i++) {
            while(finalCoun[i]>0) {
                c += i+'0' ;
                finalCoun[i]-- ;
            }
        }
        cout<< c ;
        cout<< "\n" ;
        k++ ;
    }
}

int main()
{
    freopen("A-large.in","r",stdin) ;
    freopen("ALargeOut.out","w",stdout) ;
    solve() ;
    return 0 ;
}


