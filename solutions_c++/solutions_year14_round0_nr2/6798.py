#include <iostream>

using namespace std;

int main()
{
    //Taking the number of test cases as the input
    int T;
    cin>>T;
    //Checking for each test case
    for (int i=0; i<T; i++) {
        double C, F, X, time;
        cin>>C>>F>>X;
        double min_time = X/2;   //Defining a minimum initially
        if (X>C) {
            int temp=1;     //For how many times the farm would be brought
            while (true) {
                time = 0;
                for (int a=0; a<temp; a++)
                    time = time + C/(2+(F*a));      //For each time a farm is bought
                time = time + X/(2+(F*temp));
                if (time<min_time) {
                    min_time = time;    //Comparing the situation's time with the minimum time
                    temp++;
                }
                else
                    break;
            }
        }
        //Output
        printf("Case #%d: %.7lf\n", i+1, min_time);
    }
    return 0;
}
