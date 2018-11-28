#include<bits/stdc++.h>
using namespace std;

struct star{
    int x,y;
    star(int x, int y): x(x), y(y){}
};

bool compareByX(const star &a, const star &b)
{
    return a.x < b.x;
}

double dist(star &a, star &b){
    return sqrt(((a.x-b.x)*(a.x-b.x)) + ((a.y-b.y)*(a.y-b.y)));
}


long long toBase(long long number, long long base){
    long long finalNumber = 0;
    long long place = 1;
    while(number != 0){
        long long rem = number % base;

        // cout<<number<<" "<<rem<<endl;
        finalNumber += rem * place;

        place *= 10;

        number /= base;
        
    }
    return finalNumber;
}

bool isCoinJamNumber(long long number) {
    return false;
}

int solve(long long max) {
    
	return 0;
}

long long isPrime(long long number)
{
    for(long long i = 2; i*i < number; i++)
    {
        // cout<<"isPrime: "<<i<<" "<<number<<endl;
        if(number % i == 0){
            return i;
        }
    }
    return -1;
}

int main(){
    // const long long max = 1111111;
    // int count = 1;
    // int arr[max];



    // for(long long i = 0; i < max; ++i) {
    //     arr[i] = -1;
    // }

    // for(long long i = 2; i < max-1; )
    // {
    //     if(count == 10001)
    //     {
    //         std::cout<<i<<"error"<<endl;
    //         break;
    //     }
    //     //mark all multiples
    //     for(long long j = 2; (j*i) < max-1; ++j)
    //     {
    //         arr[i*j] = j;
    //     }
    //     //find next prime
    //     for(long long k = i+1; k < max-1; k++)
    //     {
    //         if(arr[k] > 1)
    //         {               
    //             i=k;
    //             ++count;
    //             break;
    //         }   
    //     }
    // }


     long long T, N, J, count = 0;
     cin>>T;
     for(long long t = 1; t <= T; t++){
        cin>>N>>J;

        long long ans = 0;//= solve(65536 + 1);
        cout<<"Case #"<<t<<":"<<endl;

        for(long long i = 32769; i < 65535 + 1; i++) {//32769 65535
            // cout<<"loop: "<<i<<endl;
            long long currentNumber = i;
            long long bases[11] = {0,0,0,0,0,0,0,0,0,0,0};
            long long divisors[11] = {0,0,0,0,0,0,0,0,0,0,0};
            long long place = 0, b2Place = 1;
            long long b2Number = 0;
            long long firstDigit = currentNumber % 2, lastDigit = 0;
            while(currentNumber != 0)
            {
                long long base2Remainder = currentNumber % 2; 
                lastDigit = base2Remainder;

                for(int j = 0; j <= 10; j++)
                {
                    // if(currentNumber/2 != 0){
                        bases[j] += base2Remainder * pow(j,place);
                    // }
                }
                b2Number += base2Remainder * b2Place;

                place++;
                b2Place *= 10;

                currentNumber /= 2;
            }
            // cout<<"loop: "<<i<<endl;
            if(!(firstDigit == 1 && lastDigit == 1)) {
                continue;
            }
            // for(int j = 0; j <= 10; j++)
            // {
            //     cout<<"number: "<<i<<", number in b2: "<<b2Number<<", j = "<<j<<", bases: "<<bases[j]<<endl;
            // }

            bool isValid = true;
            for(int j = 2; j <= 10; j++)
            {
                // cout<<"loop: "<<i<<" is prime: "<<j<<endl;
                long long divisor = isPrime(bases[j]);
                if(divisor == -1){
                    isValid = false;
                } else {
                    divisors[j] = divisor;
                }
            }
            // cout<<"loop: "<<i<<endl;
            if(isValid) {
                cout<<b2Number<<" ";

                for(int j = 2; j <= 10; j++)
                {
                    cout<<divisors[j]<<" ";
                }
                cout<<endl;
                count++;
                if(count == 50){
                    break;
                }
            }
            

            // bool isValid = true;
            // for(long long base = 2; base <= 10; base++) {
            //     long long numb = toBase(i, base);
            //     // if(numb > max) {
            //     //     cout<<"error numb > max"<<endl;
            //     // }
            //     long long divisor = isPrime(numb);

            //     if(i == 35) {
            //         cout<<"numb = "<<numb<<", div = "<<divisor<<endl;
            //     }
            //     if(divisor == -1) {
            //         isValid = false;
            //         break;
            //     }
            // }

            // if(isValid) {
            //     cout<<i<<endl;
            // }
        }


        // cout<<"Case #"<<toBase(100,10)<<": "<<ans<<endl;
        // cout<<"Case #"<<t<<": "<<ans<<endl;
     }
}