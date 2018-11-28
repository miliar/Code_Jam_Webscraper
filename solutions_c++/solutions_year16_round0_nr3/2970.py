#include <iostream>
#include <cmath>

using namespace std;

long long findDivisor(long long number) {
    for (long long i = 2; i < number; i++) {
        if (number % i == 0) return i;
    }
}

int prime(int n)
{
    unsigned int d,odmoc,prvocislo;
    if (n<=3)
       prvocislo=1;
       else
         if (n%2==1)
            {
              odmoc=(int) sqrt(n);
              d=3;
              while ((n%d!=0) && (d<odmoc))
                d+=2;
              prvocislo=n%d;
            }
            else prvocislo=0;

    return prvocislo;
}

int main()
{

    //first I generated all binary numbers length 14 with "binaryGenerator" program and added '1' to beginning and end

    //tato cast bola pouzita na ziskanie jamcoinov. Brala zo suboru "list" zoznam vsetkych cisel dlzky 16
    //a do "jamcoins" ulozila jamcoiny
    //this part was used for getting jamcoins. It read from file "list" all numbers long 16
    //and into "jamcoins" it has written jamcoins

  /*  for (int i = 0; i < 16000; i++) {
        string number;
        cin >> number;
        bool flag = true;
        for (int i = 2; i <= 10; i++) {
            long long result = 0;
            for (int j = 0; j < 16; j++) {
                if (number[j] == '1')
                    result += pow(i,15-j);
            }

            if (prime(result)) flag = false;
        }
        if (flag) cout << number << endl;
    }*/


//this part was used to find divisors to jamcoins
    //took "jamcoins", written to "result"
    // I had to skip some jamcoins, program cycled on them, don't know why
   /* for (int i = 0; i < 50; i++) {
        string number;
        cin >> number;
        cout << number;

        for (int i = 2; i <= 10; i++) {
            long long result = 0;
            for (int j = 0; j < 16; j++) {
                if (number[j] == '1')
                    result += pow(i,15-j);
            }
            cout << " " << findDivisor(result);
        }
        cout << endl;
    }
*/

//final code just writes the answer
//it works because I know the input before. I could use the same steps for second (large) input, but program "binaryGenerator fails to generate 30-long numbers

    int t;
    cin >> t;
    int n, j;
    cin >> n >> j;
    cout << "Case #1:" << endl;

    cout << "1011001000000101 3 2 3 2 7 2 3 2 3" << endl;
    cout << "1011001000001001 7 2 3 2 1297 2 17 2 3" << endl;
    cout << "1011001000001011 3 5 22871 3 191 19 3 617 17" << endl;
    cout << "1011001000010001 3 2 3 2 7 2 3 2 3" << endl;
    cout << "1011001000010111 3 2 5 2 7 2 3 2 11" << endl;
    cout << "1011001000101011 17 2 11 2 1297 2 17 2 29" << endl;
    cout << "1011001000101111 3 37 3 3 127 3 3 3253 3" << endl;
    cout << "1011001000110001 11 19 7 13 484151 23 7 8363 29" << endl;
    cout << "1011001000110101 3 2 5 2 7 2 3 2 7" << endl;
    cout << "1011001000111011 3 7 3 3 11 3 3 23 3" << endl;

    cout << "1011001001000001 3 2 3 2 7 2 3 2 3" << endl;
    cout << "1011001001000111 3 2 5 2 7 2 3 2 11" << endl;
    cout << "1011001001001011 13 2 7 2 47779 2 941 2 554531" << endl;
    cout << "1011001001001101 3 2 5 2 7 2 3 2 11" << endl;
    cout << "1011001001010011 3 2 5 2 7 2 3 2 11" << endl;
    cout << "1011001001010111 5 487 3 1087 29 3 491 19 3" << endl;
    cout << "1011001001011111 3 2 5 2 5 2 3 2 11" << endl;
    cout << "1011001001100001 5 1321 19 227 29 5 7 43991 157" << endl;
    cout << "1011001001100101 3 2 5 2 7 2 3 2 11" << endl;
    cout << "1011001001101111 17 2 157 2 5 2 17 2 73" << endl;

    cout << "1011001001110101 5 307 3 19 823 3 10651 11 3" << endl;
    cout << "1011001001110111 3 2 5 2 5 2 3 2 11" << endl;
    cout << "1011001010000101 23 811 7 7 3533 10459 7 11 17981" << endl;
    cout << "1011001010000111 7 2 11 2 4261 2 17 2 13" << endl;
    cout << "1011001010001101 43 2 31 2 19 2 61 2 7" << endl;
    cout << "1011001010010101 3 2 5 2 7 2 3 2 11" << endl;
    cout << "1011001011001011 3 19 3 3 19 3 3 19 3" << endl;
    cout << "1011001011001101 7 89 3 7 20807 3 373631 7 3" << endl;
    cout << "1011001011001111 5 2 17 2 5 2 5 2 13" << endl;
    cout << "1011001011011011 7 2 11 2 5 2 31 2 41" << endl;

    cout << "1011001011100111 13 2 7 2 5 2 67 2 59" << endl;
    cout << "1011001011101011 163 2 67 2 5 2 853 2 7" << endl;
    cout << "1011001011101101 5 2 17 2 5 2 5 2 31" << endl;
    cout << "1011001011110011 61 2 19 2 5 2 41 2 450811" << endl;
    cout << "1011001100000001 3 2 3 2 7 2 3 2 3" << endl;
    cout << "1011001100000111 3 2 5 2 7 2 3 2 11" << endl;
    cout << "1011001100001101 3 2 5 2 7 2 3 2 11" << endl;
    cout << "1011001100010011 3 2 5 2 7 2 3 2 11" << endl;
    cout << "1011001100010111 19 7 3 13 1951 3 173 37 3" << endl;
    cout << "1011001100011001 3 2 5 2 7 2 3 2 11" << endl;

    cout << "1011001100011111 3 2 5 2 5 2 3 2 11" << endl;
    cout << "1011001100100101 3 2 5 2 7 2 3 2 11" << endl;
    cout << "1011001100110111 3 2 5 2 5 2 3 2 11" << endl;
    cout << "1011001100111011 17 2 7 2 5 2 5 2 19" << endl;
    cout << "1011001100111101 3 2 5 2 5 2 3 2 11" << endl;
    cout << "1011001101001001 3 2 5 2 7 2 3 2 11" << endl;
    cout << "1011001101001011 7 5 3 7 12101 3 5 7 3" << endl;
    cout << "1011001101111111 3 2 3 2 7 2 3 2 3" << endl;
    cout << "1011001110000011 5 2 31039 2 29 2 30577 2 13" << endl;
    cout << "1011001110110011 179 2 17669 2 5 2 5 2 17" << endl;

    return 0;
}

