#include <iostream>
using namespace std;

class SleepCounter
{
    public:
        SleepCounter();
        virtual ~SleepCounter();
        int main();
        int lastNumber(int N);
    protected:
    private:
};

SleepCounter::SleepCounter()
{
    //ctor
}

SleepCounter::~SleepCounter()
{
    //dtor
}

int lastNumber(int N)
{
    int n = N;
    int lastNumber = 0;
    int counter = 2; //The multiple of N
    char digitArray[] = "1123456789";  //array to eliminate the seen digits
    char comparison[] = "0000000000";

    while(n)
    {
        digitArray[n%10] = '0';     //n%10 is the last digit of n, making the corresponding digit in digit array '0'
        n /= 10;                    //removing the last digit of the number
        if(strcmp(digitArray, comparison) == 0) //If all of the digits are eliminated
        {
            return lastNumber;  //return the last number Beatrice saw
        }
        else if(n == 0)     //If all the digits in the multiple are checked
        {
            n = counter*N;  //move to the next multiple and repeat the process
            if(n == 0)
            {
                return 0;   //If the multiple is 0, there is no chance of eliminating any further digits, sending Beatrice into insomnia
            }
            lastNumber = n;     //keeping track of the lastnumber beatrice saw, because the value of n changes and so does the value of counter
            counter++;
        }
    }
    return 0;

}
int main()
{
    int N, T;
    cin >> T;
    for(int i = 1; i <= T; i++)
    {
        cin >> N;
        cout << "Case #" << i << ": ";
        if (lastNumber(N) == 0)
        {
            cout << "INSOMNIA" << endl;
        }
        else
        {
            cout << lastNumber(N) << endl;
        }
    }
    return 0;
}


