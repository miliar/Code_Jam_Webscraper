#include <iostream>
#include <sstream>
#include <fstream>
#include <cstdlib>
#include <algorithm>
using namespace std;

/*Precomputed fair and square numbers usign C++ algorithm
bool isPalindrome(long long n){
    ostringstream stringStreamN;
    stringStreamN << n;

    string stringN = stringStreamN.str();
    int size = stringN.size();

    for (int i = 0; i < size / 2; i++){
        if (stringN[i] != stringN[size - 1 - i]){
            return false;
        }
    }

    return true;
}

    cout << "{";
    int howMany = 0;
    for (long long i = 1; i <= 10000000; i++){
        if ( isPalindrome(i) && isPalindrome(i * i) ){
            howMany++;
            cout << i * i << ", " << endl;
        }
    }
    cout << "}" << endl;
    cout << "Total " << howMany << endl;

    39 numbers found at 1-10^14 interval.
*/

long long fairAndSquareArray[39] =
{
1,
4,
9,
121,
484,
10201,
12321,
14641,
40804,
44944,
1002001,
1234321,
4008004,
100020001,
102030201,
104060401,
121242121,
123454321,
125686521,
400080004,
404090404,
10000200001,
10221412201,
12102420121,
12345654321,
40000800004,
1000002000001,
1002003002001,
1004006004001,
1020304030201,
1022325232201,
1024348434201,
1210024200121,
1212225222121,
1214428244121,
1232346432321,
1234567654321,
4000008000004,
4004009004004
};


long long solve(long long A, long long B){
    int answer = 0;

    for (int i = 0; i < 39; i++){
        if (fairAndSquareArray[i] >= A && fairAndSquareArray[i] <= B){
            answer++;
        }
    }

    return answer;
}

int main(){

    ifstream in("C-large-1.in");
    ofstream out("C-large-1.out");

    /*
    in.close();
    out.close();
    return 0;

    fairAndSquareUntil[1] = 1;

    for (int i = 2; i <= 1000; i++){
        fairAndSquareUntil[i] = fairAndSquareUntil[i - 1];
        if (fairAndSquare[i]){
            fairAndSquareUntil[i]++;
        }
    }
    */

    int T;
    in >> T;

    int caseNumber;

    for(caseNumber = 1; caseNumber <= T; caseNumber++){

        long long A, B;
        in >> A >> B;

        out << "Case #" << caseNumber << ": " << solve(A, B) << endl;
    }

    in.close();
    out.close();

    return 0;
}
