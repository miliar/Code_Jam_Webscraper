#include <iostream>
#include <cstdlib>
#include <string>
#include <queue>
#include <vector>
#include <cmath>

using namespace std;
bool ConvertToAllBase(string);
bool primenumber(long);
bool isnotPrime(long long int);
vector<string> getBitStrings(int);
vector<long> arr;

int main() {
    int T;
    int strSize;
    int numofstr;
    cin >> T;
    cin >> strSize >> numofstr;
    //    string str;
    //    cin >> str;
    cout << "Case #1:"<<endl;
    vector<string> res = getBitStrings(strSize);
    for(vector<string>::iterator it = res.begin(); it != res.end(); ++it) {
        //        cout << *it <<endl;
        if(stoll(*it)%2){
            if(ConvertToAllBase(*it)){
                numofstr--;
            }
            if(numofstr == 0){
                break;
            }
        }
    }
    //    string str = "1000000011000011";
    //    ConvertToAllBase(str);
    return 0;
}

bool ConvertToAllBase(string number)
{
    arr.clear();
    bool isJamCoin = true;
    for(int j = 2; j < 10; j++){
        long long int result = 0;
        long long int i = 0;
        long long int rem;
        long long int num = stoll(number);
        while(num!=0){
            rem  = num%10;
            num/=10;
            result += rem*pow(j,i);
            ++i;
        }
//        cout << result << endl;
        isJamCoin = isJamCoin && isnotPrime(result);
        if(!isJamCoin){
            break;
        }
        //        cout << result << endl;
    }
    if(isJamCoin){
        isJamCoin =  isJamCoin && isnotPrime(stoll(number));
    }
    if(isJamCoin){
        cout << number << " ";
        for(int k = 0; k < arr.size(); k++){
            cout << arr[k] <<" ";
        }
        cout <<endl;
    }
    return isJamCoin;
}

//bool primenumber(long number)
//{
//    for(int i=2; i<100000000; i++)
//    {
//        if(i == number){
//            break;
//        }
//        if(number%i==0){
//            arr.push_back(i);
//            return true;
//        }
//    }
//    return false;
//}

bool isnotPrime (long long int num)
{

        long long int divisor = 3;
        long long int num_d = static_cast<long long int>(num);
        int upperLimit = static_cast<long long int>(sqrt(num_d) +1);
        
        while (divisor <= upperLimit)
        {
            if (num % divisor == 0){
                if(find(arr.begin(), arr.end(), divisor) == arr.end()){
                    arr.push_back(divisor);
                    return true;
                }
            }
            divisor +=2;
        }
        return false;
    
}

vector<string> getBitStrings(int n)
{
    vector<string> result;
    if (n <= 1)
    {
        result.push_back("1");
    }
    else
    {   // recurse, then add extra bit chars
        vector<string> sub = getBitStrings(n-1);
        for (vector<string>::const_iterator it = sub.cbegin();
             it != sub.cend(); ++it)
        {
            result.push_back(*it+'0');
            result.push_back(*it+'1');
        }
    }
    return result;
}