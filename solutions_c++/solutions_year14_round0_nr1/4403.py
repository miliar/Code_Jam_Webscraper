#include <iostream>
#include <algorithm>
using namespace std;
int arr1[5];
int arr2[5];
void caso(){
    int uno,dos,trash;
    cin >> uno;
    for(int i=1;i<5;i++){
        if(i == uno){
            for(int j=0;j<4;j++){
                cin >> arr1[j];
            }
        }else{
            for(int j=0;j<4;j++){
                cin >> trash;
            }
        }
    }

    cin >> dos;
    for(int i=1;i<5;i++){
        if(i == dos){
            for(int j=0;j<4;j++){
                cin >> arr2[j];
            }
        }else{
            for(int j=0;j<4;j++){
                cin >> trash;
            }
        }
    }

    sort(arr1,arr1+4);
    sort(arr2,arr2+4);

    int ind1,ind2;
    ind1 = 0;
    ind2 = 0;
    while(ind1 < 4 && ind2 < 4 && arr1[ind1] != arr2[ind2]){
        if(arr1[ind1] < arr2[ind2]){
            ind1++;
        }else{
            ind2++;
        }
    }
    if(ind1 >= 4 || ind2 >=4 || arr1[ind1] != arr2[ind2]){
        cout << "Volunteer cheated!" << endl;
        return;
    }
    int solution = arr1[ind1];
    ind1++;
    ind2++;
    while(ind1 < 4 && ind2 < 4 && arr1[ind1] != arr2[ind2]){
        if(arr1[ind1] < arr2[ind2]){
            ind1++;
        }else{
            ind2++;
        }
    }
    if(ind1 >= 4 || ind2 >=4 || arr1[ind1] != arr2[ind2]){
        cout << solution<< endl;
    }else{
        cout << "Bad magician!" << endl;
    }
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
