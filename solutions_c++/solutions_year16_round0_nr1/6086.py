#include <iostream>

using namespace std;

void add_digit(int &check, int a)
{
    while(a) {
        check |= (1<< (a%10) );
        a /=10;
    }
}
int solve(int n)
{
    int check = 0;
    int i=1;
    while (check < (1<<10)-1) {
        add_digit(check, n*i);
        i++;
    }
    return n*(i-1);
}

int main()
{
    int t; cin>>t;
    int i = 1;
    while (t--) {
        int n; cin>>n;
        if (n)
            cout<<"Case #"<<i<<": "<<solve(n)<<endl;
        else 
            cout<<"Case #"<<i<<": "<<"INSOMNIA"<<endl;
        i++;
    }
    return 0;
}
