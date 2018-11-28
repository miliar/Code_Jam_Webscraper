#include <iostream>
#include <fstream>
#include <array>

using namespace std;

bool eval2(int arr[10]){
    int sum = 0;
    for(int i=0; i<10; i++){
        sum += arr[i];
    }
    if(sum==0){
        return true;
    }else{
        return false;
    }
}

int eval(int a){
    int b = 0;
    int arr[10] = {1, 1, 1, 1, 1, 1, 1, 1, 1, 1};
    if(a==0){
        return 0;
    }else{
        while(eval2(arr)!=true){
            b += a;
            //cout << b << endl;
            int c = b;
            while(c!=0){
                int d = c % 10;
                arr[d] = 0;
                c /= 10;
            }
        }
    }
    return b;
}

int main(){
    int times;
    //cin >> times;
    int* b;
    b = new int[times];
    for(int i=0; i<times; i++){
        //cin >> b[i];
    }
    
    //string times2;
    ifstream read("/Users/MartinKong/Desktop/Google_Codejam/Google_Codejam/sheepi.txt");
    ofstream write("/Users/MartinKong/Desktop/Google_Codejam/Google_Codejam/sheepL.txt");
    read >> times;
    //cin.ignore(10000, '\n');
    //cout << times << endl;
    
    
    for(int i=0; i<times; i++){
        read >> b[i];
        //cout << b[i] << endl;
    }
    int res;
    for(int j=0; j<times; j++){
        res = eval(b[j]);
        write << "Case #" << j+1 << ": ";
        if(res==0){
            write << "INSOMNIA" << endl;
        }else{
            write << res << endl;
        }
    }
    delete[] b;
}