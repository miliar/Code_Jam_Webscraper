#include <iostream>
#include <fstream>
#include <string>

#define ifname "C-small-attempt0.in"
#define ofname "C-small-attempt0.out"

using namespace std;

char reduce(char r,char c) {

    if ( c == '1' )
        return r;
        
    else if ( c == -'1' )
        return -r;
        
    else if ( r == '1' )
        return c;
        
    else if ( r == -'1' )
        return -c;
        
    else if ( r == c )
        return -'1';
        
    else if ( r == -c )
        return '1';
    
    else if ( r == 'i' ) {
        if ( c == 'j' ) return 'k';
        else if ( c == 'k' ) return -'j';
    }
    
    else if ( r == -'i' ) {
        if ( c == 'j' ) return -'k';
        else if ( c == 'k' ) return 'j';
    }
    
    else if ( r == 'j' ) {
        if ( c == 'i' ) return -'k';
        else if ( c == 'k' ) return 'i';
    }

    else if ( r == -'j' ) {
        if ( c == 'i' ) return 'k';
        else if ( c == 'k' ) return -'i';
    }
    
    else if ( r == 'k' ) {
        if ( c == 'i' ) return 'j';
        else if ( c == 'j' ) return -'i';
    }
        
    else if ( r == -'k' ) {
        if ( c == 'i' ) return -'j';
        else if ( c == 'j' ) return 'i';
    }
    return -1;
}
int main()
{
    int T,test_case,L,X,i,j;
    string str;
    char r, a;
    char ijk[3] = {'i', 'j', 'k'};
    bool canReduce;
    
    ifstream is;
    ofstream os;
    is.open(ifname);
    os.open(ofname);
    
    is  >> T;
    for(test_case = 1; test_case <= T; ++test_case) {
        is >> L >> X;
        is >> str;

        a = str[0];
        for(i = 1; i < L; ++i) {
            a = reduce(a,str[i]);
        }
        r = '1';
        j = 0;
        canReduce = false;
        if ( L > 1 ) {
            while (X--) {

                for(i = 0; i < L; ++i) {
                    r = reduce(r,str[i]);
                    if ( (j < 2) && (r == ijk[j]) ) {
                        r = '1';
                        ++j;
                    }
                }
                
                if ( (j == 2) && (r =='k') ) {
                    r = '1';
                    while (X--) {
                        r = reduce(r,a);
                    }
                    
                    if ( r == '1' ) canReduce = true;
                    
                    break;
                }

            }
        }
        os << "Case #" << test_case << ": ";
        if ( canReduce )
            os << "YES" << endl;
        else
            os << "NO" << endl;
        
    }

    is.close();
    os.close();
    return 0;
}
