#include<iostream>
#include<vector>
#include<algorithm>
#include<stack>
#include<queue>
#include<cstring>
#include<cstdio>
#include<cmath>
#include<set>
#include<map>
#include<utility>
#include<climits>
 
#define unsigned long long int ulli
# define FRm(i, m, n)     for( int i = m; i <=n; i++)
# define FRrev(i, n)         for( int i = n; i >= 0; i-- )
# define FRrevm(i,n,m)         for( int i = n; i >= m; i-- )
#define max(a,b) ((a)>(b)?(a):(b))
#define S(a) scanf("%d",&(a))
#define P(a) printf("%d",(a))
#define min(a,b) ((a)<(b)?(a):(b))
#define NL printf("\n")
#define sqr(a) ((a)*(a))
#define SL(a) scanf("%lld",&(a))
#define PL(a) printf("%lld",(a))
#define lli long long int
#define FOR(I,A,B) for(int I= (A); I<(B); ++I)
#define inarrd(arr,n) for(int i=0;i<n;i++)S(arr[i]);
#define outarrd(arr,n) for(int i=0;i<n;i++){PFd(arr[i]);PF(" ");}NL;
#define outarrN(arr,n) for(int i=0;i<n;i++){PFd(arr[i]);PFN;}
#include <iostream>
#include <string>
 
 
using namespace std;
 
bool large(int** lawn, int height, int width) {
    for(int i = 0; i < height; i ++) {
        for(int j = 0; j < width; j ++) {
            bool row_valid = true;
            bool col_valid = true;
            
            for(int r = 0; r < height; r ++) {
                if (lawn[r][j] > lawn[i][j]) {
                    col_valid = false;
                    break;
                }
            }
            if (col_valid == true) {
                continue;
            } else {
                for(int r = 0; r < width; r ++) {
                    if (lawn[i][r] > lawn[i][j]) {
                        row_valid = false;
                        break;
                    }
                }
                if (row_valid == false) {
                    return false;
                }
            }
        }
    }
    
    return true;
}
 
int main(int argc, const char * argv[])
{
    int cases = 0;
    std::cin >> cases;
    for(int run = 1; run <= cases; run ++) {
        int height = 0, width = 0;
        std::cin >> height;
        std::cin >> width;
        int **lawn = new int*[height];
        for(int i = 0; i < height; i ++) {
            lawn[i] = new int[width];
            for(int j = 0; j < width; j ++) {
                std::cin >> lawn[i][j];
            }
        }
        
        if (large(lawn, height, width)) {
            std::cout << "Case #" << run << ": YES" << std::endl;
        } else {
            std::cout << "Case #" << run << ": NO" << std::endl;
        }
        
        for(int i = 0; i < height; i ++) {
            delete(lawn[i]);
        }
        delete(lawn);
    }
    return 0;
}
