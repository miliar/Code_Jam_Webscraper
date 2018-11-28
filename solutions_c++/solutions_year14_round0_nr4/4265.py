#include <iostream>
#include <algorithm>
using namespace std;
int n;
double arr1[1005];
int visi1[1005];
double arr2[1005];
int vis2[1005];
void caso(){
    cin >> n;
    for(int i=0;i<n;i++){
        cin >> arr1[i];
        visi1[i] = 0;
    }
    for(int i=0;i<n;i++){
        cin >> arr2[i];
        vis2[i] = 0;
    }
    sort(arr1,arr1+n);
    sort(arr2,arr2+n);
    int ind = n-1;
    int oks=0;
    int cambio = 1;
    while(ind>=0 && cambio == 1){
        cambio = 0;
        int ind2 = n-1;
        while(ind2 >=0 && (vis2[ind2] == 1 || arr2[ind2] > arr1[ind]) ){
           ind2--;
        }
        if(ind2 >= 0){
            cambio = 1;
            vis2[ind2] = 1;
            oks++;
        }
        ind--;
    }
    cout << oks << " ";

    ind = n-1;
    cambio = 1;
    oks=0;
    while(ind>=0 && cambio == 1){
        cambio = 0;
        int ind2 = n-1;
        while(ind2 >=0 && (visi1[ind2] == 1 || arr1[ind2] > arr2[ind]) ){
           ind2--;
        }
        if(ind2 >= 0){
            cambio = 1;
            visi1[ind2] = 1;
            oks++;
        }
        ind--;
    }
    cout << (n - oks) << endl;
}
int main()
{
    int t;
    cin >> t;
    for(int i=1;i<=t;i++){
        cout << "Case #" << i << ": ";
        caso();
    }
    return 0;
}
