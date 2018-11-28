#include <iostream>
#include<cmath>
#include<limits.h>
#include<string>

using namespace std;

int T;
long long N;

void prob1()
{

    long long tmp1, tmp2;
    int curN;
    cin >> T;
    int cnt = 0;


    for (int c=1; c<=T; c++)
    {
        cin >> N;
        cout << "Case #" << c << ": ";
        if (N ==0) {
            cout << "INSOMNIA\n";
            continue;
        }

        cnt = 0;
        tmp1 = N;
        long long multip = 1;
        bool arr [10] ={0};

        while ( cnt < 10)
        {
            tmp1 =tmp2= N*multip;
            multip++;

            while (tmp2 > 0)
            {
                curN = tmp2%10;
                tmp2 /= 10;

                if (!arr[curN])
                {
                    cnt++;
                    arr[curN] = true;
                }
            }

        }

        cout << tmp1 << endl;

    }

}

void prob2()
{
    cin >> T;
    string s;
    long long res;
    int sz;
    for (int c=1; c<=T; c++)
    {

        cin >> s;
        res = 0;
        cout << "Case #" << c << ": ";
        sz = s.size();

        for (int i=1; i<sz; i++)
        {
            if (s[i] != s[i-1])
                res++;

        }

        if (s[sz-1] == '-')
            res++;
        cout << res << endl;
    }

}

long long baseToDec(double base, int arr[], int sz){
    long long res=0;
    for (int i=0;i <sz; i++)
        res += arr[i]*pow(base, i);

    return res;
}

long long findDiv(long long num) {

    //long long sq = sqrt((double) num);

    for (long long i=3; i*i<= num; i++)
        if (num%i == 0)
            return i;

    return -1;
}
void decToBin(long long num, int bin[], int sz){
   int i=0;
    while (num > 0)
    {
        bin[i] = num%2;
        num/=2;
        i++;
    }
}
void prob3()
{

    cin >> T;
    cin >> N;
    int J;
    cin >> J;

    cout << "Case #" << 1 << ":\n";
    int successCount = 0;
    const int numLimit = 16;

    long long number , numInNewBase;
    int binary[numLimit]={0};
    binary[0] = 1;
    binary[numLimit-1] = 1;


    number = baseToDec(2.0, binary, numLimit);
    bool isPrime;

    while (successCount < J) {


        // use for given J candidate
        long long divisorsInBase[11];

        isPrime = false;
        for (double base = 2; base <= 10; base++) {
            numInNewBase = baseToDec(base, binary, numLimit);
            long long curDiv = findDiv(numInNewBase);
            if (curDiv == -1){
                isPrime=true;
                break;
            }
            else
                divisorsInBase[(int)base] = curDiv;

        }

        if (!isPrime){
            successCount++;
            for (int i=numLimit-1; i>=0; i--)
            {
                cout << binary[i];
            }

            for (int i=2; i<=10; i++)
                cout <<" " << divisorsInBase[i];
            cout << endl;
        }

        number += 2;
        decToBin(number, binary, numLimit);


    }

}

int main() {
   // cout << "Hello, World!" << endl;
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    //prob1();
  //  prob2();
    prob3();

    return 0;
}