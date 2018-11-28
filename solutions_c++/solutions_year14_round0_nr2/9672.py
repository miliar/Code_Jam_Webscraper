#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

double c,f,x;

int getBound(){
    int left = 0,right = 2000;
    while(left <= right){
        int mid = (left + right) / 2;
        double temp1 = x / (2 + mid * f);
        double temp2 = c / (2 + mid * f) + x / (2 + mid * f + f);
        if(temp1 < temp2){
            right = mid - 1;
        }else if(temp1 > temp2){
            left = mid + 1;
        }else if(temp1 - temp2 < 0.0000000001){
            return mid;
        }
    }
    return left;
}

int main(){
    ifstream input("B-small-attempt0.in");
    ofstream output("output.txt");
    int t;
    input >> t;
    for(int cas = 1;cas <= t;cas++){
        input >> c >> f >> x;
        int num = getBound();
        double ans = 0;
        for(int i = 0;i < num;i++){
            ans += c / (2 + i * f);
        }
        ans = ans + x / (2 + num * f);
        output << "Case #" << cas << ": " << fixed << setprecision(7) << ans << endl;
    }
    return 0;
}
