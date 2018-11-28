#include <cstdio>
#include <iostream>
#include <algorithm>

using namespace std;

int files[10000];

int main(){
    int ncases;
    cin >> ncases;
    for(int c = 1;c<=ncases;c++){
        int N;
        int limit;
        cin >> N >> limit;
        for(int i=0;i<N;i++){
            cin >> files[i];
        }
        sort(files,files+N);
        int count = 0;
        int low =0;
        int high = N-1;
        while(low<=high){
            if(low==high){
                //only one remains
                low++;
                high--;
                count++;
            }
            else{
                if(files[low]+files[high]<=limit){
                    low++;
                    high--;
                    count++;
                }
                else{
                    high--;
                    count++;
                }
            }
        }
        printf("Case #%d: %d\n",c,count);
    }
}
