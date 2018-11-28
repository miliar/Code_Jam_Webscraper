#include<bits/stdc++.h>

using namespace std;

int main()
{
    int t, n, a, digit, j;
    vector<int> zero(10, 0);
    ofstream file;
    file.open("E:/outfile.o");

    cin>>t;
    for(int i = 0; i < t; i++)
    {
        cin>>n;
		vector<int> v(10, 1);
		j = 1;
        if(n == 0)
        {
//            cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
            file<<"Case #"<<i+1<<": INSOMNIA"<<endl;
        }
        else
        {
            while(v != zero)
            {
            	a = n;
                while(a > 0)
                {
                    digit = a%10;
                    a /= 10;
					v[digit] = 0;	// digit seen
                }
                n /= j;
                n *= (++j);
            }
//            cout<<"Case #"<<i+1<<": "<<n - (n/j)<<endl;
            file<<"Case #"<<i+1<<": "<<n - (n/j)<<endl;
        }
    }

    return 0;
}
