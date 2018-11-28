#include <cmath>
#include <iostream>
#include <string>
#include <cstdio>
#include <cassert>
#include <vector>
using namespace std;
typedef unsigned long long ull;
ull checkIfPrime(ull number);
ull power(ull number, ull power);
int main(){
    //FILE *fin = freopen("C-small-attempt0.in", "r", stdin);
    //assert(fin!=NULL);
    FILE *fout = freopen("C-small.out", "w", stdout);
    int test;
    cin >> test;
    for (int i = 0; i < test; i++){
        int length, differentComb;
        cin >> length >> differentComb;
        cout << "Case #" << i+1 << ":" << endl;
        int number[length-2];
        int counter = 0;
        number[1] = 0;
        for (int i = 0; i < length-2; i++)
            number[i] = 0;

        long maxNum = pow(2,length-2);

        for (int i = 0; i < maxNum && counter < differentComb; i++){

            for( int j = 0; j < length-2; j++ ){
                number[j] =  (int)(i / pow(2, length-3-j)) % 2;
            }
            bool found = 1;
            vector<ull> Divisors;
            for (int b = 2; b <= 10; b++){
                ull result = power(b,length-1);

                for (int j = 0; j < length-2 ; j++){
                    result += power(b*number[j], length-2-j);
                }
                result+=1;
                //cout << result << endl;
                ull temp = checkIfPrime(result);
                if (temp != 1){
                    Divisors.push_back(temp);
                }
                else{
                    found = 0;
                    break;
                }
            }
            if (found){
                counter++;
                //cout << counter << endl;
                cout << 1;
                for (int i = 0; i < length-2; i++)
                    cout << number[i];
                cout << 1 << " ";
                for (int i = 0; i < Divisors.size(); i++){
                    cout << Divisors[i];
                    if (i != Divisors.size()-1)
                        cout << " ";// << endl;
                }
                cout << endl;
            }
            //break;
        }
    }
}

ull checkIfPrime(ull number){
    if (number == 0 || number == 1)
        return 0;
    if (number % 2 == 0){
        //cout << number << endl;
        return 2;

    }
    else{
        int count = 2;
        while (count < number){
            if (number % count == 0){
                return count;

            }
            count++;
            if (count > 10000)
                return 1;
        }
        return 1;
    }
}
//double numFinder(double number, long iter, double maxSize, double combinations){
//    cout << number << endl;
//    double counter = 0;
//    if (iter < maxSize){
//        for (double i = 0; i < 2; i++){
//            counter += numFinder( ((number*10)+i), iter+1, maxSize, combinations );
//            if (counter >= combinations)
//                break;
//        }
//        return counter;
//    }
//    else
//        {
//        vector<double> numAndDiv;
//        numAndDiv.push_back((number*10) + 1);
//        for (double b = 2; b <= 10; b++){
//            long temp = (number*10)+1;
//            long result = 0;
//            for (double i = 0; i <= maxSize; i++){
//                result += pow(b*(temp%10),i);
//                temp = temp/10;
//            }
//            //cout << result << endl;
//            temp = checkIfPrime((int)result);
//            if (temp != 1)
//                numAndDiv.push_back(temp);
//            else
//                break;
//        }
//        if (numAndDiv.size() == 10){
//            for (double i = 0; i < numAndDiv.size(); i++)
//                cout << numAndDiv[i] << " ";
//            cout << endl;
//            return 1;
//        }
//    }
//}
ull power(ull number, ull power){
    ull answer = 1;
    for (ull i = 0; i < power; i++){
        answer = answer*number;
    }
    return answer;
}
