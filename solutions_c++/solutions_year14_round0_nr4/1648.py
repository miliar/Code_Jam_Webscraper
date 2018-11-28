#include <iostream>
#include <algorithm>
#include <stdio.h>
#include <iomanip>
using namespace std;

#define MAX 1000

double naomi[MAX];
double ken[MAX];
int n;

int deceit_war(){
    int points = 0 ;
    int naomi_i = 0 , naomi_j = n-1 ;
    int ken_i = 0 , ken_j = n-1 ;

    while ( naomi_i <= naomi_j ){
        if ( naomi[naomi_j] > ken[ken_j] ){
            points++;
            naomi_j--;
            ken_j--;
        }else{
            naomi_i++;
            ken_j--;
        }
    }
    return points;
}

int war(){
    int points = 0;
    int naomi_i = 0;
    int ken_i = 0;

    while ( ken_i < n ){
        if( ken[ken_i] < naomi[naomi_i] ){
            ken_i++;
        }else{
            points++;
            ken_i++;
            naomi_i++;
        }
    }
    return n-points;
}

int main(){
    freopen("D-large.in","r",stdin);
    freopen("D-large.out","w",stdout);

    int t,tt=1;
    cin >> t;

    int i,j;

    while ( tt <= t ){
        cin >> n;
        for ( i = 0 ; i < n ; i++ )
            cin>>naomi[i];
        for ( i = 0 ; i < n ; i++ )
            cin>>ken[i];

        sort(naomi,naomi+n);
        sort(ken,ken+n);

        int data1 = deceit_war();
        int data2 = war();
        cout << "Case #" << tt << ": " << data1 << " " << data2 << endl;

        tt++;
    }
return 0;
}
