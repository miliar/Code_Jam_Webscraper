#include <iostream>
#include <cstdio>
using namespace std;

int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    int index ;
    int arr1[4][4];
    int arr2[4][4];
    int ar1[4];
    int ar2 [4 ];
    int counter =0 ;
    cin >> t;
    int ro1,ro2;
    for (int i=0;i<t;i++){
        int temp ;
        counter =0 ;
        cin >> ro1;
        index=0;
        for (int h=0;h<4;h++){
            for (int q=0;q<4;q++){
                cin >>arr1[h][q];
                if (h==ro1-1){
                    ar1[index]=arr1[h][q];
                    index ++ ;
                }
            }
        }
        cin >>ro2;
        index =0;
        for (int h=0;h<4;h++){
            for (int q=0;q<4;q++ ){
                cin >>arr2[h][q];
                if (h==ro2-1){
                    ar2[index]=arr2[h][q];
                    index ++ ;
                }
            }
        }
        for (int h=0;h<4;h++){
            for (int j=0;j<4;j++){
                if (ar1[h]==ar2[j]){
                    temp =ar1[h] ;
                    counter ++ ;
                }
            }
        }
        cout << "Case #"<<i+1<<": ";
        if (counter ==0 ){
            cout <<"Volunteer cheated!";
        }
        else if (counter ==1){
            cout  <<temp ;
        }
        else {
            cout << "Bad magician!";
        }
        cout << endl ;
    }
    return 0;
}
