#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
using namespace std;


void compare (int array1[][4], int array2[][4], int fir, int sec) {

    int one[4] , two[4] ,count = 0;
    int check[4] = {-1,-1,-1,-1};
    fir = fir -1;
    sec = sec -1;

    for (int j=0;j<4;j++){
            one[j] = array1[fir][j];
            two[j] = array2[sec][j];
    }





   string res= "";

       for(int i = 0;i<4;i++){
            for(int k = 0;k<4;k++){
                if(one[i] == two[k]){
                    count ++;
                    ostringstream ss;
                    ss << one[i];
                    res = ss.str();
                }
            }
        }

   if (count == 1){
      cout << res ;
   }
   else if(count > 1 ){
    cout << "Bad magician!";
   }else if (count == 0){
    cout << "Volunteer cheated!";
   }

}

int main(){
    int case_num, num ,fir, sec;

    ofstream res;
    int first[4][4];
    int second[4][4];

    cin >> case_num;
    for(int i =0;i<case_num;i++){
        cin >> fir;
        for (int j = 0;j<4;j++){
           for(int k=0; k<4;k++){
                cin >> first[j][k] ;
           }
        }

        cin >> sec;

        for (int l = 0;l<4;l++){
           for(int m = 0; m<4;m++){
                cin >> second[l][m] ;
           }

        }
        cout << "Case #" << i+1 <<": ";
        compare(first, second ,fir, sec);
        cout << endl;
    }

return 0;
}
