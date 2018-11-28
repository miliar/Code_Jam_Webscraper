#include <bits/stdc++.h>
using namespace std;

int main()
{
    ofstream ansfile;
    ansfile.open("answer.txt");
    long t,counter_t = 1;
    cin>>t;
    while(counter_t <= t) {
        long n, n_temp, i = 2;
        cin>>n;
        n_temp = n;

        set<int> no_count;

        if(n == 0)
        {
            ansfile<<"Case #"<<counter_t<<": INSOMNIA"<<endl;
            counter_t++;
            continue;
        }
        while(no_count.size() < 10) {

        while(n >= 1) {
                no_count.insert(n%10);
                n/=10;
        }

        if(no_count.size() < 10)
          {
              n = i*n_temp;
              i++;
          }
        }
        ansfile<<"Case #"<<counter_t<<": "<<(i-1)*n_temp<<endl;
        counter_t++;
    }
    ansfile.close();
return 0;
}
