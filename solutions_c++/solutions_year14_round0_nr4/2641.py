#include <iostream>

using namespace std;


int decitfulWar(double *naomi, double *ken, int n){
    int kenMaxPos = n-1;
    int kenMinPos = 0;
    int sum = 0;
    for ( int i = 0; i < n; ++i ){
        if ( naomi[i] < ken[kenMinPos] ){
            // always lose, bomb ken's max
            kenMaxPos--;
        } else {
            kenMinPos++;
            sum++;
        }
    }
    return sum;
}

int war(double *naomi, double *ken, int n){
    for ( int i = 0; i < n; ++i ){
        int hasBigger = 0;
        for ( int j = 0; j < n; ++j ){
            if ( ken[j] > naomi[i] ){
                ken[j] = 0.;
                hasBigger = 1;
                break;
            }
        }
        if ( !hasBigger ){
            return n-i;
        }
    }
    return 0;
}

int main(int argc, char const *argv[]){
    int nCase;
    cin >> nCase;
    for ( int k = 0; k < nCase; ++k ){
        int n;
        cin >> n;
        double *naomi = new double[n];
        double *ken = new double[n];
        for ( int i = 0; i < n; ++i ){
            cin >> naomi[i];
        }
        for ( int i = 0; i < n; ++i ){
            cin >> ken[i];
        }
        // sort two arrays
        for ( int i = 1; i < n; ++i ){
            for ( int j = i; j > 0; j-- ){
                if ( naomi[j] < naomi[j-1] ){
                    double tmp = naomi[j];
                    naomi[j] = naomi[j-1];
                    naomi[j-1] = tmp;
                } else {
                    break;
                }
            }
        }
        // for ( int i = 0; i < n; ++i ){
        //     printf("%f\t", naomi[i]);
        // }
        // cout << endl;
        for ( int i = 1; i < n; ++i ){
            for ( int j = i; j > 0; j-- ){
                if ( ken[j] < ken[j-1] ){
                    double tmp = ken[j];
                    ken[j] = ken[j-1];
                    ken[j-1] = tmp;
                } else {
                    break;
                }
            }
        }
        // for ( int i = 0; i < n; ++i ){
        //     printf("%f\t", ken[i]);
        // }
        // cout << endl;

        printf("Case #%d: %d %d\n", k+1, decitfulWar(naomi, ken ,n), war(naomi, ken, n));
        delete [] naomi;
        delete [] ken;
    }
    return 0;
}