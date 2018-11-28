#include <iostream>
#include <stdio.h>

using namespace std;



int main() {
int testNum ;
int isSolved;
int tab_size_x, tab_size_y;

cin >> testNum;
for(int i = 1;i<=testNum;i++){

    cin >> tab_size_x >> tab_size_y;
    int tab_min_x[tab_size_x], tab_min_y[tab_size_y];
    int tab[tab_size_x][tab_size_y];
    for(int j=0;j<tab_size_y;j++){
        tab_min_y[j] = 0;
    }
    for(int j=0;j<tab_size_x;j++){
        tab_min_x[j] = 0;
    }
    for(int kx=0;kx<tab_size_x;kx++){
        for(int ky=0;ky<tab_size_y;ky++){
            cin >> tab[kx][ky];
            tab_min_x[kx] = (tab[kx][ky] > tab_min_x[kx])?tab[kx][ky]:tab_min_x[kx];
            tab_min_y[ky] = (tab[kx][ky] > tab_min_y[ky])?tab[kx][ky]:tab_min_y[ky];
        }
    }



//    if (i == 3765) {
//    for(int kx=0;kx<tab_size_x;kx++){
//        for(int ky=0;ky<tab_size_y;ky++){
//            cout << tab[kx][ky] << ",";

//        }
//                    cout << endl;
//        }

//    for(int ky=0;ky<tab_size_y;ky++){
//        cout << tab_min_y[ky] << ",";
//    } cout <<endl;
//    for(int kx=0;kx<tab_size_x;kx++){
//        cout << tab_min_x[kx] << ",";
//    } cout <<endl;

//}


    isSolved = 0;
    for(int kx=0;kx<tab_size_x && isSolved == 0;kx++){
        for(int ky=0;ky<tab_size_y;ky++){
            if (!(tab[kx][ky]>=tab_min_x[kx] || tab[kx][ky]>=tab_min_y[ky])) {
            cout <<"Case #" << i << ": NO" <<  endl;
            isSolved =  1;
            break;
            }
        }
    }
    if (isSolved == 0){
        cout <<"Case #" << i << ": YES" <<  endl;
    }

}

return 0;
}
