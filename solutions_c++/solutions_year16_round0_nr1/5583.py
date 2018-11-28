#include<iostream>
#include<fstream>
using namespace std;
#define ull long long int
ull sleep(ull number)
{
    if(number <=0)
        return -1;
    int a[10] = {0};
    int flag = 0;
    ull nu = number;
    ull temp ;
    ull ct = 0;
    while(!flag)
    {
        int help = 1;
        for(int i=0; i<10; i++)
        {
            if(a[i]<=0)
                help = 0;
        }
        if(help)
        {
            flag = 1;
            break;
        }
        ct++;
        number = ct*nu;
        temp = number;
        //cout << number << "\n+++++++\n";
        while((number))
            {
                int digit = number%10;
                a[digit]++;
                number/=10;
            };

    };
//    for(int i=0; i<10; i++)
//        cout << i << " = " << a[i] <<",";
//    cout << endl;
    //cout << nu;
    return nu*ct;


}


int main()
{
    ull n;
    ifstream file;
    ofstream out("/Users/Az/Dropbox/codejam/16_1/out");
    file.open ("/Users/Az/Dropbox/codejam/16_1/inp");
    file >> n;
    ull it = 1;
    while(n--)
    {
        ull number;
        file >> number;
        ull flag = sleep(number);
        if(flag > 0)
            out << "Case #"<<it++<<": "<<flag <<"\n";
        else
            out << "Case #"<<it++<<": "<<"INSOMNIA"<<"\n";
    };
    return 0;
}
