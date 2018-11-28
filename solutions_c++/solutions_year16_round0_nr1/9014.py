
#include <iostream>

using namespace std;

void settle(int *a,long long int number,int &total)
{    int i = 0;
    while(number != 0)
    {
        int n = number%10;
        number = number/10;

        if(a[n]==0)
        {
            a[n] = 1;
            total++;
        }
     }
}

int main()
{
    int n;
    cin>>n;
    int p;

    for(p = 0;p<n;p++) // Inputs everything
    {
       int i = 0,total = 0;
       long long int number,number1;
       int check[10] = {0};
       cin>> number1;


       for(i = 0;i<=100000000;i++){
        number = number1*(i+1);

       settle(check,number,total);
        if(total == 10)
        {

            cout<<"Case #"<<p+1<<": "<<number<<endl;
            break;
        }


        }

        if(total<10)
            cout<<"Case #"<<p+1<<": INSOMNIA"<<endl;


    }



}
