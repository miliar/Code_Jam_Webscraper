#include<iostream>
#include<fstream>
#include<string>
#include<bitset>
#include<algorithm>
using namespace std;

int nums[1000];
int main(){
    ifstream in("B.in"); ofstream out("B.out");
    int T;
    in>>T;
    for (int t=0;t<T;t++){
        int N;
        in>>N;
        for (int i=0;i<N;i++) in>>nums[i];
        int ans = 0;
        for (int i=0;i<N;i++){
            int minind = 0;
            for (int j=0;j<N-i;j++){
                if (nums[j]<nums[minind]) minind = j;
            }
            ans += min(minind,N-1-i-minind);
            int tmp = nums[minind];
            for (int j=minind; j<N-i-1;j++){
                nums[j] = nums[j+1];
            }
            nums[N-i-1] = tmp;
        }
        out<<"Case #"<<t+1<<": "<<ans<<"\n";
    }
}
