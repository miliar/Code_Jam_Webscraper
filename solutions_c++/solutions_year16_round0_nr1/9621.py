#include <iostream>

using namespace std;

void check(int number, char buffer[10], int &founded)
{
    int digit;
    while(number>0)
    {
        digit = number % 10;
        if (!buffer[digit]) {
            founded++;
            buffer[digit] = 1;
        }
        number/=10;
    }
}

int calculate(int c)
{
    char buffer[10];
    int idx = 1;
    int number;
    int founded = 0;
    for(int i=0;i<10;i++)
        buffer[i] = 0;
    while(true)
    {
        number = c*idx;
        idx++;
        check(number,buffer,founded);

        if (founded == 10) {
            return number;
        }
    }
}

void processCase(int position, int c)
{
    int result;
    if (c == 0)
    {
        cout<<"Case #"<<position<<": "<<"INSOMNIA"<<endl;
        return;
    }
    result = calculate(c);
    cout<<"Case #"<<position<<": "<<result<<endl;
}

int main()
{
    int n;
    int c;
    cin>>n;
    for(int i=0;i<n;i++)
    {
        cin>>c;
        processCase(i+1, c);
    }

}
