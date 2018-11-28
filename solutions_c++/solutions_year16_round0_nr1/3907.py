#include <iostream>
using namespace std;

int main() {
    int num;
    int n ;
    cin >> num;
    int alist[10];
    int numa;
    for(int i =0 ; i <num ; i++){
        for(int j =0 ; j < 10 ; j ++){
            alist[j] = 0;
        }
        numa = 0;
        cin  >> n;
        int cnt =1;
        int found = 0;
        int temp;
        while(cnt < 100){
            temp = n*cnt;
            while(temp >0){
                int idx = temp%10;
                temp = temp / 10;
                if(alist[idx] == 0){
                    alist[idx] ++;                    
                    numa ++;
                }
            }
            if(numa == 10){
                found = 1;
                printf("Case #%d: %d\n",i+1,n*cnt);
                break;
            }
            cnt++;

        }
        if(found == 0){
            cout << "Case #" << i+1 << ": INSOMNIA" << endl;
        }
        
    }
}