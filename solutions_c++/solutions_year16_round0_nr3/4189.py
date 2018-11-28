#include<iostream>
#include<cmath>
#define lli long long int

using namespace std;

int arr[16] = {0};

void genr8() { // Whenever called should give the next possible combination

    static int n = 32769;
    int tmp = n;
    int i = 15;
    while (tmp != 1 ) {
        arr[i--] = tmp%2;
        tmp /= 2;
    }
    arr[0] = 1;

    n = n + 2;

}

lli genBase(int base) {
    lli sum = 0;
    for (int i =15,j=0; i>=0 ; i--,j++) {
        sum = sum + (arr[i] * round(pow(base, j))) ;
    }
    return sum;

}

bool isPrime (lli n) {
	lli i = 1;
	if ( n <= 1)
		return false;
	else if ( n == 2)
		return true;
	else
	while ( i++ < sqrt(n) )
		if ( n%i == 0 )
			return false;
	return true;
}

void print() {
    for (int k=0;k<16;k++)
        cout <<arr[k];
    return;
}

int main() {

    int i,ctr = 0;
    int t;
    cin >> t;
    int n,j;
    cin >> n>> j;
    cout << "Case #1:\n";
    while (true) {

        genr8();

        for ( i = 2;i<=10;i++) {

            if (isPrime(genBase(i)) == true)
                break;
        }

        if (i == 11 ){

            print();
            lli tmp;
            for ( int x = 2;x<=10;x++) {

                tmp = genBase(x);
                for (lli y = 3;y<=tmp/2;y++)
                if (tmp%y == 0) {
                    cout << " "<<y;
                    break;
                }
            }
            cout <<'\n';
            ctr++;
        }
        if (ctr == j) break;
    }
    return 0;
}
