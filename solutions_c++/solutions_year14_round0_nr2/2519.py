#include <iostream>
#include <algorithm>
#include <vector>
#include <iomanip>

using namespace std;
int caseNum;

double c,f,x;
//determines if a farm should be bought
bool buyFarm(double cookieSpeed){
double noBuy;
double doBuy;
noBuy = (x-c)/cookieSpeed;
cookieSpeed += f;
doBuy = (x)/cookieSpeed;

if(noBuy < doBuy)
    return false;
else
    return true;
}


void solve(){
cin >> c >> f >> x;
double currentSpeed = 2;
double total = 0;

if(x < c)
    total = x/currentSpeed;
else{
    while(buyFarm(currentSpeed)){
    total += c/currentSpeed;
    currentSpeed += f;
    }
    total += (x)/currentSpeed;

   }
cout << "Case #" << setprecision(0) << fixed << caseNum << ": " << setprecision(7) << fixed << total << endl;
caseNum++;
}

int main(){
caseNum = 1;
int t;
cin >> t;
for(int i = 0; i < t;i++){
solve();

}


}
