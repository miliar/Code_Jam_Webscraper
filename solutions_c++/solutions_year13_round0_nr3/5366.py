#include <iostream>
#include <cmath>
#include <fstream>
using namespace std;


/*
*/



int singleDigit(int num)
{
    return (num >= 0 && num < 10);
}
 
bool isPal(int num, int* sNum)
{
    if (singleDigit(num))
        return (num == (*sNum) % 10);
 
    if (!isPal(num/10, sNum))
        return false;
 
    *sNum /= 10;
 
    return (num % 10 == (*sNum) % 10);
}
 
bool isP(int n)
{
 
    int *sNum = new int(n); 
 
    return isPal(n, sNum);
}
int main()
{
    ifstream myReadFile;
    myReadFile.open("C-small-attempt0.in");
    ofstream of;
    of.open("C-small-attempt0.out");
    int t;
    myReadFile >> t;
    int n = 1;
    while(t--){
        int low;
        int high;
        int ans = 0;
        myReadFile >> low;
        myReadFile >> high;
        for(int i = low;i<=high;i++){
                if(sqrt(i) != int(sqrt(i))) continue;
                if(isP(i)&&isP(sqrt(i))) ans++;
        }
        of << "Case #"<<n<<": "<<ans<<endl;
        n++;
    }
    myReadFile.close();
    of.close();
    return 0;
}
