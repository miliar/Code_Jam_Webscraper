#include <iostream>
#include <sstream>
#include <cstring>
#include <cstdlib>
using namespace std;


main(){

    int n;
    cin >> n;
    int data = 1;
    while(n){
            string result;
            cin >> result;
            int num = atoi(result.c_str());
            int k = 2;
            int a[11];
            memset(a, 0, sizeof(int)*11);

            int cont = 0;
            int num1;
            bool cond = false;
            int b = 0;
            while(cont < 10){
                stringstream ss;
                for(int i = 0; i < result.size();i++){
                    if(a[result[i] - '0'] == 0){
                        a[result[i] - '0'] = 1;
                        cont++;
                    }
                }
                if(cont < 10)
                    num1 = k*num;
                if(num1 == num) b++;
                if(b == 9) {
                    cond = false;
                    break;
                }
                if(cont == 10) cond = true;
                ss << num1;
                result = ss.str();
                k++;
            }
            if(cond)
                cout << "Case #"<< data<< ": "<<num1 << endl;
            else cout << "Case #"<< data<< ": "<< "INSOMNIA" << endl;
            data++;

        n--;
    }


}
