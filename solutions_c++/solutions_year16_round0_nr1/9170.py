#include <iostream>
#include <string>
using namespace std;

bool checkArr(bool arr[10]);

int main(){
    
    int count;
    cin >> count;
    for (int i=0; i<count; i++){
        
        int num;
        cin >> num;
        if (num == 0){
            cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
            continue;
        }
        
        bool arr[10] = {false, false, false, false, false, false, false, false, false, false};
        int ans = num;
        for (int y=2; y<10000; y++){
            
            string str = to_string(ans);
            for (int z=0; z<str.length(); z++){
                switch (str.at(z)){
                        
                    case '0':
                        arr[0] = true;
                        break;
                    case '1':
                        arr[1] = true;
                        break;
                    case '2':
                        arr[2] = true;
                        break;
                    case '3':
                        arr[3] = true;
                        break;
                    case '4':
                        arr[4] = true;
                        break;
                    case '5':
                        arr[5] = true;
                        break;
                    case '6':
                        arr[6] = true;
                        break;
                    case '7':
                        arr[7] = true;
                        break;
                    case '8':
                        arr[8] = true;
                        break;
                    case '9':
                        arr[9] = true;
                        break;
                        
                    default:
                        break;
                        
                }
            }
            
            if (checkArr(arr)){
                break;
            }
            ans = num * y;
            
        }
        
        
        cout << "Case #" << i+1 << ": " << ans << endl;
    }
    
    return 0;
}
bool checkArr(bool arr[10]){
    
    bool done = true;
    for (int i=0; i<10; i++){
        if (arr[i] == false){
            done = false;
            break;
        }
    }
    
    return done;
}