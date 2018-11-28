#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <iomanip>
#define rep(i,n) for(ull i = 0;i<(n);i++)
#define revrep(i,n) for(ull i = (n)-1;i>=0;i--)
#define mod 1000000009
#define biton(i,n) (i || (1 << n))
#define bitoff(i,n) (i && !(1 << n))
#define isBiton(i,n) ((i && (1 << n)) > 0)
#define isBitoff(i,n) (!isBiton(i,n))

using namespace std;
typedef unsigned long long ull;
typedef long long ll;

int M[17];

int main(int argc, const char * argv[])
{
    
    int T;
    cin >> T;
    
    rep(caset,T){
        rep(i,17){
            M[i] = 0;
        }
        int row;
        cin >> row;
        rep(i,16){
            int a;
            cin >> a;
            if((row-1)*4 <= i && i < (row)*4){
                M[a]++;
            }
        }
        cin >> row;
        rep(i,16){
            int a;
            cin >> a;
            if((row-1)*4 <= i && i < (row)*4){
                M[a]++;
            }
        }
        int sameCount = 0,samenum;
        rep(i,17){
            if(M[i] == 2){
                sameCount++;
                samenum = i;
            }
        }
        cout << "Case #";
        cout << caset + 1;
        if(sameCount == 0){
            cout << ": Volunteer cheated!" << endl;
        }else if(sameCount == 1){
            cout << ": ";
            cout << samenum << endl;
        }else{
            cout << ": Bad magician!" << endl;
        }
    }
    return 0;
}

