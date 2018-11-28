#include<iostream>
#include<iomanip>

using namespace std;

int main()
{
    int num; 
    double c;
    double f;
    double x;

    double b;
    double last;
    double result;

    cin >> num;
    for (int i = 1; i <= num; i++)
    {
        int j = 1;
        cin >> c >> f >> x;
        result = x / 2;
        b = 0;
        do 
        {
            last = result;
            b += c / (2 + (j - 1) * f);
            result = x / (2 + j * f) + b;
            j++;
        }
        while(result < last);
        cout << "Case #" << i << ": " << fixed << setprecision(7) << last << endl;
    }
    return 0;
}   

