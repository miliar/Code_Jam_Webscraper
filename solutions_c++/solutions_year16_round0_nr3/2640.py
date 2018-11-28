#include <iostream>
#include <fstream>
#include <vector>
#include <cstdlib>
#include <cmath>
#include <algorithm>

using namespace std;

vector<long long> primeList;
vector<long long> yueshuList;


bool IsPrime(long long n,long long& yueshu)
{
    if (n<2)
    {
        //小于2的数即不是合数也不是素数
        throw 0;
    }
    long long up = sqrt(n);
    for(long long i=2;i<=up;++i)
    {
        // 和比它的一半小数相除，如果都除不尽，证明素数
        if ( 0 == n % i )
        {
            // 除尽了，合数
            yueshu = i;
            return false;
        }
    }
    return true; // 都没除尽，素数
}

int generatePrimes(long long upperBounds){
    for(long long i = 2;i<upperBounds;i++){
        long long yueshu;
        if(IsPrime(i,yueshu)){
            primeList.push_back(i);
            yueshuList.push_back(yueshu);
        }
    }
    return 0;
}

int isprime(long long n,long long& yueshu){
    auto it = find(primeList.begin(),primeList.end(),n);
    if(it != primeList.end()){
        int dis = it - primeList.begin();
        yueshu = yueshuList[dis];
        return true;
    }
    return false;
}

long long toInteger(long long digit,long long base){
    long long result = 0;
    long long currBit;
    long long mishu = 1;
    while(digit){
        currBit = digit & 1;
        result += currBit*mishu;
        mishu *= base;
        digit /= 2;
    }
    return result;
}

void integer2String(long long digit,string& out){
    char lowBit;
    while(digit){
        lowBit = digit%2 + '0';
        out.push_back(lowBit);
        digit >>= 1;
    }
    reverse(out.begin(),out.end());
}

void getNext(long long digit,string& next){
    next.clear();
    digit += 2;
    integer2String(digit,next);
}



int solve(int n,int j,vector<long long>& result,vector<long long>& yueshu){
    //long long upper = pow(10,n);
    //eneratePrimes(upper);
    long long init = 1;
    init = (init << (n-1))+1;
    while(result.size() < j){
        vector<long long> tempYueshuList;
        long long currDigit;
        bool isAllRight = true;
        for(int i = 2;i<11;i++){
            currDigit = toInteger(init,i);
            //currDigit = init;
            long long yueshu ;
            if(!IsPrime(currDigit,yueshu)){
                tempYueshuList.push_back(yueshu);
            }else{
                isAllRight = false;
                break;
            }

        }
        if(isAllRight){
            result.push_back(init);
            for(auto ele:tempYueshuList)
                yueshu.push_back(ele);
        }
        //getNext(currDigit,init);
        init += 2;
    }
    return 0;
}

int main()
{
    ifstream in("test.txt");
    ofstream out("out_large.txt");
    if (! in.is_open()){
        cout << "Error opening file";
    }
    int t;
    string s;
    in>>t;
    int n,j;
    //vector<int> result;
    int lineCount = 1;
    while(t--){
        in>>n>>j;
        vector<long long> result;
        vector<long long> yueshu;
        solve(n,j,result,yueshu);
        out<<"Case #"<<lineCount<<":"<<endl;
        for(int i = 0;i<result.size();i++){
            string s;
            integer2String(result[i],s);
            out<<s;
            int start = i*9;
            int end = start + 9;
            for(int j = start;j<end;j++){
                out<<" "<<yueshu[j];
            }
            out<<endl;
        }
        //lineCount ++;
    }
    in.close();
    out.close();

    return 0;
}
